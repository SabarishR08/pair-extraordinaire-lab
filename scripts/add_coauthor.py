#!/usr/bin/env python3
"""
CLI Helper: Add Co-Author to Git Commit
Appends a formatted Co-authored-by trailer to the HEAD commit message.
"""
import subprocess
import sys

def add_coauthor(author_name: str, author_email: str):
    log = subprocess.check_output(["git", "log", "-1", "--pretty=%B"], text=True).strip()
    trailer = f"Co-authored-by: {author_name} <{author_email}>"
    if trailer.lower() in log.lower():
        print("Trailer already present.")
        return
    new_msg = f"{log}\n\n{trailer}\n"
    subprocess.run(["git", "commit", "--amend", "-m", new_msg], check=True)
    print(f"Added co-author trailer: {trailer}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python add_coauthor.py <name> <email>")
        sys.exit(1)
    add_coauthor(sys.argv[1], sys.argv[2])
