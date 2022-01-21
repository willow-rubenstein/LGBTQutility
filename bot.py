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
            consumer_key="oXjq6AlzSmQW3QSFrSRKPFnzW",
            consumer_secret="jpODFpZmtODjfzYjWIe3ja8xQqRptLvKeRynYhqSA3jK0DR1XL",
            access_token_key="1484347838473465858-jtydBYiP2afKtS5FHxI0fIrHPZGN1C",
            access_token_secret="PNoctL9wDX1Z0ef8nEWjFoyVZIzp2ShAG1StLEt8Zeq2R"
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