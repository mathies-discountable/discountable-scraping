from GlobalFunctions.CreateClient import create_supabase_client
import pandas as pd

def fetch_data_from_database():

    supabase = create_supabase_client()

    response = supabase.table('Locality').select("locality_id", "name", "email_from_osm", "website").is_("error_code", "null").is_("has_discounts", "null").is_("email_sent", "false").is_("no_email_avaiable", "null").not_.is_("website", "null").execute()
    response_df = pd.DataFrame(response)

    fetched_localities = response_df[1][0] 

    fetched_localities_df = pd.DataFrame(fetched_localities)

    return fetched_localities_df