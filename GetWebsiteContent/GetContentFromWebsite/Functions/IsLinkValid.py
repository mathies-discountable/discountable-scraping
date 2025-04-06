# Funktion, um zu überprüfen, ob ein Link zur gegebenen URL gültig ist
def is_link_valid(link, base_url):

    forbidden_keywords = ["mailto:", "tel:", "wp-content", "news", "blog"]
    if (link.startswith("http://") or link.startswith("https://")) and not link.startswith(base_url):
        return False
    for keyword in forbidden_keywords:
        if keyword in link:
            return False
    return True