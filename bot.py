from generate_flag import generateFlag
from random import randint
import twitter
import time

class Bot:
    def __init__(self):
        self.x = 0
        self.genders = open('dict.txt').readlines()
        # create tweepy client
        self.client = twitter.Api(
            consumer_key="diPtk7uOULeQyyFCzXY6oolW6",
            consumer_secret="BSSKkZZEmW0R2FYJa1KJZ9P1s9s6rmyz7GwDCsmrPEtHLHPvKx",
            access_token_key="1383137744163983361-3vAcjxhPz8gPSXH2KcnmceRcX9Sgnn",
            access_token_secret="h7LCooxND9AQELex2E74jl7gEiJ8SbQpbwH8IoNFKJScS"
        )

    def runFlag(self):
        print("Beep boop... Generating flag!")
        g = generateFlag(randint(3,5))
        g.run()
        gender = self.genders[randint(0,len(self.genders)-1)].replace("\n", "")
        self.client.PostUpdate(f"Beep Boop! I have created a new gender for people who identify as {gender}!", media=open('flag.png', 'rb'))
        self.genders.remove(gender)
        with open("dict.txt", "w+") as f:
            f.write('\n'.join(self.genders))
        print("Flag created and colors/dict word removed!")

while True:
    B = Bot()
    B.runFlag()
    time.sleep(15*60) # Sleep for 15 minutes before making another post