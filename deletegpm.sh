#!/bin/bash

# 1. Elimina el enlace simbólico 'spm' si existe
if [[ -e /usr/local/bin/gpm ]]; then
    sudo rm /usr/local/bin/gpm
elif [[ -e "$HOME/bin/gpm" ]]; then
    rm "$HOME/bin/gpm"
fi

# 2. Elimina la configuración de PYTHONPATH del archivo .bashrc
project_dir="$(pwd)"
sed -i "/export PYTHONPATH=\$PYTHONPATH:$project_dir/Services/d" ~/.bashrc

echo "Uninstallation completed. The 'gpm' command and PYTHONPATH configuration have been removed."