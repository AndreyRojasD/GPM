from SelectProfiles import get_profile
from Commands import combo_commands
import subprocess
def Switch_Profile(id):
    try:
      profile = get_profile(id)
      commands = combo_commands(profile)
      for key, command in commands.items():
           subprocess.run(command, shell=True, check=True, universal_newlines=True)
      print(f"The profile was successfully changed to {id}")
    except Exception as e:
       print(f"Something went wrong while trying to switch profiles, the source of the problem is in Services/SwitchProfile. {e}, Run the 'gpm start' command and wait for a few seconds.")


