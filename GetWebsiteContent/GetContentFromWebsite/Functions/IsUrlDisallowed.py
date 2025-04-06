from GetContentFromWebsite.Functions.ExtractDisallowedPages import extract_disallowed_pages
import re

# Alle Links der Page extrahieren
def is_url_disallowed(url, robots_text):
    disallowed_paths = extract_disallowed_pages(robots_text)
    if disallowed_paths.empty:
        return False

    if disallowed_paths.str.contains("wholePageDisallowed").any() == True or disallowed_paths.str.contains(url).any() == True:
        return True

    for path in disallowed_paths:
        # Ersetzen von Wildcards (*) durch reguläre Ausdrücke
        pattern = path.replace('*', '.*')
        if re.search(pattern, url):
            return True
    return False