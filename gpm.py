#!/usr/bin/python3
import click

@click.group(chain=True)
def gpm():
    pass

@gpm.command()
def list():
    from Services.RetriveProfiles import retrieve_profiles
    retrieve_profiles()

@gpm.command()
def create():
    from Services.CreateProfiles import create_profiles
    create_profiles()

@gpm.command()
@click.argument("name", type=str)
def delete(name):
    from Services.DeleteProfiles import DeleteProfiles
    DeleteProfiles(name)

@gpm.command()
@click.argument("name", type=str)
def edit(name):
    from Services.EditProfiles import EditProfiles
    EditProfiles(name)

@gpm.command()
@click.argument("name", type=str)
def use(name):
    from Services.SwitchProfile import Switch_Profile
    Switch_Profile(name)

@gpm.command()
def start():
    from Services.Start import starts
    starts()



if __name__ == '__main__':
    gpm()
