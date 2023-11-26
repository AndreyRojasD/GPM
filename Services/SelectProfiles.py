from . import models

def get_profile(name):
    try:
        profile = models.filter(models.Profile.id == id, models.Profile).first()
        id = profile.id
        user_name = profile.user_name
        email = profile.email
        pull_rebase = profile.pull_rebase
        ssh_key_name = profile.ssh_key_name
        name = profile.name
        
        print("{:<10} {:<15} {:<30} {:<13} {:<20}".format(
                "name", "user_name", "email", "pull_rebase", "ssh_key_name"))
        print("{:<10} {:<15} {:<30} {:<13} {:<20}".format(
                    name, user_name, email, pull_rebase, ssh_key_name))
    except Exception as e:
        print(f"Failed get profile, Run the 'gpm start' command.")