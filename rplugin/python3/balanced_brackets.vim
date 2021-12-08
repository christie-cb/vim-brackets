"fun! s:TypeAutoBracketPlugin()
"
"   let s:chars_typed = 0
"   imap <silent> <expr> <Plug>(AutoBracketCommand) <SID>AutoBracketCommand()
"  "inoremap { {<CR>}<ESC>ko
"  "inoremap ( (<CR>)<ESC>ko
   "inoremap [ [<CR>]<ESC>ko
"endfun
"if g:completed_typing | call s:TypeAutoBracketPlugin() | endif
inoremap { {<CR>}<ESC>ko
inoremap ( (<CR>)<ESC>ko
inoremap [ [<CR>]<ESC>ko

