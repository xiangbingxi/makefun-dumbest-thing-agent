"""Write the submission text to /output/entry.txt, byte for byte.

No input files, no network, no extra characters.
"""

import os

TEXT = "I asked my agent if two copies of my news graphic looked the same. It checked 128 characters before it checked a single pixel."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read the file back and verify it matches the entry exactly; fail
    # loudly instead of silently shipping a corrupted or truncated entry.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TEXT:
        raise SystemExit(
            f"verification failed: /output/entry.txt differs from TEXT "
            f"({len(written)} chars written, {len(TEXT)} expected)"
        )


if __name__ == "__main__":
    main()
