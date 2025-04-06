from urllib.parse import urlparse, urlunparse

# Alle Unterpfade von einer URL entfernen
def strip_subpaths(url):
    parsed_url = urlparse(url)
    # Rekonstruieren der URL mit nur Schema, Netzort und ohne Pfad/Parameter/Anker
    stripped_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    return stripped_url