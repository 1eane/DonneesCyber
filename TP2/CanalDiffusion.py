from datetime import datetime
import random

class CanalDiffusionAnonyme:
    def __init__(self):
        # Utilisons une liste pour stocker les messages
        self.messages = []

    def posterMessageAnonyme(self, message):
        # Ajoute le message avec l'étiquette temporelle
        timestamp = datetime.now().strftime("%Hh%Mm%Ss")
        message_poste = {"message": message, "timestamp": timestamp}
        self.messages.append(message_poste)

        # Trie la liste des messages par ordre chronologique
        self.messages = sorted(self.messages, key=lambda x: x["timestamp"])

    def afficherMessages(self):
        # Affiche les messages dans l'ordre chronologique
        for message in self.messages:
            print(f"{message['timestamp']} : {message['message']}")

    def recupererMessagesAnonymes(self, debut, fin):
        messages_periode = []

        # Parcours des messages et récupération de ceux dans la période spécifiée
        for message in self.messages:
            if debut <= message['timestamp'] <= fin:
                messages_periode.append(message['message'])

        return messages_periode

