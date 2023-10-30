from models.Dbmodels import Profiles

def combo_commands(profile:Profiles):
    pull_value = "true" if profile.pull_rebase else "false"
    comands = {
        'user': f'git config user.name {profile.user_name}',
        'email': f'git config user.email {profile.email}',
        'pull': f'git config pull.rebase {pull_value}',
        'ssh': f'git config --global core.sshCommand "ssh -i ~/.ssh/{profile.ssh_key_name}"',
    }
    return comands

