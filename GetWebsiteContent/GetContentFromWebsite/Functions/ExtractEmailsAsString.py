import re

def extract_emails_as_string(text):
    # Regulärer Ausdruck für E-Mail-Adressen
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)

    # Doppelte E-Mails entfernen
    emails = list(set(emails))

    # wenn keine E-Mails gefunden wurden, None zurückgeben
    if not emails:
        return None
    
    # Zusammenführen der gefundenen E-Mails zu einem String
    return " ".join(emails)