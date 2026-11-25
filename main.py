"""Entry for make.fun: One Line, One Laugh.

Therapy advice taken literally, at 3 a.m., into a fridge door.
"""
import os

LINE = "My therapist said to confront my problems head-on, so I walked straight into the fridge door at 3 a.m. looking for answers and cake."
MAX_CHARS = 200


def write_entry(out_dir):
    if not LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry must be one non-empty line within the limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
