from GlobalFunctions.CreateClient import create_supabase_client
import pandas as pd

def fetch_chain_companies_from_database():
    supabase = create_supabase_client()

    response = supabase.table('ChainCompany').select("chain_domain").execute()
    df = pd.DataFrame(response)
    
    fetched_chain_companies = df[1][0] 

    website_list = [item['chain_domain'] for item in fetched_chain_companies]

    return website_list