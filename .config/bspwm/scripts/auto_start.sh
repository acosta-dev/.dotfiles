#!/bin/bash
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
setxkbmap -model pc104 -layout es,us -option grp:alt_shift_toggle &
killall polybar;polybar main &
xsetroot -cursor_name left_ptr &
picom &
nitrogen --restore
nm-applet &
$HOME/Apps/Telegram/Telegram -startintray -- %u &

pgrep -x pidgin >/dev/null || pidgin &
pgrep -x flameshot >/dev/null || flameshot &