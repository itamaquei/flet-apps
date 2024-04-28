from flet import *
from random import randint

"""
Topics:
    - Custom Fonts
    - Custom Asssets
    -- to use custom fonts pass the assest_dir into app(asset_dir="enter the location")
    -- the pass it as a dict page.font{"fontName": "font_dir"}

    - intro to Card and Container
    - Guess me Game (p1) -> part 1
"""

# which player guess the answer first is the winner

def main(page:Page):
    page.window_width = 750
    page.window_height = 500
    page.title = "Guess Me"
    page.padding = padding.only(top=20)

    answer = randint(1, 100)

    print(f"=> {answer}")

    def check_player1(e:ControlEvent):
       if int(player_1.value) < answer:
           result.controls.append(
               Text("Guess a higher values")
           )
           page.update()
           
       elif int(player_1.value) > answer:
           result.controls.append(
               Text("Guess a lower values")
           )
           page.update()
       elif int(player_1.value) == answer:
           result.controls.append(
               Text(f"Whoo You got the right answer")
           )
           page.update()
       else:
           result.controls.append(
               Text("Something went wrong")
           )
       page.update()


    def check_player2(e:ControlEvent):
       if int(player_2.value) < answer:
           result.controls.append(
               Text("Guess a higher values")
           )
           
       elif int(player_2.value) > answer:
           result.controls.append(
               Text("Guess a lower values")
           )
           
       elif int(player_2.value) == answer:
           result.controls.append(
               Text(f"Whoo You got the right answer")
           )
        
       else:
           result.controls.append(
               Text("Something went wrong")
           )
       page.update()


    player_1:TextField = TextField(
        hint_text="Guess a number (1-100)..",
        label='player 1',
        border_radius=10
    )
    player_2:TextField = TextField(
        hint_text="Guess a number (1-100)..",
        label='player2',
        border_radius=10
    )


    result:Column = Column()

    #control is where the widget goes

    player_1_btn:ElevatedButton = ElevatedButton(
        "Check your answer",
        on_click=check_player1
    )

    player_2_btn:ElevatedButton = ElevatedButton(
        "Check your answer",
        on_click=check_player2
    )

    page.add(
        Card(
            content=Container(
                    content=Row(
                        controls=[Text(value="Guess Me", size=30)],
                        alignment='center'
                ),
                padding=padding.only(bottom=20, top=10),
                
        ),
        color='lightblue'
        ),
        Column(
            controls=[
                Row(
                controls=[player_1, player_1_btn],
                alignment='center'
            ),
                Row(
                controls=[player_2, player_2_btn],
                alignment='center'
            ),
            ],
            spacing=20
        ),
        result #Column
    )

app(main)