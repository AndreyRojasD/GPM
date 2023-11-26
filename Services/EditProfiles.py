from .Inputs import inputs
from . import models

def EditProfiles(name):
    try:
        profile = models.filter(models.Profile.name == name, models.Profile).first()
        if not profile:
            print("Profile not found.")
            return
        print("Press enter to leave the field unchanged.")
        data = inputs()
        if data.email != "":
            profile.email = data.email
        if data.user_name != "":
            profile.user_name = data.user_name
        if data.pull_rebase != "":
            profile.pull_rebase = data.pull_rebase
        if data.ssh_key_name != "":
            profile.ssh_key_name = data.ssh_key_name
        if data.name != "":
            profile.name = data.name
        models.save(profile)
        
    except Exception as e:
           print(f"Failed Edit profile, Run the 'gpm start' command.")

