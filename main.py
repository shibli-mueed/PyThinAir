# GUI libraries
import flet as ft
from flet.buttons import RoundedRectangleBorder
from flet.text import TextThemeStyle 

# System libraries
from os import path,mkdir
from time import sleep
import json

#dependencies
from  machine import fetch, convert_audio, convert_video

# Path
root = path.dirname(path.realpath(__file__)).replace('\\', '/')

def UI(page: ft.Page):
    page.title = "PyThinAir Pannel"
    page.padding = 50
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "always"
    
    selected_subreddit = ft.TextField(value="confession",  label="Subreddit", width=410)
    selected_time = ft.Dropdown(
        width=200, label="Time",value="week",
        options=[
            ft.dropdown.Option("all"),
            ft.dropdown.Option("hour"),
            ft.dropdown.Option("day"),
            ft.dropdown.Option("week"),
            ft.dropdown.Option("month"),
            ft.dropdown.Option("year"),          
        ],
    )
    limit = ft.TextField(value="2", width=200, label="Quantity",)
    
    progress = ft.Row(
        [
            ft.ProgressBar(width=410)
        ],
        # alignment=ft.MainAxisAlignment.CENTER
    )
    titles = ft.Text("Feched Titles",style=TextThemeStyle.TITLE_LARGE)
    items = []
    
    dick={}
    
    def main(e):
        dick = {
            "sub":selected_subreddit.value,
            "time":selected_time.value,
            "limit":limit.value
        }
        if len(items)!=0:
            for i in items:
                page.controls.remove(i)
        
        
        
        page.add(progress)
        
        keys,vals = fetch.scrap(dick,root)
        
        for i in keys:
            item = ft.Row(
                        [
                            ft.Column([ ft.Text(i)]),
                        ],
                        # alignment=ft.MainAxisAlignment.START
                    )
            page.add(item)
            items.append(item)
            page.update()
            
            
        # audio.convert_audio(keys, vals, root)
        # video.convert_video(keys,vals,root)
        
        convert_audio(keys, vals, root)
        convert_video(keys,vals,root)
        
        page.controls.remove(progress)
        # print(type(page.controls))
        page.update()
        
    # Initialize
    def initialize():
        if path.exists(f"{root}/machine/res/reddit.json") == False:
            print('''Error: Reddit Credentials are missing in diarectory!
                            /machine/res/reddit.json''')
            return False
        if path.exists(f"{root}/machine/res/res.json") == False:
            print('''Error: Resources File is missing in diarectory!
                            machine/res/res.json''')    
            return False
        if path.isdir(f"{root}/audio") == False:
            mkdir(f"{root}/audio")
        if path.isdir(f"{root}/video") == False:
            mkdir(f"{root}/video")
            
        if path.exists(f"{root}/database.json") == False:
            json.dump({},open("database.json",'w'))
        
        return True

    initialize()
    
    page.add(
        ft.Row([ft.Text(
            "ʕっ•ᴥ•ʔっ",
            style=TextThemeStyle.TITLE_LARGE
            )
                ]),
        ft.Row(
            [
                # ft.Text("SubReddit"),
                selected_subreddit
                
            ],
            # alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                selected_time,
                limit
            ],
            # alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.FloatingActionButton(text="Do this shit now!",
                                  width=410,
                                  on_click=main,
                                  shape=ft.RoundedRectangleBorder(radius=5),
                                  ),
            ],
            # alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            titles
        ]
        )
    )
    
    
    
ft.app(target=UI,view=ft.WEB_BROWSER)
