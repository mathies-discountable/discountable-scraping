
from GlobalFunctions.CreateClient import create_supabase_client

def push_localities_in_database(invalid_localities_df):
    
    supabase = create_supabase_client()

    for index, row in invalid_localities_df.iterrows():
        supabase.table('Locality').update({"error_code": row['error']}).eq("locality_id", row['id']).execute()