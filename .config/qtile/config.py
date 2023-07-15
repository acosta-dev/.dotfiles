import os
import subprocess
from libqtile import bar, layout, widget,hook,qtile
from libqtile.config import Click, Drag, Group, DropDown, ScratchPad, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from enum import Enum


# Cattppucin Color Palette
colors = {"base" : "#1e1e2e",
           "mantle" : "#181825",
           "crust" : "#11111b",
           "text" : "#cdd6f4",
           "subtext0" : "#a6adc8",
           "subtext1" : "#bac2de",
           "surface0" : "#313244",
           "surface1" : "#45475a",
           "surface2" : "#585b70",
           "overlay0" : "#6c7086",
           "overlay1" : "#7f849c",
           "overlay2" : "#9399b2",
           "blue" : "#89b4fa",
           "lavender" : "#b4befe",
           "sapphire" : "#74c7ec",
           "sky" : "#89dceb",
           "teal" : "#94e2d5",
           "green" : "#a6e3a1",
           "yellow" : "#f9e2af",
           "peach" : "#fab387",
           "maroon" : "#eba0ac",
           "red" : "#f38ba8",
           "mauve" : "#cba6f7",
           "pink" : "#f5c2e7",
           "flamingo" : "#f2cdcd",
           "rosewater" : "#f5e0dc",
           "white" : "#ffffff",
           "transparent" : "#FF00000"}

mod = "mod4"
terminal = guess_terminal()

## Sticky Windows
def float_to_front(qtile):
    for window in qtile.currentGroup.windows:
        if window.floating:
            window.cmd_bring_to_front()

win_list = []
def stick_win(qtile):
    global win_list
    win_list.append(qtile.current_window)
def unstick_win(qtile):
    global win_list
    if qtile.current_window in win_list:
        win_list.remove(qtile.current_window)
@hook.subscribe.setgroup
def move_win():
    for w in win_list:
        w.togroup(qtile.current_group.name)

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

class GroupLayout(Enum):
    MONADTALL = "monadtall"
    MONADWIDE = "monadwide"
    BSP = "bsp"
    MAX = "max"
    MATRIX = "matrix"
    FLOATING = "floating"
    RATIO_TILE = "ratiotile"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run")),
    Key([mod], "space", lazy.spawn("rofi -show drun")),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "f3", lazy.spawn("fsearch")),
    Key([mod], "z", lazy.function(stick_win), desc="make window sticky"),
    Key([mod, "shift"], "z", lazy.function(unstick_win), desc="unstick window"),
    Key([mod], "s", lazy.window.toggle_floating()),
]


groups = [
    ScratchPad(
        name ="scratchpad",
        dropdowns = [
            DropDown(
                name = "term", 
                x = 0.1,
                y = 0.0,
				height = 0.4650,
                cmd = "alacritty",
                opacity = 1.0
            ),
            DropDown(
                name = "telegram", 
                x = 0.2,
                y = 0.15,
                width = 0.5,
                height = 0.70,
                cmd = "telegram-desktop",
                opacity = 1.0
            )
        ]
    ),
    Group(
        name = "1",
        label = "",
        layout = "monadtall",
    ),
    Group(
        name = "2",
        label = "󰇩",
        layout = "monadwide",
    ),
    Group(
        name = "3",
        label = "󰨞",
        layout = "monadtall",
    ),
    Group(
        name = "4",
        label = "",
        layout = "monadtall",
    ),
    Group(
        name = "5",
        label = "󰭻",
        layout = "monadtall",
    ),
    Group(
        name = "6",
        label = "",
        layout = "monadtall",
    ),
    Group(
        name = "7",
        label = "",
        layout = "monadtall",
    ),
    Group(
        name = "8",
        label = "",
        layout = "monadtall",
    ),
    Group(
        name = "9",
        label = "",
        layout = "monadtall",
    ),
    Group(
        name = "0",
        label = "",
        layout = "monadtall",
    )
]

for i in groups[1:]:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
        Key([], 'F11', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('telegram')),
    ])

def init_layout_theme():
    return {"margin":10,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=12,
    padding=3,
    foreground="#cdd6f4",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                
                widget.GroupBox(font="IosevkaNerdFontMono",
                                fontsize = 24,
                                highlight_method = "line",
                                highlight_color=['1e1e2e', '1e1e2e']),
                widget.Prompt(),
                widget.WindowName(format=" {name}", max_chars=30, foreground=colors['green'], fmt = '<b>{}</b>'),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Mpd2(status_format='{play_status} {artist}/{title}'),
                widget.TextBox("", fontsize = 80, foreground=colors['peach'],padding=-16),
                widget.CPU(format=" {load_percent}% ", fmt = '<b>{}</b>', background=colors['peach'], foreground="#050000"),
                widget.TextBox("", fontsize = 80, foreground=colors['mauve'],background=colors['peach'],padding=-16),
                widget.Memory(format=' {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} ', measure_mem='G',fmt = '<b>{}</b>',background=colors['mauve'], foreground="#050000"),
                widget.TextBox("", fontsize = 80, foreground=colors['blue'],background=colors['mauve'],padding=-16),
                widget.PulseVolume(fmt = '<b>  {} </b>', foreground=colors['base'],background=colors['blue']),
                widget.TextBox("", fontsize = 80, foreground=colors['green'],background=colors['blue'],padding=-16),
                widget.Clock(format="󰸗 %Y-%m-%d %a 󰥔 %I:%M %p ", fmt = '<b>{}</b>', background=colors['green'],foreground=colors['surface0']),
                widget.TextBox("", fontsize = 80, foreground=colors['base'],background=colors['green'],padding=-16),
                widget.CheckUpdates(distro="Arch", no_update_string='  ', display_format="󰇚{updates}" ,fmt = '<b>{}</b>',foreground='1e1e2e',background=colors['base'], colour_no_updates=colors['green'], colour_have_updates=colors['red']),
                #widget.Net(interface='enp1s0', format='󰜮 {down}'),
                widget.Systray(),
                widget.CurrentLayoutIcon(scale=0.6),
                #widget.QuickExit(),
            ],
            24,
            background=colors['base'],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart" # or focus
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])



floating_types = ["notification", "toolbar", "splash", "dialog"]

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='Pidgin'),
    Match(wm_class='Nm-connection-editor'),
    Match(wm_class='Psi+'),
    Match(wm_class='qimgv'),
    Match(wm_class='Fsearch'),
    Match(wm_class='Ferdium'),
    Match(wm_class='TelegramDesktop'),
    Match(wm_class='Xdm-app'),
    Match(wm_class='File-roller'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Galculator'),
],  fullscreen_border_width = 0, border_width = 0)



