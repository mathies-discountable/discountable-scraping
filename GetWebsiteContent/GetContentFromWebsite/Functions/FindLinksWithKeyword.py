from GetContentFromWebsite.Functions.ComparePathWithURL import compare_path_with_url
from GetContentFromWebsite.Functions.FindKeywordAndCutLink import find_keyword_and_cut_link
from GetContentFromWebsite.Functions.IsLinkValid import is_link_valid

# Funktion, welche die Links mit den Keywords vergleicht und den kürzesten oder alle Links zurückgibt
def find_links_with_keyword(base_url, links, keywords, url, should_shorten, return_all):

    legal_links_with_keyword = []

    for keyword in keywords:

        pricing_links_with_keyword = []

        for link in links:

            # Vergleiche den aktuellen Link mit der Basis-URL und der gegebenen URL
            if compare_path_with_url(base_url, url, link) == False:

                # Suche nach dem Keyword im Link und kürze den Link ggf.
                link_with_keyword = find_keyword_and_cut_link(link, keyword, base_url, should_shorten)

                # Überprüfe, ob der Link gültig ist, nicht zur Startseite führt und kein "#" enthält
                if is_link_valid(link_with_keyword, base_url) == True and link_with_keyword != "/" and "#" not in link_with_keyword:

                    pricing_links_with_keyword.append(link_with_keyword)

                    # Füge die temporäre Liste der Hauptliste hinzu (dies könnte redundant sein)
                    legal_links_with_keyword.append(link_with_keyword)

        # Falls mindestens ein Link mit dem Keyword gefunden wurde und nicht alle zurückgegeben werden sollen
        if pricing_links_with_keyword and return_all == False:
            # Wähle den kürzesten Link aus der Liste
            shortest_link = min(pricing_links_with_keyword, key=len)
            return shortest_link

    # Falls Links gefunden wurden und alle zurückgegeben werden sollen
    if legal_links_with_keyword and return_all == True:
        return legal_links_with_keyword
    else:
        # Keine passenden Links gefunden
        return None
