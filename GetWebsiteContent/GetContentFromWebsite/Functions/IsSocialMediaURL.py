import re

def is_social_media_url(url):
    social_media_regex = re.compile(
        r'^(https?:\/\/)?(www\.)?(facebook\.com|linkedin\.com|twitter\.com|instagram\.com)\/.+$'
    )
    
    return social_media_regex.match(url) is not None