# vim-brackets

A Neovim plugin to highlight imbalanced brackets.

![](https://media3.giphy.com/media/QiiKrC822ZjDHkt42y/giphy.gif?cid=790b7611c463a4ad91a8a74ee6f44fa7271914e12ac05b44&rid=giphy.gif&ct=g)

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

Imbalanced brackets will be highlighted upon exiting Insert mode.
