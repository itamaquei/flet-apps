import flet as ft

def main(page: ft.Page):
    page.window_width = 500
    page.window_height = 400
    page.theme_mode = 'light'

    def increament(e:ft.ControlEvent):
        left_text_number.value = int(left_text_number.value) + 5
        page.update()

    def decreament(e:ft.ControlEvent):
        right_text_number.value = int(right_text_number.value) - 5
        page.update()

    
    left_text_number:ft.TextField = ft.TextField(value="0", width=70) #increamnet by 5
    right_text_number:ft.TextField = ft.TextField(value="100", width=70) #decreamnet by 5

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.TEXT_INCREASE, on_click=increament),
                left_text_number,
                right_text_number,
                ft.IconButton(icon=ft.icons.TEXT_DECREASE, on_click=decreament),
            ],
            spacing=20,
        )
    )


ft.app(target=main)