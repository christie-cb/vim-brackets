import typing
from typing import Optional, List, Tuple

class Brackets():
    def __init__(self):
        self.brackets = {
            "{": "}",
            "[": "]",
            "(": ")",
        }

    def are_brackets_balanced(self, string: str) -> bool:
        stack = []
        for item in string:
            if item in self.brackets.keys():
                stack.append(item)
            elif item in self.brackets.values():
                if len(stack) == 0:
                    return False
                opening = stack.pop(-1)
                if self.brackets[opening] != item:
                    return False
        return True
    """
    Given a string, return the indices of parentheses that don't have a matching
    closing bracket or don't have a matching opening bracket.
    """
    def where_brackets_imbalanced(self, line: str) -> List[int]:
        stack = [] # (i, bracket)
        imbalanced = []
        for i in range(len(line)):
            item = line[i]
            item_tuple = (i, item)
            if item in self.brackets.keys():
                stack.append(item_tuple)
            elif item in self.brackets.values():
                if len(stack) == 0:
                    imbalanced.append(item_tuple)
                    continue
                opening_tuple = stack.pop(-1)
                if self.brackets[opening_tuple[1]] != item:
                    imbalanced.append(opening_tuple)
                    imbalanced.append(item_tuple)
        if len(stack) != 0:
            imbalanced = stack + imbalanced
        return sorted([idx for idx, item in imbalanced])

    Buffer = List[str]
    def find_coords(self, buf: Buffer) -> List[Tuple[int, int]]:
        one_long_string = ''.join(buf)
        hl = self.where_brackets_imbalanced(one_long_string) #[0, 1, 10]
        num_rows = len(buf)
        output = [] # [(col, row)]
        cum_row_len = 0
        for i in range(num_rows):
            row_len = len(buf[i])
            if len(hl) == 0:
                return output
            while hl[0] <= row_len + cum_row_len:
                index = hl.pop(0)
                output.append((index - cum_row_len, i))
                if len(hl) == 0:
                    return output
            cum_row_len += row_len
            print(cum_row_len)
        return output
