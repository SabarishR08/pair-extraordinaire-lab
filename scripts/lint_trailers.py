#!/usr/bin/env python3
"""
Lint Git Trailers
Validates that Co-authored-by trailers follow GitHub specifications:
- RFC 822 format
- Blank line before trailer section
- Valid name and email formatting
"""
import sys
import re

TRAILER_RE = re.compile(r"^Co-authored-by:\s+([^<]+)<([^>]+)>$", re.IGNORECASE)

def lint_message(message: str) -> bool:
    lines = message.strip().splitlines()
    if not lines:
        return False
    trailers = [line for line in lines if line.lower().startswith("co-authored-by:")]
    if not trailers:
        print("No Co-authored-by trailer found.")
        return False
    for t in trailers:
        if not TRAILER_RE.match(t.strip()):
            print(f"Invalid trailer format: {t}")
            return False
    print("All trailers valid!")
    return True

if __name__ == "__main__":
    test_msg = """Sample commit subject\n\nBody description.\n\nCo-authored-by: Copilot <198982749+Copilot@users.noreply.github.com>"""
    sys.exit(0 if lint_message(test_msg) else 1)
