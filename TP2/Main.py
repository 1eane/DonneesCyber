import CanalDiffusionAnonyme from CanalDiffusion


def genererSecret(canal, interlocuteur1, interlocuteur2, duree):
    debut = int(time() * 1000)
    fin = debut + duree * 1000  # Convertir la durée en millisecondes

    while int(time() * 1000) < fin:
        bit = choice([0, 1])
        if bit == 0:
            canal.posterMessageAnonyme(f"{interlocuteur1}")
        else:
            canal.posterMessageAnonyme(f"{interlocuteur2}")
        sleep(0.001)  # Attente de 1 milliseconde entre les messages

canal = CanalDiffusionAnonyme()
alice = "Alice"
bob = "Bob"

duree_protocol = 5  # Durée de 60 secondes

# Supposons que la génération commence maintenant
debut_protocol = datetime.now() - timedelta(seconds=duree_protocol)
fin_protocol = datetime.now()

# Extraction du secret
secret = extraireSecret(canal, debut_protocol.strftime("%Y-%m-%d %H:%M:%S"), fin_protocol.strftime("%Y-%m-%d %H:%M:%S"))
print("Le secret partagé est :", secret)

# Vérification du secret
SecretAlice = alice.verifierSecret(secret)
SecretBob = bob.verifierSecret(secret)

print(SecretAlice)
print(SecretBob)

if SecretAlice == SecretBob:
    print("Alice et Bob ont le même secret")
else:
    print("Alice et Bob n'ont pas le même secret")