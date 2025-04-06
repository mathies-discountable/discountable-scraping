from GetContentFromWebsite.Functions.GetRobotsURL import get_robots_url
from GetContentFromWebsite.Functions.IsRobotsValid import is_robots_valid
from GetContentFromWebsite.Functions.IsUrlDisallowed import is_url_disallowed
from GetContentFromWebsite.Functions.IsSocialMediaURL import is_social_media_url
from GlobalFunctions.StripSubpaths import strip_subpaths
from GetContentFromWebsite.Functions.GetLinksFromWebsite import get_links_from_website
from GetContentFromWebsite.Functions.MatchLinksWithAllKeywords import match_links_with_all_keywords
from GetContentFromWebsite.Functions.MatchLinksWithCertainKeywords import match_links_with_certain_keywords
from GetContentFromWebsite.Functions.MatchLinksWithLegalKeywords import match_links_with_legal_keywords
from GetContentFromWebsite.Functions.RemovePrimaryLinkFromList import remove_primary_link_from_list
from GetContentFromWebsite.Functions.ExtractEmailsAsString import extract_emails_as_string

import requests

def fetch_content_from_website(row):

    # Scraping-Header setzen
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    website_url = None
    robots_exists = True

    # Places setzen
    id = row['locality_id']

    # Website setzen 
    website_url = row['website']
    
    # Wenn Facebook, dann aussortieren
    if is_social_media_url(website_url):
        print(f"Link führt zu Social-Media: {website_url}")
        return {'is_valid': False, 'id': id, 'website': website_url, 'error': 'SM', 'pricing_content': None, 'contact_email_adresses': None }

    # Die URL zuschneiden
    stripped_website_url = strip_subpaths(website_url)

    # Robots.txt fetchen und Status überprüfen
    robots_url = get_robots_url(stripped_website_url)
    try:
        robots_response = requests.get(robots_url, headers=header)
    except:
        print(f"Beim Website-Aufruf gab einen Error: {website_url}")
        return {'is_valid': False, 'id': id, 'website': website_url, 'error': 'c;W', 'pricing_content': None, 'contact_email_adresses': None }

    if robots_response.status_code != 200 or is_robots_valid(robots_response.text) == False:
        robots_exists = False

    # Überpüfen, ob die Mainpage bzw. die gesamte Seite nicht gecrawlt werden darf
    if robots_exists == True and is_url_disallowed(website_url, robots_response.text) == True:
        print(f"Scraping der Mainpage nicht erlaubt: {website_url}")
        return {'is_valid': False, 'id': id, 'website': website_url, 'error': 'd;M', 'pricing_content': None, 'contact_email_adresses': None  }
    
    # Main-Page fetchen und Status überprüfen
    mainpage_response = requests.get(website_url, headers=header)
    
    if mainpage_response.status_code != 200:
        print(f"Fehler beim Abrufen folgender Main-Page der Website: {website_url} Status-Code: {mainpage_response.status_code}")
        return {'is_valid': False, 'id': id, 'website': website_url, 'error': f'{mainpage_response.status_code};M', 'pricing_content': None, 'contact_email_adresses': None  }

    # Alle Links aus der Main-Page extrahieren
    links_from_mainpage = get_links_from_website(mainpage_response.text)

    # Links mit gefundenen Keywords extrahieren
    matched_link_main_page = match_links_with_all_keywords(website_url, links_from_mainpage, website_url)   

    # Die Links zum Impressum, AGB, etc. extrahieren
    matched_legal_and_contact_links = match_links_with_legal_keywords(website_url, links_from_mainpage, website_url)   


    content_for_email_extraction = mainpage_response.text + "\n"

    if matched_legal_and_contact_links != None:
        for link in matched_legal_and_contact_links: 
            legal_content_response = requests.get(website_url + "/" + link, headers=header)
            if legal_content_response.status_code == 200:        
                content_for_email_extraction += legal_content_response.text + "\n"

    contact_email_adresses = extract_emails_as_string(content_for_email_extraction)
        


    # Den Link speichern, falls existent
    if matched_link_main_page == None:
        print(f"Fehlende Links auf Mainpage der Website: {website_url} ")
        return {'is_valid': True, 'id': id, 'website': website_url, 'error': None, 'pricing_content': mainpage_response.text, 'contact_email_adresses': contact_email_adresses  }

    # Überprüfen, ob der Link gecrawlt werden darf
    pricing_page_link = website_url + "/" + matched_link_main_page
    if robots_exists == True and is_url_disallowed(pricing_page_link, robots_response.text) == True:
        print(f"Scraping der Preisseite nicht erlaubt: {pricing_page_link}")
        return {'is_valid': False, 'id': id, 'website': website_url, 'error': 'd;P', 'pricing_content': None, 'contact_email_adresses': None}

    # RawText des Preis-Seite fetchen und Status überprüfen
    pricing_page_response = requests.get(pricing_page_link, headers=header)

    if pricing_page_response.status_code != 200:
        print(f"Fehler beim Abrufen der Preis-Seite folgender Website: {website_url} Status-Code: {pricing_page_response.status_code}")
        return {'is_valid': False, 'id': id, 'website': website_url, 'error': f'{pricing_page_response.status_code};P', 'pricing_content': None, 'contact_email_adresses': None  }
    

    # Alle Links aus der Preis-Seite extrahieren
    links_from_pricing_page = get_links_from_website(pricing_page_response.text)

    # Alle Links, die gleich dem von der Mainpage sind, entfernen
    links_from_pricing_page = remove_primary_link_from_list(matched_link_main_page, links_from_pricing_page, website_url)

    # Link mit passendem Keywords extrahieren
    matched_link_pricing_page = match_links_with_certain_keywords(website_url, links_from_pricing_page, pricing_page_link)

    sub_page_exists = False
    if matched_link_pricing_page != None:

        # RawText der Unterseite der Pricing-Page fetchen und Status überprüfen
        pricing_sub_page_link = website_url + "/" + matched_link_pricing_page
        pricing_sub_page_response = requests.get(pricing_sub_page_link, headers=header)

        if pricing_sub_page_response.status_code != 200:
            print(f"Fehler beim Abrufen der Unterseite der Pricing-Page folgender Website: {website_url} Status-Code: {pricing_sub_page_response.status_code}")
            return {'is_valid': False, 'id': id, 'website': website_url, 'error': f'{pricing_sub_page_response.status_code};S', 'pricing_content': None, 'contact_email_adresses': None  }

        else: 
            # RawText von Unterseite von HTML-Code und irrelevantem Content bereinigen
            sub_page_exists = True

    if sub_page_exists == True:
        pricing_content = f"{pricing_page_response.text} \n {pricing_sub_page_response.text}"
    else:
        pricing_content = pricing_page_response.text 


    print("Content gefunden bei: ", website_url)
    return {'is_valid': True, 'id': id, 'website': website_url, 'error': None, 'pricing_content': pricing_content, 'contact_email_adresses': contact_email_adresses  }

    