import imaplib
import email
from email.header import decode_header
import re

# Se connecter à la boîte mail
def connexion_boite_mail(username, password, imap_server):
    try:
        # Se connecter au serveur IMAP
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        print("Connexion réussie !")
        return mail
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None

def recuperer_emails(mail, dossier="INBOX", nombre_emails=10):
    try:
        # Sélectionner la boîte de réception
        mail.select(dossier)

        # Rechercher les derniers e-mails
        status, messages = mail.search(None, "ALL")
        message_ids = messages[0].split()

        emails = []
        for i in message_ids[-nombre_emails:]:  # Récupérer les derniers e-mails
            status, msg_data = mail.fetch(i, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    emails.append(msg)

        print(f"{len(emails)} e-mails récupérés.")
        return emails
    except Exception as e:
        print(f"Erreur lors de la récupération des e-mails : {e}")
        return []

# Fonction pour extraire les liens
def extraire_liens_email(msg):
    liens = []
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain" or content_type == "text/html":
                body = part.get_payload(decode=True).decode()
                pattern = r'https?://[^\s"]+'
                liens += re.findall(pattern, body)
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            body = msg.get_payload(decode=True).decode()
            pattern = r'https?://[^\s"]+'
            liens += re.findall(pattern, body)
    return liens

def detecter_phishing(liens, domaines_securises):
    liens_suspects = []
    for lien in liens:
        domaine = lien.split('/')[2]
        if domaine not in domaines_securises:
            liens_suspects.append(lien)
    return liens_suspects

def detecter_phishing(liens, domaines_securises):
    liens_suspects = []
    for lien in liens:
        domaine = lien.split('/')[2]
        if domaine not in domaines_securises:
            liens_suspects.append(lien)
    return liens_suspects

def generer_rapport(emails, domaines_securises, fichier_rapport="rapport_phishing.txt"):
    with open(fichier_rapport, "w") as f:
        for email_msg in emails:
            sujet = decode_header(email_msg["Subject"])[0][0]
            if isinstance(sujet, bytes):
                sujet = sujet.decode()

            liens = extraire_liens_email(email_msg)
            liens_suspects = detecter_phishing(liens, domaines_securises)

            f.write(f"Sujet : {sujet}\n")
            f.write(f"Liens détectés : {liens}\n")
            f.write(f"Liens suspects : {liens_suspects}\n\n")
    print(f"Rapport généré : {fichier_rapport}")


if __name__ == "__main__":
    username = input("entrer votre adresse mail tel que: email@example.com ")
    password = input("entrer votre mot de passe")
    imap_server = input("entrer votre imap: 'imap.gmail.com' ou 'outlook.office365.com' ")
    domaines_securises = ["www.google.com", "www.gmail.com"]

    mail = connexion_boite_mail(username, password, imap_server)
    if mail:
        emails = recuperer_emails(mail, nombre_emails=5)
        generer_rapport(emails, domaines_securises)