#!/bin/bash
killall polybar;polybar main &
xsetroot -cursor_name left_ptr &
picom &
nitrogen --restore
nm-applet &
$HOME/Apps/Telegram/Telegram -startintray -- %u &
flameshot &
pidgin &