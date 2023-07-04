#!/bin/bash
killall polybar;polybar main &
xsetroot -cursor_name left_ptr &
picom &
killall && polybar example &
nitrogen --restore
nm-applet &
$HOME/Apps/Telegram/Telegram -startintray -- %u &
flameshot &
pidgin &