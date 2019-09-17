#!/bin/bash

mkdir ~/.vim/bundle
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
mkdir ~/.vim/colors
curl -O https://raw.githubusercontent.com/nanotech/jellybeans.vim/master/colors/jellybeans.vim ~/.vim/colors

sudo apt-get update

if [ -z $(command -v ctags) ]; then
  sudo apt-get install ctags
fi;

if [ -z $(command -v ag) ]; then
  sudo apt-get install silversearcher-ag
fi;
