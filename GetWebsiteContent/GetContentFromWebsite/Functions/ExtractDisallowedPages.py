import pandas as pd

# Verbotene Seiten aus der robots.txt extrahieren
def extract_disallowed_pages(robots_text):
    disallowed_paths = []
    user_agent_section = False

    for line in robots_text.splitlines():
        stripped_line = line.strip()

        if stripped_line.lower() == "user-agent: *":
            user_agent_section = True
            continue

        if "user-agent:" in stripped_line.lower() and not stripped_line.lower() == "user-agent: *":
            user_agent_section = False
            continue

        if user_agent_section and stripped_line.lower().startswith("disallow:"):
            path = stripped_line.split("Disallow:", 1)[1].strip()
            if path != "":
                disallowed_paths.append(path)

    return pd.Series(disallowed_paths, dtype='object')