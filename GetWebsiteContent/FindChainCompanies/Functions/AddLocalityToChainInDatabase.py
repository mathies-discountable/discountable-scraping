from GlobalFunctions.CreateClient import create_supabase_client

def add_locality_to_chain_in_database(chain_url, locality_id):
    supabase = create_supabase_client()

    supabase.table('Chain').insert({"id": 1, "name": "Denmark"}).execute()


    