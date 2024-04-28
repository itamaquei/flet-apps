from flet import *
import speedtest
from time import sleep

def main(page:Page):
    page.window_width = 850
    page.window_height = 550
    page.title = "Internet Speed Test"
    page.theme_mode = "dark"
   # page.padding = padding.only(top=30)
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = MainAxisAlignment.CENTER
    #page.window_bgcolor = "blue"
    #page.bgcolor='#000000'
    page.auto_scroll = True
    page.scroll = True
    page.padding = padding.only(top=50)
    st = speedtest.Speedtest()

    # find and connect to the best server in the region
    ideal_server = st.get_best_server()
    city = ideal_server['name']
    country = ideal_server["country"]
    cc = ideal_server['cc']
 
    def animate_getSpeedContainer(e:ControlEvent):
        getSpeedContainer.width = 400 
        getSpeedContainer.height = 700

        
        line_01.value = "> calculating download speed, please wait.."
        line_01.color = "white"
        getSpeedContainer.update()
        sleep(2)


        line_02.value = f"> finding the best possible servers in {city}, {country} ({cc})"
        getSpeedContainer.update()
        sleep(2)            
        
        line_03.value = "> connection established, staus OK, fetching download speed"
        download_speed = st.download()/1024/1024
        progress_bar.opacity = 1
        progress_row
        getSpeedContainer.update()
        progress_bar.value = 1
        sleep(2)

            
        line_04.value = f"> the download speed is {(round(download_speed,3))} Mbps"
        getSpeedContainer.update()
        sleep(2)

        line_05.value = "> calculating upload speed, please wait..."
        getSpeedContainer.update()
        sleep(2)

        line_06.value = "> executin upload script, hold on"
        getSpeedContainer.update()
        sleep(2)

        progress_bar_02.opacity = 1
        progress_row

        upload_speed = st.upload()/1024/1024

        line_07.value = f"> the upload speed is {round(upload_speed,3)} Mdps"
        progress_bar_02.value = 1
        getSpeedContainer.update()
        sleep(3)

        line_08.value = "> task completed successfully"
        line_08.size = 15
        getSpeedContainer.update()



    line_01:Text = Text(value="> press start...", color='green', size=20) 
    line_02:Text = Text(value="", color='green', size=20, weight='bold', font_family='ink free') 
    line_03:Text = Text(value="", color='green', size=20, weight='bold', font_family='ink free') 
    
    # after line 3
    progress_bar = ProgressBar(width=300, color='#0080ff', bgcolor='white', opacity=0)
    progress_text:Text = Text(value="  ")
    progress_row:Row = Row(controls=[progress_text, progress_bar])
    
    line_04:Text = Text(value="", color='yellow', size=20, weight='bold', font_family='ink free') 
    line_05:Text = Text(value="", color='green', size=20, weight='bold', font_family='ink free')
    line_06:Text = Text(value="", color='green', size=20, weight='bold', font_family='ink free')

    progress_bar_02 = ProgressBar(width=300, color='#0080ff', bgcolor='white', opacity=0)
    progress_text:Text = Text(value="  ")
    progress_row_02:Row = Row(controls=[progress_text, progress_bar_02]) 
    
    line_07:Text = Text(value="", color='yellow', size=20, weight='bold', font_family='ink free')
    line_08:Text = Text(value="", color='white', size=20, weight='bold', font_family='ink free') 
    line_09:Text = Text(value="", color='white', size=20,weight='bold', font_family='ink free')

    termal_text:Column = Column(
        controls=[
            line_01,
            line_02,
            line_03,
            progress_row,
            line_04,
            line_05,
            line_06,
            progress_row_02,
            line_07,
            line_08
        ]
    )


    appTitle:type[Container] = Container(
            content=Column(
                controls=[
                Row(
                    controls=[
                    Text(
                        "Internet",
                        size=40,
                        color='red',
                        weight='bold',
                    ),
                    Text(
                        value="Speed",
                        size=40,
                        color='yellow',
                        weight='bold',
                        font_family='ink free'
                    ),
                ],
                alignment='center'
            ),
            ],
            alignment=MainAxisAlignment.CENTER,
            ),
        )
    

    getSpeedContainer:type[Container] = Container(
        content=termal_text,
        width=200,
        height=100,
        bgcolor='#4d4d4d',
        border_radius=30,
        padding=padding.all(20),
        animate=animation.Animation(1000, 'BounceOut'),
        on_click=animate_getSpeedContainer
    )

    page.add(
        appTitle,
        Row(
            controls=[getSpeedContainer],
            alignment=MainAxisAlignment.CENTER
        ),
        Row(
            controls=[IconButton(
                icon=icons.PLAY_ARROW,
                icon_color='black',
                bgcolor='green',
                on_click=animate_getSpeedContainer
            )
        ],
            alignment='center'
        )
    )



app(target=main)