from RetriveProfiles import retrieve_profiles
from models.Dbmodels import Profiles

def get_profile(id):
    try:
        profiles = retrieve_profiles()

        for profile in profiles:
            if profile[0] == id:
                id, user_name, email, pull_rebase, ssh_key_name = profile
                return Profiles(id, user_name, email, pull_rebase, ssh_key_name)
            print("ID de perfil no encontrado.")

    except Exception as e:
        print(f"Error al seleccionar el perfil, verifique la ruta Services/SelectProfiles: {e},  Run the 'gpm start' command and wait for a few seconds.")