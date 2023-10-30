from Querys import UpdateProfiles
from connector import dbconnector
from Inputs import inputs
from models.Dbmodels import Profiles
def EditProfiles(id):
    try:
        data  = inputs()
        profile = Profiles(id , user_name = data.user_name, email = data.email, pull_rebase = data.pull_rebase, ssh_key_name = data.ssh_key_name)
        query = UpdateProfiles(profile)
        with dbconnector() as db:
            db.execute(query)
    except Exception as e:
           print(f"Failed Edit profile, review file Services/EditProfiles Error: {str(e)}, Run the 'gpm start' command and wait for a few seconds.")

