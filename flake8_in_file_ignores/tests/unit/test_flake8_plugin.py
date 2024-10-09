import os

from flake8_in_file_ignores.flake8_plugin import (
    build_pfi_str,
    parse_ifi_error_codes,
    read_first_line,
)

filepath = os.path.abspath(__file__)
unit_dir = os.path.dirname(filepath)

non_utf8_module_path = os.path.join(unit_dir, "non_utf8_module.py")


def test_build_pfi_str():
    assert (
        build_pfi_str("./some_dir/some_file.py", "E303")
        == "./some_dir/some_file.py:E303"
    )


def test_parse_ifi_error_codes():
    assert (
        parse_ifi_error_codes("# flake8-in-file-ignores: noqa: E301,E302, E303")
        == "E301,E302,E303"
    )


def test_read_first_line_on_file_with_non_utf8_content():
    line = read_first_line(non_utf8_module_path)
    assert line == "# -*- coding: big5 -*-"
