from bs4 import BeautifulSoup

# Header und Footer entfernen
def remove_unnecessary_html_elements(html_text):

    soup = BeautifulSoup(html_text, 'html.parser')

    # Entferne Footer und Header Inhalte
    for footer in soup.find_all('footer'):
        footer.decompose()
    for header in soup.find_all('header'):
        header.decompose()

    return str(soup)