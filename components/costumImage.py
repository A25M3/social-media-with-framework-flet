from flet import *

def costumeImage(source):

    costume_img = Image(
        src=source,
        width=300,
        height=300,
        fit= ImageFit.CONTAIN
    )

    return costume_img