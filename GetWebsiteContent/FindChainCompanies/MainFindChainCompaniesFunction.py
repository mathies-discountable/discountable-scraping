from FindChainCompanies.Functions.ExtractDomainName import extract_domain_name
from FindChainCompanies.Functions.AddLocalityToChainInDatabase import add_locality_to_chain_in_database

def is_chain_company(website_url, already_iterated_localities, chain_companies):
    
    for chain_url in chain_companies:
        if extract_domain_name(website_url) in chain_url:
            add_locality_to_chain_in_database(chain_url, website_url)
            return {'is_chain': True, 'chain_url': chain_url}
    
    if extract_domain_name(website_url) in already_iterated_localities:
        return {'is_chain': True, 'chain_url': None}

    return {'is_chain': False, 'chain_url': None}


