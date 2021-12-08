import pynvim
import sys
import os; sys.path.append(os.path.dirname(__file__))
from balanced_brackets.brackets import Brackets

@pynvim.plugin
class BalancedBrackets():
    def __init__(self, nvim):
        self.nvim = nvim
        self.brackets = Brackets()
        #self.nvim.command("inoremap { {<CR>}<ESC>ko")

    @pynvim.function("HighlightImbalancedBrackets")
    def highlight_imbalanced_brackets(self, args):
        current_buffer = ''.join(self.nvim.current.buffer)
        if self.brackets.are_brackets_balanced(current_buffer):
            return
        highlight_coords = self.brackets.find_coords(self.nvim.current.buffer)
        for x, y in highlight_coords:
            self.nvim.current.buffer.add_highlight("Error", y, x, x+1)
