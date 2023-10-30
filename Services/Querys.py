def SelectProfiles():
    try:
        query = "SELECT * FROM profiles"
        return query
    except Exception as e:
        print(f"Error with SelectProfiles review file Services/Querys Function SelectProfiles Error: {e}")
def CreateProfiles(profile):
    try:
        query = f"INSERT INTO profiles (id, user_name, email, pull_rebase,ssh_key_name) VALUES ({profile.id}, '{profile.user_name}', '{profile.email}', {profile.pull_rebase}, '{profile.ssh_key_name}');"
        return query
    except Exception as e:
        print(f"Error with SelectProfiles review file Services/Querys Function CreateProfiles Error: {e}")
def UpdateProfiles(profile):
    try:
        query = f"Update profiles SET user_name = '{profile.user_name}', email = '{profile.email}', pull_rebase = {profile.pull_rebase}, ssh_key_name = '{profile.ssh_key_name}' WHERE id  = {profile.id}"
        return query
    except Exception as e:
        print(f"Error with UpdateProfiles review file Services/Querys Function CreateProfiles Error: {e}")
def DeleteProfile(id):
    try:
        query = f"DELETE FROM profiles WHERE id = {id}"
        return query
    except Exception as e:
         print(f"Error with UpdateProfiles review file Services/Querys Function CreateProfiles Error: {e}")
