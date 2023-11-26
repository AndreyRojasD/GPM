from . import models


def DeleteProfiles(name):
    try:
        profile = models.filter(models.Profile.name == name, models.Profile).first()
        if not profile:
            print("Profile not found.")
            return
        profile.delete()
        models.commit()
    except Exception as e:
        print(f"Failed delete profile, Run the 'gpm start' command.")

