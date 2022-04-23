# PyThinAir
## Preview
Create videos out of thin air, It automatically fetch internet stories and create videos out of it with awesome background music and voiceover.
View sample videos on [youtube](https://www.youtube.com/channel/UCAK3NCcUFDkqtKwjfoYn9jA) 

## PRAW
It uses praw, so you need to register your app on reddit in order to fetch the post.
Regiter your app [here](https://ssl.reddit.com/prefs/apps/)
After registering yourself paste the *client_id, client_secret* and *user_agent* in the *machine/res/reddit.json*

## Voiceover
The sequence of the voiceover is intro -> para1 -> para2 -> title of the post -> content of the post -> para3 -> outro.
You can edit the file *machine/res/res.json* and paste the phrases for Intro, Outro and Middle Paragraphs.

## How it works
* It fetch reddit post
* Randomly organise the phrases which have given in the *machine/res/res.json*
* Use google text to speach to convert an audio file
* Randomly select background images and background music given in *machine/res* folder and listed in *machine/res/res.json*
* Render a .mp4 file and save it into video folder in root directory

Major Libraries PRAW, gTTS, MoviePy, PySimpleGUI
