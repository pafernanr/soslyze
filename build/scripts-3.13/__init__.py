#!python
import os
import sys

sys.path.insert(0, "/usr/lib/tools/")

try:
    sys.path.insert(0, os.getcwd())
    from soslyze import SoSLyze
except KeyboardInterrupt as exc:
    raise SystemExit() from exc


def main():
    SoSLyze()
    os._exit(0)


if __name__ == '__main__':
    main()
