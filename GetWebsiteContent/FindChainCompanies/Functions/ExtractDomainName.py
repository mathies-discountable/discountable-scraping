from GlobalFunctions.StripSubpaths import strip_subpaths

def extract_domain_name(url):

    url = strip_subpaths(url)

    url = url.replace("http://", "")
    url = url.replace("https://", "")
    
    return url