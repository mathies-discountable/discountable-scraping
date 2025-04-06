
def is_robots_valid(robots_text):
    if '<html>' in robots_text or '<body>' in robots_text or '<head>' in robots_text:
        return False
    else:
        return True