from flet import *
from time import sleep

def main(page: Page):
    page.theme_mode = 'light'
    page.title = "Greetings App"
    page.window_width = 500
    page.window_height = 700
    page.scroll = True
    page.auto_scroll = True

    def say_hello(e:ControlEvent) -> None:
       if not first_name.value:
           if last_name.value:
            greeting.controls.append(
            Text(f"Hello {last_name.value}", size=35, font_family='ink free')
        )
            last_name.value = ""
           else:
            greeting.controls.append(
            Text("Please Enter your name",size=35, font_family='ink free')
        )
            first_name.focus()
            page.update()
       
       else:
        greeting.controls.append(
            Text(f"Hello {first_name.value} {middle_name.value} {last_name.value}",size=35, font_family='ink free')
        )
        if last_name.value:
            last_name.value = ""
            first_name.value = ""
            first_name.focus()
        else:
           first_name.value = ""
           first_name.focus()

        page.update()

    def clear_screen(e:ControlEvent):
       greeting.clean()
       first_name.focus()
    

    greeting:type[Column] = Column()

    first_name:TextField = TextField(
        label="Enter first name", 
        bgcolor="transparent",
        autofocus=True
    )

    last_name:TextField = TextField(label="Enter last name")

    middle_name:TextField = TextField(label="Enter middle name")
    
    page.add(
        Column(
            controls=[
                first_name, # TextField
                middle_name, #TextField
                last_name, # TextField
                Row(
                controls=[
                    ElevatedButton(text="Say hello",on_click=say_hello),
                    ElevatedButton(text="Clear Screen",on_click=clear_screen)
                ]
                )
            ]
        ),
        greeting
    )   



app(main)
