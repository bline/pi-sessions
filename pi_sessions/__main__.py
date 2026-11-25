from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core.resume import ResumeError, ResumeRequest, execute_resume
from .ui.app import PiSessionsApp


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Browse and manage Pi sessions.")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument(
        "--select", action="store_true", help="select a session without launching Pi"
    )
    modes.add_argument(
        "--advanced-select", action="store_true",
        help="keep browser management actions while selecting without launching Pi",
    )
    parser.add_argument(
        "--output", type=Path, metavar="FILE", help="new file for the selected path (JSON string)"
    )
    args = parser.parse_args(argv)
    picker_mode = args.select or args.advanced_select
    if picker_mode and args.output is None:
        parser.error("--select and --advanced-select require --output FILE")
    if args.output is not None and not picker_mode:
        parser.error("--output requires --select or --advanced-select")

    app = PiSessionsApp(select_mode=args.select, advanced_select=args.advanced_select)
    result = app.run()
    if picker_mode and app.return_code:
        return app.return_code
    if not isinstance(result, ResumeRequest):
        return 0

    if args.output is not None:
        try:
            with args.output.open("x", encoding="utf-8") as output:
                json.dump(str(Path(result.file).absolute()), output)
                output.write("\n")
        except OSError as e:
            print(f"Could not write selection: {e}", file=sys.stderr)
            return 1
        return 0

    try:
        execute_resume(result)  # replaces process; does not return on success
    except ResumeError as e:
        print(f"Resume failed: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
