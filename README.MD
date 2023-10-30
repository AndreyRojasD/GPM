# Table of Contents

- [GPM](#gpm)
- [Notes](#notes)
- [Contribution Guide](#contribution-guide)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Commands and Usage](#available-commands-and-usage)

## GPM

GPM is a cutting-edge tool that simplifies the management of Git profiles through the command line. With GPM, you can effortlessly oversee your Git profiles, addressing common challenges like accidentally sending commits to the wrong repositories with incorrect usernames or emails. This tool streamlines the process of switching between Git profiles, allowing you to do so with a single, user-friendly command. GPM is particularly valuable for developers working in the dynamic world of software consulting, where they often serve multiple clients, each with their unique SSH keys and Git profiles. This versatile tool empowers you to seamlessly switch between profiles, create, delete, edit, and list profiles, making your Git profile management a breeze.

## Notes

1. This tool is currently designed for use on Ubuntu systems, but it will soon be updated to enable usage on macOS and Windows.
2. This is an experimental version of the project, and we are open to recommendations. Please feel free to open bug reports or feature requests.

## Contribution Guide

1. Find the issue you want to work on, or open a new one and start working on it.
2. Create a branch with the following structure: `story-<<Issue-number>>`, such as `story-71`.
3. Only modify the necessary files and elements for your issue. If you notice something else that needs attention, please open a separate issue.
4. Once you have your changes ready, use conventional commits for your commits and include the issue reference in the commit message. For example: `feat: Add stop command (#2)`.

## Prerequisites

1. Python3
2. pip
3. Linux operating system

## Getting Started

1. Run the command `pip install -r requirements.txt`.
2. Execute the command `sudo ./install.sh`.
3. Run `gpm start`.
4. Execute the Python path command as shown in the output of `gpm start`.


## Available Commands and Usage

To streamline your Git profile management, GPM offers a range of powerful commands. Here's a list of available commands and their usage:

```bash
gpm create                # Create a new Git profile
gpm list                  # List all existing Git profiles
gpm use <<id_to_use>>     # Switch to a specific Git profile by providing its ID
gpm delete <<id_to_delete>>  # Delete a Git profile by specifying its ID
gpm edit <<id_to_edit>>    # Modify an existing Git profile using its ID
gpm start                # Start using GPM for efficient profile management
gpm stop                 # Halt GPM to complete your session
```

These commands enable you to effortlessly control and customize your Git profiles, making Git profile management a seamless part of your workflow.