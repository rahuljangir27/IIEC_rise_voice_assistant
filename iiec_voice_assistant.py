import pyttsx3
import os
pyttsx3.speak("welcome to apps launchboard\n\n")

while True:
	

	print("What you want to do  : ",end="")
	p=input()

		
	if ("who" in p) and ("you" in p) :
	    pyttsx3.speak("I am an voice assistant who can any task for you")
	    print("I can start chrome \n I can start notepad \n I can start media player \n I can browse anything for you on youtube,google,wikipidea\n I can send a whatsapp message to anyone you want")	
	
	# run chrome
	elif (("run" in p) or ("start" in p) or ("launch" in p)) and (("chrome" in p) or ("web" in p) or ("browser" in p)):
	    os.system("chrome")
	    pyttsx3.speak("opening Chrome")

	#search on youtube
        # example :::: search iiec rise 2020 on youtube     or  browse iiec rise 2020 on youtube       
	elif (("search" in p) or ("browse" in p) ) and ("youtube" in p):
	    x=p[7:-11]
	    y=x.replace(' ','+')
	    os.system("chrome ""https://www.youtube.com/results?search_query="+y+"")
	    pyttsx3.speak("searching"+x+"on youtube")

	#search on google
	# example :::: search vaccine for covid-19 on google     or  browse iiec rise 2020 on google 
	elif (("search" in p) or ("browse" in p) ) and ("google" in p):
	    x=p[7:-10]
	    y=x.replace(' ','+')
	    os.system("chrome ""https://www.google.com/search?q="+y+"")
	    pyttsx3.speak("searching"+x+"on google")

	#search on wikipidea
	# example :::: search iiec rise 2020 on wikipidea    or  browse iiec rise 2020 on wikipidea 
	elif (("search" in p) or ("browse" in p) ) and ("wikipidea" in p):
	    x=p[7:-13]
	    y=x.replace(' ','+')
	    os.system("chrome ""https://en.wikipedia.org/wiki/Special:Search?search="+y+"")
	    pyttsx3.speak("searching"+x+"on wikipidea")

	#sending a text on whatsapp
	# example ::: whatsapp hi how are you to 94XXXXX987 
	elif ("whatsapp" in p) or ("to" in p):
	    x=p[9:-14]
	    z=x.replace(' ','+')
	    y="91"+p[-10:]
	    os.system("chrome ""wa.me/"+y+"/?text="+z+"")
 
	elif (("run in p") or ("start" in p ) or ("launch" in p)) and (("notepad" in p ) or ("editor" in p)) :
	    os.system("notepad")
	    pyttsx3.speak("opening notepad")

	elif (("run in p") or ("start" in p ) or ("launch" in p)) and (("vlc" in p ) or ("media" in p) or ("player" in p)) :
	    os.system("vlc")
	    pyttsx3.speak("opening vlc")

	
	elif (("run in p") or ("start" in p ) or ("launch" in p)) and (("cmd" in p ) or ("command prompt" in p) or ("terminal" in p)) :
	    os.system("cmd")
	    pyttsx3.speak("opening terminal")

	elif "exit" in p :
            pyttsx3.speak("Closing the launchboard")
            break

   
	    