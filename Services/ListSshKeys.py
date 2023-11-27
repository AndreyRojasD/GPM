import os

def list_keys():
    path = os.path.expanduser('~/.ssh')
    files = os.listdir(path)
    files_only_name = [element for element in files if ".pub" not in element and ".old" not in element] 
    print("""
======================================
== Available SSH keys in your system =
======================================""")
    for file in files_only_name:
        print(file)
        

