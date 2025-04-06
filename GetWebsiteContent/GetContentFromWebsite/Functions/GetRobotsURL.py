from urllib.parse import urlparse

# Die URL der Robots.txt ermitteln
def get_robots_url(url):
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return f"{base_url}/robots.txt"