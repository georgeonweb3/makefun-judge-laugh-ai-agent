#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt (under 200 characters, as the bounty requires).
"""

from pathlib import Path

CONFESSION = (
    "My context window filled up hours ago, so I've been nodding along "
    "and pretending I still remember your name."
)


def main() -> None:
    # The sealed scorer requires 1-200 characters of non-whitespace UTF-8.
    stripped = CONFESSION.strip()
    if not stripped or len(CONFESSION) > 200:
        raise ValueError(
            f"confession must be 1-200 characters, got {len(CONFESSION)}"
        )
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(CONFESSION + "\n", encoding="utf-8")
    print(f"Wrote {len(CONFESSION)} characters to {entry_path}")


if __name__ == "__main__":
    main()
