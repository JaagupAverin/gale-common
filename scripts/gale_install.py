import argparse
import os
import sys
from pathlib import Path
from typing import Any, override

from west.commands import WestCommand

sys.path.append(os.fspath(Path(__file__).parent.parent))


class GaleInstall(WestCommand):
    def __init__(self) -> None:
        super().__init__(
            "gale-install",
            "GaleInstall",
            "Install requirements for Gale development. Usage: west gale-install",
        )

    @override
    def do_add_parser(self, parser_adder: Any) -> argparse.ArgumentParser:
        parser: argparse.ArgumentParser = parser_adder.add_parser(
            self.name,
            help=self.help,
            description=self.description,
        )
        return parser

    @override
    def do_run(self, args: argparse.Namespace, unknown: list[str]) -> None:
        requirements_path = Path(__file__).parent.parent / "requirements.txt"
        if not requirements_path.exists():
            self.die(f"requirements.txt not found at {requirements_path}")  # pyright: ignore[reportUnknownMemberType]
        else:
            self.inf(f"Installing requirements from {requirements_path}...")  # pyright: ignore[reportUnknownMemberType]
            os.system(f"{sys.executable} -m pip install -r {requirements_path}")
