from GetContentFromWebsite.Functions.FindLinksWithKeyword import find_links_with_keyword

# Funktion, um den ersten Link zurückzugeben, der das höchstpriorisierte Keyword enthält
def match_links_with_all_keywords(base_url, links, url):
    keywords = [
    "Preis", "Pric",
    "Eintritt", "Admission", "Entrance",
    "Ermäßig", "Ermaßig", "Ermassig", "Ermaeßig", "Ermaessig", "Erma%DFig", "Ermae%DFig", "Discount",
    "Behindertenrabatt", "DisabledDiscount",
    "Behindert", "Disabled",
    "Eingeschränkt", 
    "Eingeschrankt", 
    "Eingeschraenkt", 
    "Rabatt", 
    "Nachteilsausgleich",
    "Nachteil", "Disabled",
    "Nachlass", 
    "Ticket", 
    "Tarife", "Rates",
    "Kosten", "Costs",
    "Gebühren", "Gebuehren", "Gebuhren", "Geb%FCehren", "Fee",
    "Karte", 
    "FAQ",
    "HäufiggestellteFragen", "HaeufiggestellteFragen", "HaufiggestellteFragen", "H%E4ufiggestellteFragen", "FrequentlyAskedQuestions",
    "Mitgliedschaft", "Membership",
    "Pauschale", "FlatRate",
    "Information", "Information",
    "Detail", 
    "Allgemeines", "General",
    "Angebote", "Offers",
    "Aktionen", "Promotions",
    "Besuch", "Visit",
    "Planen",
    "Übersicht", "Uebersicht", "Ubersicht", "U%FCbersicht", "Overview"
]


    return find_links_with_keyword(base_url, links, keywords, url, True, False)