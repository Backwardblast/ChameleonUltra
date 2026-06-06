import re
from pathlib import Path

from chameleon_enum import Command


DEFINE_RE = re.compile(
    r"^#define\s+DATA_CMD_([A-Z0-9_]+)\s+\(?([0-9]+)\)?",
    re.MULTILINE,
)


def _firmware_commands():
    repo_root = Path(__file__).resolve().parents[3]
    header = repo_root / "firmware" / "application" / "src" / "data_cmd.h"
    return DEFINE_RE.findall(header.read_text(encoding="utf-8"))


def test_firmware_command_ids_are_unique():
    entries = _firmware_commands()
    names = [name for name, _ in entries]
    ids = [int(command_id) for _, command_id in entries]

    assert len(names) == len(set(names))
    assert len(ids) == len(set(ids))


def test_python_command_ids_match_firmware():
    firmware = {name: int(command_id) for name, command_id in _firmware_commands()}

    for command in Command:
        assert command.name in firmware
        assert command.value == firmware[command.name]
