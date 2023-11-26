from . import models
from .Inputs import inputs
def create_profiles():
    try:
        profile = inputs()
        if models.filter(models.Profile.name == profile.name, models.Profile).first():
            print("Profile already exists.")
            return
        models.save(profile)
    except Exception as e:
        print(f"Failed create profile, Run the 'gpm start' command.")
