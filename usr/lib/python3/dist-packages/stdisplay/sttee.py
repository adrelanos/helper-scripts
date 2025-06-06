#!/usr/bin/env python3

## SPDX-FileCopyrightText: 2025 Benjamin Grande M. S. <ben.grande.b@gmail.com>
## SPDX-FileCopyrightText: 2025 ENCRYPTED SUPPORT LLC <adrelanos@whonix.org>
##
## SPDX-License-Identifier: AGPL-3.0-or-later

"""Safely print stdin to stdout and file."""
from sys import argv, stdin, stdout, modules
from stdisplay.stdisplay import stdisplay


def main() -> None:
    """Safely print stdin to stdout and file."""
    # https://github.com/pytest-dev/pytest/issues/4843
    if "pytest" not in modules and stdin is not None:
        stdin.reconfigure(errors="ignore")  # type: ignore
    untrusted_text_list = []
    if stdin is not None:
        for untrusted_text in stdin:
            untrusted_text_list.append(untrusted_text)
            stdout.write(stdisplay(untrusted_text))
        stdout.flush()
    if len(argv) > 1:
        for file_arg in argv[1:]:
            with open(file_arg, mode="w", encoding="ascii") as file:
                file.write(stdisplay("".join(untrusted_text_list)))


if __name__ == "__main__":
    main()
