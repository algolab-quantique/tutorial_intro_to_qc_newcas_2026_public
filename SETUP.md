# Environment Setup 

These instructions will set up a solid coding environment that will work well for this tutorial and afterwards. 
You do not have to use it, but the running instructions will assume it.

In particular, we will install VS Code as the integrated development environment (IDE) and pyenv as the python version handler.

Each hands-on will then have instructions to allow you to safely install the needed packages. 

We emphasize safely here as there have been recent `supply chain attacks` targeting popular packages such as numpy. Such attacks aim to *silently* acquire the host machine's login credentials, including for password managers.

The best way to follow the instructions is to just copy-paste the terminal commands where they are used.

If you have problems with the setup, just let me know. It is better to ask than to spend a lot of time trying to get the setup to work.

## Environment Setup Instructions

1. Set up VS Code and Pyenv for your operating system following the appropriate section below:
    - [Windows](#vs-code-and-pyenv-in-windows-setup)
    - [Linux](#vs-code-and-pyenv-in-linux-setup)
    - [MacOS](#vs-code-and-pyenv-in-macos-setup)
1. Run VSCode
1. Open the extensions side bar. The icon looks like ![Four boxes, with one tilted](./exensions_icon_dark.png).
1. Search for and install the following add-ons:
    - Python ([direct link](https://marketplace.visualstudio.com/items?itemName=ms-python.python))
    - Jupyter ([direct link](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter))

After this, your setup should be good to go. Each hands-on will have instructions on creating a local environment and installing the needed python packages. Again, it is best to just copy-paste the commands in order to avoid typos and complications.

## VS Code and Pyenv in Windows Setup

VSCode combined with WSL documentation can be [found here](https://code.visualstudio.com/docs/remote/wsl).

1. ### Install WSL2

    Note: You need Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11. If you do not have have that, [see here](https://learn.microsoft.com/en-us/windows/wsl/install#prerequisites).

    In PowerShell (search for *PowerShell* in the start menu), run:

    `wsl.exe --install --web-download -d Ubuntu-24.04`

    After installation, follow the instructions for setup (i.e., add username, password, etc.). You may need to restart your computer and re-execute the above command twice.

    To open WSL2/Ubuntu in the future, run `wsl.exe` in PowerShell 

1. ### Install VS Code

    Install VS Code **in Windows**, *not* in WSL2/Ubuntu.

    [VS Code download is here](https://code.visualstudio.com/Download).

    **Note**: When prompted to `Select Additional Tasks` during installation, be sure to check the `Add to PATH` option so you can easily open a folder in WSL using the `code` command.

1. ### Install VS Code WSL add-on

    Go [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) or, in VS Code, search for `WSL` in the extensions side bar (the icon looks like four boxes, with one tilted).

1. ### Install Pyenv

    Pyenv allows you to easily manage python versions.

    If you have trouble with the installation, see the [Pyenv documentation](https://github.com/pyenv/pyenv#installation).

    1. Install pyenv by running the following in the WSL2/Ubuntu terminal (*not* the VS Code terminal): 

        `curl -fsSL https://pyenv.run | bash`

    1. Activate pyenv in the shell with
        
        `pyenv init --install`

        If the shell cannot find *pyenv* in the future, [see here](https://github.com/pyenv/pyenv#b-set-up-your-shell-environment-for-pyenv).
        
    1. Restart the shell with

        `exec "$SHELL"`

    1. Install the needed dependencies with the following. Copy and paste the whole thing at once.

        ```
        sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev curl git \
        libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libzstd-dev
        ```

1. ### Install venv 
    venv allows for the creation of python environments.

    You can use the following commands:
    ```
    sudo apt update
    sudo apt install python3-venv
    ```

1. ### [Return to Main Instructions](#environment-setup-instructions)



##  VS Code and Pyenv in Linux Setup

1. ### Install VS Code

    [VS Code download is here](https://code.visualstudio.com/Download).

1. ### Install Pyenv

    Pyenv allows you to easily manage python versions.

    If you have trouble with the installation, see the [Pyenv documentation](https://github.com/pyenv/pyenv#installation).

    1. Install pyenv by running the following in the terminal: 

        `curl -fsSL https://pyenv.run | bash`

    1. Activate pyenv in the shell with
        
        `pyenv init --install`

        If the shell cannot find *pyenv* in the future, [see here](https://github.com/pyenv/pyenv#b-set-up-your-shell-environment-for-pyenv).
        
    1. Restart the shell with

        `exec "$SHELL"`

    1. Install the needed dependencies with the following. Copy and paste the whole thing at once.

        ```
        sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev curl git \
        libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libzstd-dev
        ```

1. ### [Return to Main Instructions](#environment-setup-instructions)

## VS Code and Pyenv in MacOS Setup

1. ### Install VS Code

    [VS Code download is here](https://code.visualstudio.com/Download).

1. ### Install Pyenv

    Pyenv allows you to easily manage python versions.

    If you have trouble with the installation, see the [Pyenv documentation](https://github.com/pyenv/pyenv#installation).

    1. Install [homebrew](https://brew.sh/) if you don't have it by running the following in the terminal: 

        `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    1. Install pyenv with 

        `brew update`
        
        `brew install pyenv`
    1. Activate pyenv in the shell with
        
        `pyenv init --install`

        
    1. Restart the shell with

        `exec "$SHELL"`

    1. Install the needed dependencies with 

        `brew install openssl@3 readline sqlite3 xz tcl-tk@8 libb2 zstd zlib pkgconfig`

1. ### [Return to Main Instructions](#environment-setup-instructions)