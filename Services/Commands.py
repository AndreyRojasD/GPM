from . import models

def combo_commands(profile: models.Profile):

    comands = {
        'user': f'git config user.name {profile.user_name}',
        'email': f'git config user.email {profile.email}',
        'pull': f'git config pull.rebase {profile.pull_rebase}',
        'ssh': f'git config --global core.sshCommand "ssh -i ~/.ssh/{profile.ssh_key_name}"',
    }
    return comands

