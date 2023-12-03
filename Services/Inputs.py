from Services import models
from Services.ListSshKeys import list_keys

def inputs():
     
     name = input("Insert the profile name: ")
     user_name = input("Insert you user name: ")
     email = input("Inert you user email: ")
     pull_rebase = input("Do you want to enable pull rebase y/n?: ")
     rebase = 'true' if pull_rebase == "y" else 'false'
     list_keys()
     ssh_key_name = input("Enter the name of your SSH key.: ")
     profile = models.Profile(user_name = user_name, name = name, email = email, pull_rebase = rebase , ssh_key_name = ssh_key_name)
     return profile
