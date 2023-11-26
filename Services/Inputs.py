from . import models


def inputs():
     
     name = input("Insert the profile name: ")
     user_name = input("Insert you user name: ")
     email = input("Inert you user email: ")
     pull_rebase = input("Do you want to enable pull rebase? Enter 'true' to enable and 'false' to disable.: ")
     ssh_key_name = input("Enter the name of your SSH key.: ")
     profile = models.Profile(user_name = user_name, name = name, email = email, pull_rebase = pull_rebase, ssh_key_name = ssh_key_name)
     return profile
