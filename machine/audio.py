from gtts import gTTS

#shorten the title to save the files
def temp_title(x):
    li1 = x.split(' ')
    return ' '.join(li1[0:10])


def convert_audio(keys,vals,path):
    j=0
    while j != len(keys):
        try:
            #print("Converting Audio...")
            text_ts=gTTS(text=vals[j], lang='en', slow=False)
            text_ts.save(f"{path}/audio/{temp_title(keys[j])}.mp3")
            print(keys[j],' SAVED')
            j+=1
            
        except Exception as e:
            print(e)
            #Beep(frequency, duration)