from .SelectProfiles import get_profile
from .Commands import combo_commands
from . import models
import subprocess
def Switch_Profile(name):
    try:
      profile = models.filter(models.Profile.name == name, models.Profile).first()
      if not profile:
        print("Profile not found.")
        return
      commands = combo_commands(profile)
      for key, command in commands.items():
        subprocess.run(command, shell=True, check=True, universal_newlines=True)
      print(f"The profile was successfully changed to {profile.name}.")
    except Exception as e:
      print(f"Something went wrong while trying to switch profiles, Run the 'gpm start' command.")


