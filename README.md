# vim-brackets

A Neovim plugin to highlight imbalanced brackets.

## Install

Update Python in your init.vim (usually found here: `~/.config/nvim/init.vim`)

```vim
let g:python3_host_prog = '/usr/bin/python3'
let g:python_host_prog = '/usr/bin/python2'
```

Use your preferred plugin manager, this is how it's done with [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'christie-cb/vim-brackets'
```

Run:

```vim
:PlugInstall
:UpdateRemotePlugins
```

## Use

```
:call HighlightImbalancedBrackets()
```
