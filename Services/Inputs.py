from models.Dbmodels import Profiles


def inputs():
     
     id = 1
     user_names = input("Insert you user name: ")
     emails = input("Inert you user email: ")
     pull_rebases = input("Do you want to enable pull rebase? Enter 'True' to enable and 'False' to disable.: ")
     ssh_key_names = input("Enter the name of your SSH key.: ")
     profile = Profiles(id ,user_names, emails, pull_rebases,ssh_key_names)
     return profile

