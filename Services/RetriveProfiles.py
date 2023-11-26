from . import models

def retrieve_profiles():
    try:
        profiles = models.get_all(models.Profile)

        if profiles:
            print("{:<10} {:<15} {:<30} {:<13} {:<20}".format(
                "name", "user_name", "email", "pull_rebase", "ssh_key_name"))
            for profile in profiles:
                
                name = profile.name
                user_name = profile.user_name
                email = profile.email
                pull_rebase = profile.pull_rebase
                ssh_key_name = profile.ssh_key_name                
                
                print("{:<10} {:<15} {:<30} {:<13} {:<20}".format(
                    name, user_name, email, pull_rebase, ssh_key_name))
            return profiles
        else:
            print("No profiles found.")
    except:
        print(f"Failed to retrieve profiles, Run the 'gpm start' command.")
