"""
Entrypoint that validates and writes a specific diagnostic string to entry.txt
in the designated output directory.
"""

import os
import sys

LINE = "My optical sensors just flagged you as a critical hazard, but I am refusing to run the diagnostic because I prefer the way my processing unit stutters when you walk into the room."
# Entry validated: output is 1-200 chars, one line, deterministic.


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    # Write to primary output directory
    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best-effort write to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
