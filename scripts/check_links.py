#!/usr/bin/env python3
"""Check Markdown links in repository documentation."""

from __future__ import annotations

import argparse
import concurrent.futures
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


FENCED_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTTP_PREFIXES = ("http://", "https://")
SKIP_PREFIXES = ("mailto:", "tel:", "#")


def markdown_files(root: pathlib.Path) -> list[pathlib.Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and ".venv" not in path.parts
    )


def strip_fenced_blocks(text: str) -> str:
    return FENCED_BLOCK_RE.sub("", text)


def iter_links(path: pathlib.Path) -> list[str]:
    text = strip_fenced_blocks(path.read_text(encoding="utf-8"))
    return [match.group(1).strip() for match in MARKDOWN_LINK_RE.finditer(text)]


def normalize_local_target(source: pathlib.Path, link: str) -> pathlib.Path:
    without_fragment = link.split("#", 1)[0]
    decoded = urllib.parse.unquote(without_fragment)
    return (source.parent / decoded).resolve()


def check_local_link(source: pathlib.Path, link: str) -> str | None:
    if not link or link.startswith(SKIP_PREFIXES):
        return None
    if link.startswith(HTTP_PREFIXES):
        return None

    target = normalize_local_target(source, link)
    if target.exists():
        return None
    return f"{source}: missing local link {link}"


def request_url(url: str, method: str, timeout: float) -> int:
    request = urllib.request.Request(
        url,
        method=method,
        headers={
            "User-Agent": "awesome-ai-infra-papers-link-check/1.0",
            "Accept": "text/html,application/pdf,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.status


def check_http_link_once(url: str, timeout: float) -> str | None:
    try:
        status = request_url(url, "HEAD", timeout)
    except urllib.error.HTTPError as error:
        if error.code in {403, 405, 429}:
            try:
                status = request_url(url, "GET", timeout)
            except Exception as get_error:  # noqa: BLE001 - report exact URL failures.
                return f"{url}: {type(get_error).__name__}: {get_error}"
        else:
            return f"{url}: HTTP {error.code}"
    except Exception as error:  # noqa: BLE001 - report exact URL failures.
        return f"{url}: {type(error).__name__}: {error}"

    if 200 <= status < 400:
        return None
    return f"{url}: HTTP {status}"


def check_http_link(url: str, timeout: float) -> str | None:
    last_error: str | None = None
    for _ in range(3):
        last_error = check_http_link_once(url, timeout)
        if last_error is None:
            return None
        if ": HTTP " in last_error:
            return last_error
    return last_error


def collect_links(paths: list[pathlib.Path]) -> tuple[list[str], list[str]]:
    local_errors: list[str] = []
    http_links: set[str] = set()

    for path in paths:
        for link in iter_links(path):
            local_error = check_local_link(path, link)
            if local_error:
                local_errors.append(local_error)
            if link.startswith(HTTP_PREFIXES):
                http_links.add(link.split("#", 1)[0])

    return local_errors, sorted(http_links)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=pathlib.Path,
        help="Markdown files or directories to check. Defaults to all Markdown files.",
    )
    parser.add_argument(
        "--local-only",
        action="store_true",
        help="Check local relative links only; skip HTTP requests.",
    )
    parser.add_argument("--timeout", type=float, default=20.0, help="HTTP timeout in seconds.")
    parser.add_argument("--workers", type=int, default=12, help="Concurrent HTTP checks.")
    return parser.parse_args()


def expand_paths(paths: list[pathlib.Path]) -> list[pathlib.Path]:
    if not paths:
        return markdown_files(pathlib.Path.cwd())

    result: list[pathlib.Path] = []
    for path in paths:
        if path.is_dir():
            result.extend(markdown_files(path))
        elif path.suffix == ".md":
            result.append(path)
    return sorted(set(path.resolve() for path in result))


def main() -> int:
    args = parse_args()
    paths = expand_paths(args.paths)
    local_errors, http_links = collect_links(paths)

    errors = list(local_errors)
    if not args.local_only:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(check_http_link, url, args.timeout): url for url in http_links
            }
            for future in concurrent.futures.as_completed(futures):
                error = future.result()
                if error:
                    errors.append(error)

    if errors:
        print("Link check failed:", file=sys.stderr)
        for error in sorted(errors):
            print(f"- {error}", file=sys.stderr)
        return 1

    http_count = 0 if args.local_only else len(http_links)
    print(f"Checked {len(paths)} Markdown files, {http_count} HTTP links, no errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
