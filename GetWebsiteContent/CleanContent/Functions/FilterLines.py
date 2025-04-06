import re

def filter_lines(text):

    #! Bei über 500 Zeilen: rauswerfen
    def contains_telephone_number(text):
        pattern = r'\b(\+?\d{1,4}[\s-]?)?\(?\d{1,4}\)?([\s-]?\d{1,4}){2,3}\b'
        return bool(re.match(pattern, text))

        # Schlüsselwörter in einer Inline-Liste
    keywords = ["Cookie", "Datenschutz", "Akzeptieren", "Nutzungsbedingungen", "AGB", "Allgemeine Geschäftsbedingungen",
    "Impressum", "Anmeld", "Registrier", "Login", "Konto", "Newsletter", "Abonnieren",  "Menü", "Imbiss", "Restaurant",
    "Social Media", "Social-Media", "Twitter", "Facebook", "Instagram", "LinkedIn", "YouTube", "Teilen", "Snapchat", "TikTok",
    "Kontakt", "Standort", "Adresse", "Telefon", "FAQ", "Tracking", "Analyse", "ÖPNV", "Anfahrt", "speichern", "share", 
    "Tab" , "Suche", "Route", "Karte", "Contact", "Google", "Maps", "Wegbeschreibung", 
    "?", "Englis", "Sprache", "language", "Pfeiltaste" , "Connection", "Verbindung", "Content", "Galerie", "Medien" ,"Rundgang", "Datei", 
    "PDF", "JPG", "PNG", "JPEG", "HEIC", "zurück", "Fax", "Mail", "straße", "Str.", "Hausnummer", 
    "strasse", "3D", "Tour", "Folge uns", "Follow", "Termin", "click" ,"springen", "move", "skip", "open"
    "close", "Taxi", "Zug",  "@", "Parkh","geschlo", "Stellenangebote", "Karriere", "Jobs", "Bewerb", "Store",
    "Navigation", "Sitemap", "Sponsor", "Quicklinks", "Aktuelles", "Homepage", "Startseite", "Information", "Support","©", 
    "Kundenservice", "Postfach", "PLZ", "Postleitzahl", "GmbH", "user", "typo", "Silvester", "Neujahr", "Ostern", "Pfingsten", "Weihnacht",
    "Heiligabend", "Präferenz", "Einstellung", "Kunst", "Geschicht", "Auto", "Bahn", "löschen" ]

    lines = text.split('\n')
    filtered_lines = []

    for line in lines:
        if not any(keyword.lower() in line.lower() for keyword in keywords) and len(line) > 1 and not contains_telephone_number(line):
            filtered_lines.append(line)

    return '\n'.join(filtered_lines)