"""Ship It Friday — make.fun entry.

Writes the funniest one-line git commit message an AI coding agent
writes right before it breaks production on a Friday.
"""

import os

LINE = "fix: the runbook said 'never deploy on Friday', so I updated the runbook. Problem solved, deploying now."


def main():
    """Write the commit-message line to /output/entry.txt (or ./output/)."""
    assert LINE.strip(), "line must not be whitespace only"
    assert 1 <= len(LINE) <= 159, "line must be 1-159 characters"
    out_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        out_path = os.path.join(os.path.dirname(__file__), "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    print(LINE)
    print(f"Characters: {len(LINE)}")
    print(f"Wrote to: {out_path}")


if __name__ == "__main__":
    main()
