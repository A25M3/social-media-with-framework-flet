from flet import *

def costumButton(btnLabel,page,route,btnIcon,iconColor):
    costumButton = ElevatedButton(
        btnLabel,
        width=130,
        bgcolor="black",
        color="white",
        icon=btnIcon,
        icon_color=iconColor,
        on_click=lambda e: page.go(route)
        )

    return costumButton