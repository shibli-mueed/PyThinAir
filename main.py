#selecting the enviroment
import sys
x = ['',
     'dirtyenv',
     'dirtyenv\\lib\\site-packages']

for a in x:
    sys.path.append(a)

#system libraries
from os import path,mkdir
from time import sleep
import json

#path
root = path.dirname(path.realpath(__file__)).replace('\\', '/')
    
#GUI libraries
import PySimpleGUI as sg





#Theme and layout
sg.theme('Black')
sg.set_options(font='Calibri 13',input_elements_background_color="#000")
layout = [
    [sg.Push(),sg.Text('ʕっ•ᴥ•ʔっ')],
    [sg.Text("Subreddit "),sg.Input(key='sub',
                                    default_text='confession',
                                    border_width=0)],
    
    [sg.Text("Time "),sg.Combo(['week','month','day','all','year','hour'],
                              key='time',
                              expand_x=True,
                              default_value='week'
                              )],
    
    [sg.Text("Max Quantity "),sg.Input(key='limit',
                                       expand_x=True,
                                       border_width=0,
                                       default_text=7)],
    
    [sg.Button("Do this shit now!",key='submit',expand_x=True)],
    [sg.Output(size=(60,10),echo_stdout_stderr=True)]
]

window = sg.Window("PyThinAir Pannel",
                   layout,
                   no_titlebar=False)

#initialize
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




#main function
def main():
    
    #dependencies
    import machine.fetcher as fetch
    import machine.audio as audio
    import machine.video as video
    
    print("Status: Fetching...")
    #sleep(0.5)
    
    keys,vals = fetch.scrap(value,root)
    
    
    print("\nStatus: Fetched!")
    #sleep(0.5)
    

    print("\nStatus: Converting Audio...")
    #sleep(0.5)
    audio.convert_audio(keys, vals, root)
    
    
    print("\nStatus: Audio Converted")
    #sleep(0.5)
    
    print("\nStatus: Converting Video...")
    video.convert_video(keys,vals,root)
    
    print("\nStatus: Video Converted")






while True:
    event, value = window.read()
    if initialize():
        if event == 'submit':
            if value['sub'] == "":
                print("Subreddit not mentioned!")
                continue
                
            if value['time'] == "":
                print("Time not mentioned!")
                continue
                
            if value['limit'] == "":
                print("Quantity not mentioned!")
                continue
            main()  
    
    if event ==sg.WIN_CLOSED:
        break
    
 
window.close()   

