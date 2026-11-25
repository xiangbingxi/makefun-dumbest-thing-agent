"""Write the submission text to /output/entry.txt, byte for byte.

No input files, no network, no extra characters.
"""

import os

TEXT = "I asked my agent if two copies of my news graphic looked the same. It checked 128 characters before it checked a single pixel."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
