from unittest.mock import MagicMock
from brackets import Brackets
# python3 -m pytest -v tests/test_brackets.py

def test_where_brackets_imbalanced():
    """
    Want to test that we'll get the index of any parentheses
    missing either a matching open or a matching close
    """
    line = "{{{]"
    brackets = Brackets()
    output = brackets.where_brackets_imbalanced(line)
    assert output == [0, 1, 2, 3]

    balanced_line = "{}[]()"
    balanced_output = brackets.where_brackets_imbalanced(balanced_line)
    assert balanced_output == []

    nearly_balanced_line = "{{[(])]}}"
    nearly_balanced_output = brackets.where_brackets_imbalanced(nearly_balanced_line)
    assert nearly_balanced_output == [4]

    code = "{(() =>  cool_function('some stuff');}, 3000)}"
    code_output = brackets.where_brackets_imbalanced(code)
    assert code_output == [len(code)-9]


def test_find_coords():
    brackets = Brackets()
    brackets.where_brackets_imbalanced = MagicMock()
    brackets.where_brackets_imbalanced.return_value = [0, 1, 9]
    buf = [
            "][",
            "(){}{",
            "}[",
    ]
    output = brackets.find_coords(buf)
    assert output == [(0,0), (1,0), (2,2)]
    brackets.where_brackets_imbalanced.return_value = [1, 5, 9]
    output = brackets.find_coords(buf)
    assert output == [(1,0), (3,1), (2,2)]
