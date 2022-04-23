import praw
import re
import random
import json
import uuid

with open('machine/res/reddit.json','r') as foo:
    cred = json.load(foo) 
    
with open("machine/res/res.json",'r') as file:
    asset = json.load(file)


#add to database
def add_in_database(keys,vals,path):
    with open(f"{path}/database.json",'r') as foo:
        data = json.load(foo)
    
    for i in range(len(keys)):
        temp={
            "id":str(uuid.uuid4()),
            "title":keys[i],
            "body":vals[i]
        }
        
        data[str(len(data)+1)]=temp
    with open(f"{path}/database.json",'w') as file:
        json.dump(data,file,indent=4)
        

#remove unwanted things from content and title
def remove_things(a):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    temp= emoji_pattern.sub(r'', a)
    
    li=temp.split()
    for i in li:
        if 'http' in i:
            li.remove(i)

    return ' '.join(li).replace('\\','-').replace('/', '-').replace('*',' ').replace('\"',' ')


def phrase_choose():
    intro = random.choice(asset["intro"])
    para1 = random.choice(asset["para1"])
    para2 = random.choice(asset["para2"])
    para3 = random.choice(asset["para3"])
    outro = random.choice(asset["outro"])
    
    
    return intro,para1,para2,para3,outro

def scrap(dictionary,path):
    keys=[]
    vals=[]
    while True:
        #try:
               
            
        param=int(dictionary['limit'])
        subr=dictionary['sub']
        time=dictionary['time']
        reddit = praw.Reddit(client_id=cred['client_id'],
                            client_secret=cred['client_secret'],
                            user_agent=cred['user_agent'])

        #print('\nFetching...')
        subms = reddit.subreddit(subr).top(time,limit=param)
        

        for i in subms:
            if not i.stickied:
                author= str(i.author).replace('_',' ')
                global title
                title= str(i.title)
                title = remove_things(title)

                content=i.selftext
                content = remove_things(content)

                phrase=f'''{phrase_choose()[0]} {phrase_choose()[1]} {phrase_choose()[2]} {phrase_choose()[3]},{title}, {content}. {phrase_choose()[4]}'''
                
                
                print(f'{" ".join(title.split()[:10])} DONE')

                keys.append(title)
                vals.append(phrase)

        add_in_database(keys,vals,path)
        
        break
            
        '''except Exception as e:
            #print('ERROR!!!')
            print('While Fetching'+'_'*20,e)'''
            
    return keys,vals
    
            
