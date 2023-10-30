#!/bin/bash


chmod +x gpm.py
chmod +x start.sh
if [[ -w /usr/local/bin ]]; then
    sudo ln -s "$(pwd)/gpm.py" /usr/local/bin/gpm
else
    if [ -d "$HOME/bin" ] && [[ -w "$HOME/bin" ]]; then
        ln -s "$(pwd)/gpm.py" "$HOME/bin/gpm"
    elseUnable to create the symbolic link. Ensure you have write permissions in /usr/local/bin or create the $HOME/bin directory and add it to your PATH environment variable
        echo ""
        exit 1
    fi
fi

./start.sh
