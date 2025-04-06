import argparse
import os
import sys
from pathlib import Path
from typing import Any, override

from west.commands import WestCommand

sys.path.append(os.fspath(Path(__file__).parent.parent))


class GaleCheckout(WestCommand):
    def __init__(self) -> None:
        super().__init__(
            "hello",
            "print hello",
            "Print hello to a someone. Usage: west hello <name>",
        )

    @override
    def do_add_parser(self, parser_adder: Any) -> argparse.ArgumentParser:
        parser: argparse.ArgumentParser = parser_adder.add_parser(
            self.name,
            help=self.help,
            description=self.description,
        )
        _ = parser.add_argument("name", type=str, help="name of the person to greet")
        return parser

    @override
    def do_run(self, args: argparse.Namespace, unknown: list[str]) -> None:
        if not args.name:
            self.die("Please provide a name")  # pyright: ignore[reportUnknownMemberType]
        else:
            self.inf(f"Hello, {args.name}!")  # pyright: ignore[reportUnknownMemberType]
