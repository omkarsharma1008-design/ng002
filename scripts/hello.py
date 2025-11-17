# Simple greeting script: hello.py
# Usage:
#   python scripts/hello.py          # prints "Hello, world!"
#   python scripts/hello.py Alice    # prints "Hello, Alice!"
#
# Keeps behavior simple so you can test it immediately after adding it.

import sys

def greet(name: str = "world") -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"

def main(argv):
    name = argv[1] if len(argv) > 1 else "world"
    print(greet(name))

if __name__ == "__main__":
    main(sys.argv)
