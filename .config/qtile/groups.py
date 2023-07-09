from libqtile.config import Group, DropDown, ScratchPad

def Groups():
    def init_groups(self):
        return [
            ScratchPad(
                name ="scratchpad",
                dropdowns = [
                    DropDown(
                        name = "term", 
                        cmd = "alacritty",
                        opacity = 0.9
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
                label = "",
                layout = "monadtall",
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
