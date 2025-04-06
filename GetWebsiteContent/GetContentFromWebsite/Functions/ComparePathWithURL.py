from urllib.parse import urlparse, urljoin
from GetContentFromWebsite.Functions.NormalizePath import normalize_path

def compare_path_with_url(base_url, url, path):
    if url.replace('/','') == path.replace('/',''):
        return True

    # Extrahiert und vergleicht das Schema und die Domäne
    parsed_base_url = urlparse(base_url)
    parsed_url = urlparse(url)
    if parsed_base_url.scheme != parsed_url.scheme or parsed_base_url.netloc != parsed_url.netloc:
        return False  # Unterschiedliche Schemata oder Domänen

    # Normalisiert den Pfad der URL
    normalized_url_path = normalize_path(parsed_url.path)

    # Löst den relativen Pfad in Bezug auf die Basis-URL auf
    absolute_path = urljoin(base_url, path)
    parsed_absolute_path = urlparse(absolute_path)
    normalized_absolute_path = normalize_path(parsed_absolute_path.path)

    # Vergleicht die normalisierten Pfade
    return normalized_url_path == normalized_absolute_path