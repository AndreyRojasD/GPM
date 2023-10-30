from Querys import DeleteProfile
from connector import dbconnector
def DeleteProfiles(id):
    try:
        query = DeleteProfile(id)
        with dbconnector() as db:
         db.execute(query)
    except Exception as e:
        print(f"Failed delete profile, review file Services/DeleteProfiles Error: {str(e)},  Run the 'gpm start' command and wait for a few seconds.")

