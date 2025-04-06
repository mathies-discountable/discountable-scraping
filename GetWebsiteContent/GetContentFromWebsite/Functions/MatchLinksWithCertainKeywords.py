from GetContentFromWebsite.Functions.FindLinksWithKeyword import find_links_with_keyword

# Funktion, die den ersten Link zurückgibt, der eines der speziellen Keywords enthält
def match_links_with_certain_keywords(base_url, links, url):
    keywords = [
        "Ermäßig", "Ermaßig", "Ermassig", "Ermaeßig", "Ermaessig", 
        "Erma%DFig", "Ermae%DFig", "Behindertenrabatt", "Behindert", "Rabatt", "Nachteilsausgleich", "Nachteil", "Eingeschränkt", 
        "Eingeschrankt", "Eingeschraenkt", "Nachlass", "Details", "FAQ", "HäufiggestellteFragen", "HaeufiggestellteFragen",
        "HaufiggestellteFragen", "H%E4ufiggestellteFragen"
    ]

    return find_links_with_keyword(base_url, links, keywords, url, False, False)