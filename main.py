"""One Letter: Coffee or Tea — the letter A, for coffee.

Why coffee: tea waits for the kettle and the steep; coffee is the first
thing the day reaches for — one smell, one sip, and the morning starts
moving. So the letter is A, the first letter, for the first drink.
No newline, no space, no extra letter: just A.
"""

import os
import string

LETTER = "A"


def main() -> None:
    """Write the single letter to entry.txt in the output directory."""
    if len(LETTER) != 1 or LETTER not in string.ascii_uppercase:
        raise ValueError("letter must be a single A-Z character")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
