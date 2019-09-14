dotfiles
========

These are my dot files.

Put a symbolic link into `conf.avail` directory to enable a config with

```
$ ./install.py
```

If no file is found, a symbolic link is created.

## xinitrc

Mandatory packages

* app-admin/conky
* x11-apps/xsetroot
* x11-wm/dwm
* x11-terms/xterm

install `conky` without `X` support

## Xdefaults

* setup `xterm` colors
* setup default colours

# vimrc

* mkdir -p .vim/bundle
* git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/vundle
* mkdir .vim/colors
* https://raw.githubusercontent.com/nanotech/jellybeans.vaim/master/colors/jellybeans.vim



### Contact

Jan Frederik Hake, <jan_hake@gmx.de>. [@enter\_haken](https://twitter.com/enter_haken) on Twitter.
