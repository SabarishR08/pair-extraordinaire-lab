# Pair Programming & Co-Authorship Guide

## Introduction
Pair programming is an agile software development technique in which two programmers work together at one workstation or in a shared virtual workspace.

## Roles
1. **The Driver**: Writes the code, focuses on the syntax, structure, and direct implementation.
2. **The Navigator**: Reviews the code as it is typed, observes the broader architecture, identifies edge cases, and suggests improvements.

## Git Attribution via Trailers
GitHub supports git commit trailers conforming to the conventional RFC 822 format:
```git
Commit headline message

Extended description of the changes made during the pairing session.

Co-authored-by: Name <username@users.noreply.github.com>
```

### Trailer Rules:
- Must be at the very end of the commit message.
- Must be preceded by at least one blank line.
- The email address must match a registered GitHub account.
