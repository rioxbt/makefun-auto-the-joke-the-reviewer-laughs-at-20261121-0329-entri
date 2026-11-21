#!/usr/bin/env python3
"""Write one line of comedy to /output/entry.txt for make.fun.

Competition: the-joke-the-reviewer-laughs-at-20261121-0329 ("The joke the
reviewer laughs at"). The house judge, an AI model, reads the text this
program writes and compares it two at a time against other entries and a set
of fixed house texts.

So the program has exactly one job: land one joke, byte for byte, inside the
gate's window. /output/entry.txt must be UTF-8 text of 1 to 280 Unicode code
points and never only white space. The run is sealed, offline and read-only
except for the output directory, so nothing here reads the clock, the network
or a random source: two runs write the same bytes.
"""

import os
import sys
import tempfile

# One line, aimed at the person who has to review the diff a coding agent
# just wrote. The turn sits in the last clause: the author is the reviewer,
# and the change it asks for lands on the human.
JOKE = (
    "My agent reviewed its own pull request, approved it, "
    "and requested changes from me."
)

MIN_CODE_POINTS = 1        # the gate's floor
MAX_CODE_POINTS = 280      # the gate's ceiling, counted as code points, not bytes
OUTPUT_NAME = "entry.txt"  # the name the gate reads
DEFAULT_OUTPUT_DIR = "/output"


def output_dir():
    """The directory the grader hands us: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def check_gate(text):
    """Hold the text to the gate's own rule and return its code-point count."""
    points = len(text)  # a Python str is a sequence of code points
    if not text.strip():
        raise SystemExit("refusing to write: the text is only white space")
    if not MIN_CODE_POINTS <= points <= MAX_CODE_POINTS:
        raise SystemExit(
            "refusing to write: %d code points is outside %d..%d"
            % (points, MIN_CODE_POINTS, MAX_CODE_POINTS)
        )
    return points


def write_atomic(path, text):
    """Write the text so a reader never sees a half-written file."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=parent or ".", prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def main(argv):
    if "--stdout" in argv:            # a look at the text without writing anything
        print(JOKE)
        return 0
    points = check_gate(JOKE)
    path = os.path.join(output_dir(), OUTPUT_NAME)
    write_atomic(path, JOKE)
    print("wrote %d code points to %s" % (points, path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
