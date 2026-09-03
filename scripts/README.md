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

Some publishers and GitHub pages may block scripted `HEAD` or `GET` requests. The checker treats an ACM DOI returning `403` to both methods as a known automated-access block; other HTTP failures still fail the check.
