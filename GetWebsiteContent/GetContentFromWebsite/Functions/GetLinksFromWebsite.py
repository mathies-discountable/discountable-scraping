from bs4 import BeautifulSoup

# Alle Links der Page extrahieren
def get_links_from_website(rawText):
    soup = BeautifulSoup(rawText, 'html.parser')

    # Alle 'a'-Tags finden, die 'href'-Attribute extrahieren und alle Links, die auf Bilder verweisen, entfernen
    links = [a['href'] for a in soup.find_all('a', href=True) if not a['href'].lower().endswith(('.jpg', '.heic' '.jpeg', '.png', '.gif', '.bmp'))]

    # Entfernen von Duplikaten
    links = list(set(links))

    return links