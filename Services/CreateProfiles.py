from connector import dbconnector
from Querys import CreateProfiles
from models.Dbmodels import Profiles
from HashGenerate import hashing
from Inputs import inputs
def create_profiles():
    try:
        id = hashing()
        data = inputs()
        profile = Profiles(id , user_name = data.user_name, email = data.email, pull_rebase = data.pull_rebase, ssh_key_name = data.ssh_key_name)
        query = CreateProfiles(profile)
        with dbconnector() as db:
            db.execute(query)
    except Exception as e:
        print(f"Failed create profile, review file Services/CreateProfiles Error: {str(e)},  Run the 'gpm start' command and wait for a few seconds.")
