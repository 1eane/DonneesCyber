from datetime import datetime
import random
import time


class Canal:
    def __init__(self):
        self.allMessages = []

    def postMsg(self, msg):
        self.allMessages.append(msg)

class Person: 
    def __init__(self, name, canalCom):
        self.name = name
        self.canalCom = canalCom
        self.myMsg = []

    def sendMsg(self):
        b = random.randint(0, 1)
        if(self.name == "Alice"):
            # case if Alice want send message
            if b == 0:
                body = "Alice"
            else:
                body = "Bob"
        else:
            # case if Bob want send message
            if b == 0:
                body = "Bob"
            else:
                body = "Alice"

        msg = body + " " + str(datetime.now())
        
        # add message to the canal
        self.canalCom.postMsg(msg)
        # add message to my personal message list
        self.myMsg.append(msg)

        # sleep between 0.5 and 1 secondes
        timerSleep = random.uniform(0.5,1)
        time.sleep(timerSleep)


    def extractSecret(self):
        secret = []
        for message in self.canalCom.allMessages:
            if message in self.myMsg:
                if self.name in message: 
                    bit = 0
                else: 
                    bit = 1
            else:
                if self.name in message:
                    bit = 1
                else: 
                    bit = 0
            # array with secret password
            secret.append(bit)
        return secret

    
def generateSecret(personA, personB, duration, canal):
    start_time = time.time()

    while time.time() - start_time < duration:
        personA.sendMsg()
        personB.sendMsg()


canal = Canal()

Alice = Person("Alice", canal)
Bob = Person("Bob", canal)

generateSecret(Alice, Bob, 5, canal)

print(Bob.extractSecret())
print(Alice.extractSecret())

print("tous les messages du canal : ")
print(canal.allMessages)
print("\n")

print("Bod messages : ")
print(Bob.myMsg)
print("\n")

print("Alice messages : ")
print(Alice.myMsg)