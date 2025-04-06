# Links nach Position der KEyowrds zuschneiden
def find_keyword_and_cut_link(link, keyword, base_url, should_shorten):

    if keyword.lower() in link.lower():
        if link.startswith(base_url):
            link = link[len(base_url):]
            if not link:  
                return '/'

        keyword_end_index = link.lower().find(keyword.lower()) + len(keyword)
        next_slash_index = link.find('/', keyword_end_index)

        if next_slash_index != -1 and should_shorten:
            return link[:next_slash_index]
        else:
            return link
    else:
        return "/"  # Gibt den unveränderten Link zurück, wenn kein Keyword gefunden wurde