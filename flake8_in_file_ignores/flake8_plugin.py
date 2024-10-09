from typing import List

# metadata
__version__ = "0.3.0"

from flake8.discover_files import expand_paths

CODE_PREFIX = "IFI"  # stands for "In File Ignores"


IFI_TAG = "# flake8-in-file-ignores:"
IFI_FULL_TAG = "# flake8-in-file-ignores: noqa:"


def read_first_line(filepath: str) -> str:
    with open(filepath, errors="ignore") as f:
        first_line = f.readline().rstrip()
    return first_line


def build_pfi_str(filepath: str, error_codes_csv: str):
    # the way per_file_ignores expects it
    return f"{filepath}:{error_codes_csv}"


def get_ifi_noqa(filepaths: List[str]) -> List[str]:
    ifi_noqa_item = []
    for file_path in filepaths:
        # print(f"Checking {file_path}")
        first_line = read_first_line(file_path)
        if IFI_TAG in first_line:
            error_codes = parse_ifi_error_codes(first_line)
            ifi_noqa_item.append(build_pfi_str(file_path, error_codes))
    return ifi_noqa_item


def parse_ifi_error_codes(line: str) -> str:
    """Parses line like
    # flake8-in-file-ignores: noqa: E731,E123
    to extract the code
    """
    if IFI_FULL_TAG not in line:
        raise Exception(
            f"flake8-in-file-ignores plugin expects to find `{IFI_FULL_TAG}`, which is different from what it found on line `{line}`"
        )

    line = line.replace(IFI_FULL_TAG, "")
    return line.replace(" ", "").strip()


class MyFlake8Plugin:
    version = __version__
    name = "flake8-infile-ignores"
    code_prefix = CODE_PREFIX

    def __init__(self, tree, filename: str):
        self.tree = tree

    @classmethod
    def parse_options(cls, option_manager, options, args):
        # print(option_manager, options, args)
        excludes = (*options.exclude, *options.extend_exclude)
        filepaths = cls.get_files(options, excludes)
        # print(f"{filepaths=}")
        ifi_noqa_strs = get_ifi_noqa(filepaths)
        if ifi_noqa_strs:
            # original_pfi = options.per_file_ignores
            concat_pfi = " ".join(ifi_noqa_strs)
            options.per_file_ignores += " " + concat_pfi
            # print(
            #     f"flake8-in-file-ignores - Patching options.per_file_ignores from `{original_pfi}` to `{options.per_file_ignores}`"
            # )
        else:
            # print(f"flake8-in-file-ignores - No match found")
            pass

    @staticmethod
    def get_files(options, excludes):
        # inspired from flake8 codebase
        return tuple(
            expand_paths(
                paths=options.filenames,
                stdin_display_name=options.stdin_display_name,
                filename_patterns=options.filename,
                exclude=excludes,
            )
        )

    def run(self):
        yield from []
