import random, wikipedia, time


stopWords = open("stopwords.txt", "r+")
stopwords = stopWords.read()
stopWords.close()

happyWords = open("happyWords.txt", "r+")
happywords = happyWords.read()
happyWords.close()

sadWords = open("sadWords.txt", "r+")
sadwords = sadWords.read()
sadWords.close()

welcomePhrases = ("Hey", "Yo", "Hello", "Hi", "Welcome", "Bonjour")
happyPhrases = ("That's good to hear!", "Sounds great!", "Glad you're good", "That's grand")
sadPhrases = ("That's not good!", "Hope you're okay!", "That sucks to hear!", "Sorry to hear that")
fairwellPhrases = ("Goodbye", "Cya", "Laters", "Catch you soon", "Bye!", "Fairwell")

def findKeyword(words):
    for word in words:
        if word.lower() not in stopwords: return word
        
def findHappy(happyWord):
    for word in happyWord:
        if word.lower() in happywords: 
            print(random.choice(happyPhrases))
        
def findSad(sadWord):
    for word in sadWord:
        if word.lower() in sadwords: 
            print(random.choice(sadPhrases))
    
def wikiSearch():
    
    print ("Did you mean " + research + ", " + wikipedia.summary(research, sentences=2) + "\n")
    
while True: 
      
    print("Anyone there?")
    response = raw_input(">")

    print(random.choice(welcomePhrases))
    response = raw_input(">")
    
    name = raw_input("What is your name?\n>")
    
    splitWords = name.split(" ")
    keyWord = findKeyword(splitWords)
    print(random.choice(welcomePhrases) + " " + keyWord)
    
    time.sleep(1)
    print("I am a chatbot called...")
    time.sleep(2)
    print("Chatbot")
    time.sleep(1)   
    
    feeling = raw_input("How are you feeling today " + keyWord + "?\n>")
    
    splitWords = feeling.split(" ")
    feelingResponse = [findHappy(splitWords), findSad(splitWords)]
    
    if (findHappy in feelingResponse is True):
            findHappy()
            
    elif (findSad in feelingResponse is True):
            findSad()
            
    else: 
        print("I do not understand that feeling")

    age = input("How old are you " + keyWord + "?\n>")
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
    time.sleep(1)
    research = raw_input("Please enter what you want to search \n>")
         
    wikiSearch() 
    
    while True:
        print("Is there anything else you would like to learn about?")
        userInput = raw_input()
           
            
        if (userInput == "yes"):
            print("Please enter what you want to search")
            research = raw_input(">")
            wikiSearch()
        elif(userInput == "no"):
            break 
        
        else:
            print("Please answer with yes or no")
            
        
    favColour = raw_input("Okay then, what is your favourite colour?\n>")
    
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
    
    print("Well it is time for me to go...")
    time.sleep(2)
    print("What I have learnt about you is, you're called " + keyWord)
    time.sleep(1)
    print("You're " + str(age) + " years old")
    time.sleep(1)
    print("You are feeling " + feeling)
    time.sleep(1)
    print("The last thing you searched was " + research)
    time.sleep(1)
    print("..And your favoruite colour is " + favColour)
    time.sleep(1)
    print("Nice to meet you " + keyWord)
    time.sleep(1)
    print(random.choice(fairwellPhrases))
    
        
        
        
