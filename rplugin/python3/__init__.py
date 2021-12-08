import pynvim
import sys
import os; sys.path.append(os.path.dirname(__file__))
from balanced_brackets.brackets import Brackets

@pynvim.plugin
class BalancedBrackets():
    def __init__(self, nvim):
        self.nvim = nvim
        self.brackets = Brackets()
        #self.nvim.feedkeys("inoremap { {<CR>}<ESC>ko")
        self.highlight_src = self.nvim.new_highlight_source()

    @pynvim.autocmd("InsertLeave")
    def highlight_imbalanced_brackets(self):
        self.nvim.current.buffer.clear_highlight(src_id=self.highlight_src)
        current_buffer = ''.join(self.nvim.current.buffer)
        if self.brackets.are_brackets_balanced(current_buffer):
            return
        highlight_coords = self.brackets.find_coords(self.nvim.current.buffer)
        for x, y in highlight_coords:
            self.nvim.current.buffer.add_highlight("Error", y, x, x+1, src_id=self.highlight_src)

    @pynvim.autocmd("InsertCharPre", eval='v:char', sync=True)
    def autocomplete_brackets(self, char):
        if char in self.brackets.brackets.keys():
            self.nvim.feedkeys(self.brackets.brackets[char], options="i")
