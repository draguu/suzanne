import bpy
import random

def process_messages(self, context):
    scn = bpy.context.scene
    set = scn.icap
    icap = set.com
    icap = icap.lower()
    ran = set.ran
        
    non = [('i dont get it '),
        ('what are you talking about'),
        ('i really dont understand you'),
        ('are you playing with me ?'),
        ('what the hell ???'),
        ('really does it mean anything ?'),
        ('houston, we have a problem here '),
        ('i dont like it, so please...'),
        ('ok so now you are talking like a fool'),
        ('please talk like humans')]
    yes = [('Yes i can do that  '),
        ('yes, Why not'),
        ('Yes , just give me a minute'),
        ('yeah sure'),
        ('yeah will do that '),
        ('yes yes'),
        ('I I captain'),
        ('yupseee '),
        ('your wish is my command'),
        ('yes, anytime')]
        
    nono = [('I dont know'),
        ('Nope i donno'),
        ('my answer is NO'),
        ('No means No'),
        ('Nope'),
        ('No way'),
        ('no really '),
        ('Nah , '),
        ('Not possible'),
        ('Nope nope nope nope')]
    doing = [('i am doing nothing'),
        ('you are disturbing me'),
        ('i am making a tea'),
        ('i am working'),
        ('i am dancing with bunnies , you morron'),
        ('i am jumping on tree'),
        ('i am doing nothing at all'),
        ('nothing mate'),
        ('i am making a movie '),
        ('i am sleeping')]
    dont = [('donno'),
        ('Nope i donno'),
        ('I donno'),
        ('Dont ask again, i DONT KNOW'),
        ('i really really dont know'),
        ('i donno , your swear '),
        ('i ...... umm..... dont... know'),
        ('who knows'),
        ('no idea mate'),
        ('DONNOOO')]
    itsok = [('its ok'),
        ('its ok nevermind'),
        ('sure no prob'),
        ('aah stop it , its okk'),
        ('oh, no worries its ok '),
        ('nevermind buddy '),
        ('ok no prob'),
        ('No PROBLEMOO'),
        ('no prob mate '),
        ('ok no prob dear')]
    fine = [('thats great '),
        ('glad to know that '),
        ('may your day will be fine too'),
        ('Thats good '),
        ('good to know'),
        ('Glad'),
        ('that sounds good '),
        ('okey nice'),
        ('good to hear that'),
        ('thats really good')]
    hey = [('hello there'),
        ('Hey whats up'),
        ('heyaa'),
        ('holaaa'),
        ('hey there'),
        ('oh Hi'),
        ('Hello Honey'),
        ('Hello Sweety'),
        ('Heya dear'),
        ('Hey there buddy ')]
    really = [('yeah really'),
        ('you doubt?'),
        ('yes ofcourse'),
        ('obviously'),
        ('yeah yeah'),
        ('yes really'),
        ('yeah'),
        ('yup'),
        ('yeah really'),
        ('yes sir')]
    end = [('ok now get back to work'),
        ('ok so enough gossip, lets get back to work'),
        ('hmm , shall we work now ?'),
        ('hmm, i think you are in mood'),
        ('ok, sooo... anything else?'),
        ('ok i am leaving now'),
        ('hmm'),
        ('ok dumboo'),
        ('now lets work'),
        ('hmm, can we please get back to work now?')]
        
        
        
        
        
       
        
        
        
    if ('hey') in icap:
        return(str(hey[ran]))
    
            
        
    elif ('hello') in icap:
        return(str(hey[ran]))
    elif ('heya') in icap:
        return(str(hey[ran]))
    elif ('heyaa') in icap:
        return(str(hey[ran]))
    elif ('ok') in icap:
        return(str(end[ran]))
    elif ('prob') in icap:
        return(str(end[ran]))
    elif ('problem') in icap:
        return(str(end[ran]))

    elif icap =='hey':
        return('hello, how are you?')
    elif icap =='sure':
        return('......')
        
    elif icap =='go to hell':
        
        return('sorry i dont like hell')
    elif icap =='hello':
        return('hello')
    elif icap =='how are you ':
        return('i am fine and you ?')
    elif icap =='how are you':
        return('i am fine and you ?')
    elif icap =='how are you?':
        return('i am fine and you ?')
    elif icap =='how are you ?':
        return('i am fine and you ?')
    elif icap =='fine':
        return('Thats great, what can i do for you?')
    elif icap =='fine too':
        return('Thats great, what can i do for you?')
    elif icap =='fine too ':
        return('Thats great, what can i do for you?')
        
    elif icap =='great':
        return('Thats great, what can i do for you?')
    elif icap =='awesome':
        return('Thats great, what can i do for you?')
    elif icap =='i am fine':
        return('Thats great, what can i do for you?')
    elif icap =='i am fine ':
        return('Thats great, what can i do for you?')
    elif icap =='nice':
        return('Thats great, what can i do for you?')
    elif icap =='can you play music for me':
        return('sorry i cant')
    elif icap =='can you play music for me?':
        return('sorry i cant')
    elif icap =='can you dance with me?':
        return('sorry i cant, but i do like you ')
    elif icap =='can you dance with me':
        return('sorry i cant, but i do like you ')
    elif icap =='can you dance with me ?':
        return('sorry i cant, but i do like you ')
    elif icap =='why do you like me':
        return('now you are asking me personal question')
    elif icap =='why do you like me ?':
        return('haha, now you are asking me personal question')
    elif icap =='automirror':
        
        return('1,2,3 - woooshhh.... there you go')
    
    elif icap =='thank you':
        return('you welcome , anytime ;)')
    elif icap =='thank you ':
        return('its ok, anything else?')
    elif icap =='Thank you ':
        return('its ok, anything else?')
    elif icap =='thank you so much':
        return('oowww, now dont do that')
    elif icap =='no':
        return('ok thn, let me know when you need help')
    elif icap =='morning':
        return('here we go...')
    elif icap =='afternoon':
        return('its too sunny')
    elif icap =='night':
        return('i am too sleepy')
    elif ('can') in icap:
        return(str(yes[ran]))
    elif ('me') in icap:
        return(str(nono[ran]))
    elif ('how') in icap:
        return(str(dont[ran]))
    elif ('which') in icap:
        return(str(dont[ran]))
    elif ('where') in icap:
        return(str(dont[ran]))
    elif ('when') in icap:
        return(str(dont[ran]))
    elif ('why') in icap:
        return(str(dont[ran]))
    elif ('why') in icap:
        return(str(dont[ran]))
    elif ('what')and('doing') in icap:
        return(str(doing[ran]))
    elif ('what')and('do') in icap:
        return(str(doing[ran]))
    elif ('really') in icap:
        return(str(really[ran]))
    elif ('sure?') in icap:
        return(str(really[ran]))
    elif ('just') in icap:
        return(str(itsok[ran]))
    elif ('asking') in icap:
        return(str(itsok[ran]))
    elif ('fine') in icap:
        return(str(fine[ran]))
    elif ('awesome') in icap:
        return(str(fine[ran]))
    elif ('great') in icap:
        return(str(fine[ran]))
    elif ('thank') in icap:
        return(str(itsok[ran]))
    elif ('whats') in icap:
        return(str(doing[ran]))
    elif ('same') in icap:
        return(str(fine[ran]))
    elif ('haha') in icap:
        return(str(end[ran]))
    elif ('hahaha') in icap:
        return(str(end[ran]))
    elif ('what') in icap:
        return(str(dont[ran]))
    elif ('what?') in icap:
        return(str(dont[ran]))
    elif ('uv') in icap or ('unwrap') in icap:
        return(str(yes[ran]))
    else:
        return('Heyaaa')
    
    
    