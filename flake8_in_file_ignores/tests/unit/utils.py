import ast


def get_tree_from_str(pycode, filename="test_dummy_file.py"):
    return compile(pycode, filename, "exec", ast.PyCF_ONLY_AST, True)
