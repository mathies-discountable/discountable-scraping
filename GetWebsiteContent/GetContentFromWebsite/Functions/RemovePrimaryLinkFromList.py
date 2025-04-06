def remove_primary_link_from_list(primary_link, links, base_url):
    if primary_link.startswith(base_url):
        primary_link = primary_link[len(base_url):]

    for link in reversed(links):
        if link.startswith(base_url):
            stripped_base_url_link = link[len(base_url):]
            if stripped_base_url_link.replace('/', '') == primary_link.replace('/', ''):
                links.remove(link)
        else:
            if link.replace('/', '') == primary_link.replace('/', ''):
                links.remove(link)

    return links