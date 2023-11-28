from datetime import date, datetime
from time import strftime
import random
import sched, time


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
        time = datetime.now()
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
        self.canalCom.postMsg(msg)
        self.myMsg.append(msg)

    def extractSecret(self):
        secret = []
        #pour chaque message
        for message in self.canalCom.allMessages:
            #regarder si il s'agit d'un message envoyé par la personne
            if message in self.myMsg:
                #regarder si il contient Alice ou Bob
                if self.name in message: # cas où le message de la personne contient le nom de la même personne 
                    bit = 0
                else: # cas où le message de la personne contient le nom d'une autre personne
                    bit = 1
            else :#si ce n'est pas un message envoyé par la personne
                if self.name in message: # cas où le message envoyé par une autre personne contient le nom de la personne qui récupère le secret
                    bit = 1
                else: # cas où le message envoyé par une autre personne contient le nom de cette autre personne
                    bit = 0
            #en déduire la valeur du bit et le stocker dans le secret 
            secret.append(bit)
        return secret

    
def genererSecret(personA, personB, duration, canal):
    start_time = time.time()

    while len(canal.allMessages) < 10:
        current_time = time.time()
        elapsed_time = current_time - start_time
        personA.sendMsg()
        personB.sendMsg()

        time.sleep(0.3)



canal = Canal()

Alice = Person("Alice", canal)
Bob = Person("Bob", canal)

genererSecret(Alice,Bob, 1, canal)

print(Bob.extractSecret())
print(Alice.extractSecret())

print("tous les messages du canal : \n")
print(canal.allMessages)

print("Bod messages : \n")
print(Bob.myMsg)

print("Alice messages : \n")
print(Alice.myMsg)