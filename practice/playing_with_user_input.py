from flet import *

def main(page:Page):
    page.window_width = 400
    page.window_height = 300
    page.theme_mode = 'light'
    page.vertical_alignment = MainAxisAlignment.CENTER

    def increament(e:ControlEvent):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    def decrement(e:ControlEvent):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    txt_number:TextField = TextField(value="0", width=100, text_align='right')

    page.add(
        Row(
            controls=[
                IconButton(icon=icons.EXPOSURE_PLUS_1, on_click=increament),
                txt_number,
                IconButton(icon=icons.EXPOSURE_MINUS_1, on_click=decrement)
            ],
            alignment=MainAxisAlignment.CENTER
        ),
    )

# page.clean() -> Cleans everything on screen
"""
if not condition:
    # means if there is no value
"""


app(main)