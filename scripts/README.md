# Scripts

Small maintenance utilities for this repository.

## Link checking

Check only local Markdown references:

```bash
python3 scripts/check_links.py --local-only
```

Check local references and HTTP links:

```bash
python3 scripts/check_links.py
```

Some publishers and GitHub pages may block scripted `HEAD` or `GET` requests. If a link is known to work in a browser, keep it and note the automated-check limitation in the change description.
