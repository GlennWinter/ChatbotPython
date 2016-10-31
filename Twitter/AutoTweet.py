import twitter, datetime, urllib2, sqlite3, datetime, time
#imports libraries

#uses sql to connect to chrome history
connect = sqlite3.connect("C:\Users\Glenn\AppData\Local\Google\Chrome\User Data\Default\History")
mouse = connect.cursor()

while True:

    #Gets the recent website titles visited on chrome from local storage
    mouse.execute("SELECT urls.title FROM urls")
    rows = mouse.fetchall()

    #Creates array to store the website titles
    history = []

    for row in rows:
        history.append(row)

    #Variables that store the last sites visited and prints site name and then terminates the SQL conenction
    lastSite = str(history[-1])
    site = lastSite[3:-3]
    print(site)
    connect.close

    #opens and reads text file
    file = open("twitterstuff.txt")
    creds = file.read().split('\n')

    #sets variable and format for twitter API 
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    #Gets current time
    timestamp = datetime.datetime.utcnow()

    #Posts a tweet with last site visited and timestamp
    response = api.PostUpdate("The last site I visited was: " + site + " at " + str(timestamp))

    print("The last site I visited was: " + site + "at "  + str(timestamp))

    #Makes twitter update every hour
    time.sleep(3600)
    

