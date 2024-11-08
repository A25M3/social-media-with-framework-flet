from flet import *

def textField(fieldIcon, fieldLabel, P=False):
    t_field = TextField(label=fieldLabel, icon=fieldIcon, password=P, can_reveal_password=P)

    return t_field