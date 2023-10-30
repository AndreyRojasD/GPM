from connector import dbconnector
from Querys import SelectProfiles as SelectProfiles

def retrieve_profiles():
    try:
        with dbconnector() as db:
            query = SelectProfiles()
            db.execute(query)
            results = db.fetchall()

            if results:
                print("{:<10} {:<15} {:<30} {:<13} {:<20}".format(
                    "id", "user_name", "email", "pull_rebase", "ssh_key_name"))
                for row in results:
                    id, user_name, email, pull_rebase, ssh_key_name = row
                    print("{:<10} {:<15} {:<30} {:<13} {:<20}".format(
                        id, user_name, email, pull_rebase, ssh_key_name))
                return results
            else:
                print("No profiles found.")
    except Exception as e:
        print(f"Failed to retrieve profiles, review file Services/RetrieveProfiles Error: {str(e)},  Run the 'gpm start' command and wait for a few seconds.")
