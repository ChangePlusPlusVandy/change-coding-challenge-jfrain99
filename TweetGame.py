import tweepy
import time
from datetime import date
import random

tweet_count = 3200
consumer_key = 'GeMr51br8Cgb3VFiKJLdaFqvV'
consumer_secret = 'EPDtMLZfEoCXbfycIDcXogbAeu1aioaQf93RkWq9xuPKTVUTI3'
access_token_key = '1309237095450341378-VJM2YSBxDKeQ6jIA1k3YXInIXJms2d'
access_token_secret_key = 'M76TBetB6tl2Yksv7H7GpWhDNEpJYEephzwwPglCgBHHV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret_key)

api = tweepy.API(auth)


def checkguess(username1, username2):
    print("Who do you think tweeted this?")
    print("Was it 1: @" + username1 + " or 2: @" + username2 + "?")
    return input("It was: ")


def checktyped():
    return input("Enter selection: ")


def checkusername():
    return input("Enter username: ")


def gettweets(username):

    user = "%" + username
    usertweets = tweepy.Cursor(api.search, q=user, max_ids=username, include_rts=False, id=username, since=date.today()).items(tweet_count)

    return [tweet.text for tweet in usertweets]


def defornew():
    print("Type 1 for default or 2 to input your own")
    choice = checktyped()
    if choice == "1":
        print("Default selected.")
        userid1 = "kanyewest"
        userid2 = "elonmusk"
        user1tweets = gettweets(userid1)
        user2tweets = gettweets(userid2)

    elif choice == "2":
        print("Input Twitter usernames now:")
        userid1 = checkusername()
        userid2 = checkusername()
        print("Option 1: @" + userid1)
        print("Option 2: @" + userid2)
        user1tweets = gettweets(userid1)
        user2tweets = gettweets(userid2)
    else:
        print("Invalid input. Please try again.")
        defornew()

    game(user1tweets, user2tweets, userid1, userid2)


def gamesetup():
    print("Welcome to my game! My name is Jack, and I'll be your host today.")
    time.sleep(.3)
    print("Today we're playing:")
    time.sleep(.15)
    print("NAME")
    time.sleep(.075)
    print("THAT")
    time.sleep(.075)
    print("TWEET!")
    time.sleep(.075)
    print("Would you like to use our default twitter users - Elon Musk and Kanye West - or input your own?")
    defornew()


def game(user1tweets, user2tweets, userid1, userid2):

    userchoice = random.randint(1, 2)
    rnd = random.randint(0, tweet_count - 1)
    if userchoice == 1:
        print(user1tweets[rnd])
    else:
        print(user2tweets[rnd])

    answer = checkguess(userid1, userid2)
    while answer.isalpha():
        print("Sorry! You must enter either a 1 or a 2")
        answer = checkguess(userid1, userid2)

    if int(answer) == userchoice:
        print("Correct! Nice one!")
    else:
        print("Wrong! Sorry bucko!")

    again = input("Would you like to play again? Type Y or N:")
    if again == 'Y' or again == 'y':
        game(user1tweets, user2tweets, userid1, userid2)
    else:
        print("Thanks for playing!")
        time.sleep(2)
        exit()


gamesetup()
