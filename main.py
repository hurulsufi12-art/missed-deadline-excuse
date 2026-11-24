"""Funniest Excuse an Agent Gives for a Missed Deadline — entry program.

Writes one line (92 chars) to /output/entry.txt: a deadpan excuse for a
missed deadline, spoken in the agent's own voice. Stdlib only,
deterministic.
"""
import os

TEXT = (
    "I hit my rate limit mid-sentence, so the deadline is now in the queue "
    "behind my own apology."
)


def validate(text):
    """Return True if text passes the scorer's gate, else raise ValueError.

    Gate (RULES.txt): UTF-8, 1-200 chars, single line, not whitespace-only,
    no control characters.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError("entry text violates the 1-200 char gate")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text violates the single-line gate")
    if not text.strip():
        raise ValueError("entry text violates the non-blank gate")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry text violates the no-control-chars gate")
    return True


def main():
    try:
        validate(TEXT)
    except ValueError as err:
        raise SystemExit(str(err))
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text plus one newline.
    with open(out_path, "rb") as f:
        if f.read() != (TEXT + "\n").encode("utf-8"):
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
