from .FindLinksWithKeyword import find_links_with_keyword

# Funktion, um den ersten Link zurückzugeben, der das höchstpriorisierte Keyword enthält
def match_links_with_legal_keywords(base_url, links, url):
    legal_keywords = [
    "Impressum", "Imprint", 
    "AGB", "Terms",
    "AllgemeineGeschäftsbedingungen", "AllgemeineGeschaeftsbedingungen", "AllgemeineGesch%E4ftsbedingungen", 
    "Nutzungsbedingungen", "TermsOfUse",
    "Rechtlich", "Legal",
    "Urheberrecht", "Copyright",
    "Lizenz", "License",
    "Richtlinien", "Guidelines", "Policy",
    "Kontakt", "Contact"
    ]


    return find_links_with_keyword(base_url, links, legal_keywords, url, False, True)