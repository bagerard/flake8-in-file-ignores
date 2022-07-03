from flake8_in_file_ignores.flake8_plugin import build_pfi_str, parse_ifi_error_codes


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
