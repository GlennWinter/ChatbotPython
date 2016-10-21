import random
import wikipedia
import json


stopWords = open("stopwords.txt", "r+")
happyWords = open("happyWords.txt", "r+")
sadWords = open("sadWords.txt", "r+")
#print stopWords
#happyWords.write("good")
#happyWords.close()
#pr


welcomePhrases = ("Hey", "Yo", "Hello", "Hi", "Welcome", "Bonjour")
 


def findKeyword(words):
    for word in words:
        if word.lower() not in stopWords: return word
    
    
while True: 
      
    print("Anyone there?")
    response = raw_input("> ")


    print(random.choice(welcomePhrases))
    response = raw_input("> ")
    
    name = raw_input("What is your name?\n > ")
    print("Hello " + name)
    
    age = input("How old are you?\n >")
    year = 2016 - age
    print("Ah so you were born in " + str(year))
    
    if (year == 1996):
        print("Sophie Turner was also born that year")

    
    response = raw_input("> ")
    if (response == "What she order?"):
        print("Fish Fillet")
        

    research = raw_input("Is there anything you would like to learn about?")
    print "Did you mean " + research + "," + wikipedia.summary(research, sentences=2)
