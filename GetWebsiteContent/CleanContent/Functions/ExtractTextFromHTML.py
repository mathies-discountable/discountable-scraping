from bs4 import BeautifulSoup

def extract_text_from_html(rawHtml):

    soup = BeautifulSoup(rawHtml, 'html.parser')
    
    # Entfernen von Script- und Style-Tags
    for script in soup(["script", "style"]):
        script.extract()
    
    # Extrahieren des Textes
    text = soup.get_text()

    # Mehrere Leerzeichen und Zeilenumbrüche entfernen
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text