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
@click.argument("id", type=int)
def delete(id):
    from Services.DeleteProfiles import DeleteProfiles
    DeleteProfiles(id)

@gpm.command()
@click.argument("id", type=int)
def edit(id):
    from Services.EditProfiles import EditProfiles
    EditProfiles(id)

@gpm.command()
@click.argument("id", type=int)
def use(id):
    from Services.SwitchProfile import Switch_Profile
    Switch_Profile(id)

@gpm.command()
def start():
    from Services.Start import starts
    starts()

@gpm.command()
def stop():
    from Services.stop import stop as down
    down()


if __name__ == '__main__':
    gpm()
