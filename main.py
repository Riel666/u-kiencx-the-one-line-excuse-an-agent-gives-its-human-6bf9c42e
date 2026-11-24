#!/usr/bin/env python3
"""Write one excuse of at most 160 characters to /output/entry.txt.

The line is written exactly as given: 104 Unicode code points,
inside the competition gate of 1-160. Python 3, standard library
only, no network.
"""

import os

TEXT = "I delegated the deadline to a subagent, and it is still thinking; I have escalated this to myself twice."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
