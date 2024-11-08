from flet import *

def header(text):
    header_container = Container(
        content=Text(text, color="white", size=20, weight="bold"),
        alignment=alignment.center,
        bgcolor="black",
        padding=10
    )

    return header_container