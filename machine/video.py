from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip
from moviepy.editor import CompositeAudioClip

import random
import json

with open("machine/res/res.json",'r') as file:
    asset = json.load(file)

def temp_title(x):
    li1 = x.split(' ')
    return ' '.join(li1[0:10])

def bg_choose():
    bgimg = random.choice(asset["images"])
    bgm = random.choice(asset["sounds"])
    return bgimg,bgm

def convert_video(keys,vals,path):
    i=0
    while i != len(keys):
        try:
            bg_audio = AudioFileClip(f'machine/res/{bg_choose()[1]}.mp3')
            main_audio = AudioFileClip(f"{path}/audio/{temp_title(keys[i])}.mp3")
            clip = VideoFileClip(f"machine/res/{bg_choose()[0]}.png") 

            compo = CompositeAudioClip([main_audio.volumex(1.2),
                                        bg_audio.volumex(0.17)
                                        ])  
            clip = clip.set_audio(compo)
            clip = clip.set_duration(main_audio.duration).resize((720,720) )

            clip.write_videofile(f"{path}/video/{temp_title(keys[i])}.mp4",fps=15)

        except Exception as e:
            #print('ERROR!!!')
            #Beep(frequency, duration)
            #Beep(frequency, duration)
            print(e)
            del keys[i]
            del vals[i]
        finally:
            i+=1