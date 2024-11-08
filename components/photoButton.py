from flet import *

def photoButton(page, selected_file ,iconColor, text):
     # Function to handle file selection
    def on_file_selected(e):
        if file_picker.result != None:
            selected_file[0] = file_picker.result.files[0].name

    # Create FilePicker
    file_picker = FilePicker(on_result=on_file_selected)

    # Add the file picker to the page
    page.overlay.append(file_picker)

    # Function to trigger file picker on button click
    def on_photo_click(e):
        file_picker.pick_files(allow_multiple=False)

    photo = TextButton(
                text=text, 
                icon="photo", 
                icon_color=iconColor,
                style=ButtonStyle(colors.BLACK),
                 on_click=on_photo_click
                )

    return photo