import random
import wikipedia
import time

stopWords = open("stopwords.txt", "r+")
happyWords = open("happyWords.txt", "r+")
sadWords = open("sadWords.txt", "r+")
#print stopWords
#happyWords.write("good")
#happyWords.close()



welcomePhrases = ("Hey", "Yo", "Hello", "Hi", "Welcome", "Bonjour")
 


def findKeyword(words):
    for word in words:
        if word.lower() not in stopWords: return word
    
def wikiSearch():
    
    print "Did you mean " + research + ", " + wikipedia.summary(research, sentences=2) + "\n"
    
while True: 
      
    print("Anyone there?")
    response = raw_input("> ")


    print(random.choice(welcomePhrases))
    response = raw_input("> ")
    
    name = raw_input("What is your name?\n > ")
    
    splitWords = name.split(" ")
    keyWord = findKeyword(splitWords)
    print(random.choice(welcomePhrases) + " " + keyWord)
    time.sleep(1)
    print("I am a chatbot called...")
    time.sleep(2)
    print("Chatbot")
    time.sleep(1)   
    age = input("How old are you " + name + "?\n >")
    year = 2016 - age
    time.sleep(1)
    print("Ah so you were born in " + str(year))
    time.sleep(1)
    
    if (year == 1996):
        print("Sophie Turner was also born that year")
    elif (year == 1995):
        print("RJ Cycler was also born that year")
    elif (year == 1997):
        print("Chloe Grace Moretz was also born that year")
    elif (year >= 1998):
        print("You're young, go back to school!")
    elif (year <= 1994):
        print("You oldy! Go back to the carehome")
    
    time.sleep(2)
    print("Is there anything you would like to learn about? ")
    research = raw_input()
    print(" ")      
    wikiSearch() 
    
    while True: 
        userInput = raw_input("Is there anything else you would like to learn about?\n >")
           
            
        if (userInput == "yes"):
            print("Please enter what you want to search\n >")
            research = raw_input()
            wikiSearch()
        elif(userInput == "no"):
            break 
        
        else:
            print("Please answer with yes or no  >")
            
        
    favColour = raw_input("Okay then, what is your favourite colour?\n >")
    
    if (favColour == "red"):
        print("Ahh the colour of love, shame I don't have feelings")
    
    elif (favColour == "green"):
        print("That's my favourite colour too!")
    
    elif(favColour == "blue"):
        print("That blue my mind, *robotic laughter*")
        
    elif(favColour == "orange"):
        print("Also a tasty fruit, good choice!")

    elif(favColour == "yellow"):
        print("Poor choice!")

    elif(favColour == "indigo"):
        print("A weird choice of colour!")

    elif(favColour == "violet"):
        print("Not a bad choice!")
    else:
        print("I haven't heard of that colour!")

    time.sleep(2)

    
        
        
        
