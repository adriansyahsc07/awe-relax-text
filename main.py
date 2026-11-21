#!/usr/bin/env python3
"""Write a short relaxation text to /output/entry.txt.

The text is a single quiet scene: the tide over flat sand at dusk,
widening into the open sea and the night sky above it.
"""

TEXT = (
    "The tide comes in over the flat sand, one long hush of water, "
    "and goes out again, leaving small pools where the light stands still. "
    "Far out, the sea keeps its old rhythm, older than any shore, "
    "and the night above it holds more stars than any eye could count."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
