## What are you seeing? ##
This is for **developing and testing** new Ansible Playbooks for Arch Linux post-installation.
My big project for **march** is a complete overhaul of the archinstall.yml Ansible Playbook, which will handle everything there is **after the installation of the OS** for it to be great.

Here will only be **snippets** of what will be in the new playbook.
I **test parts of it here** in different playbooks and combine the thing at the end when everything works.

What you see here can work but garuntiee for nothing.

### What is currently tested? ###
At the moment, the following Playbooks are tested and work in my machine.
Please note that after a fresh arch installation you'll need to install python and python3 for Ansible to work on the remote machine.

- AurInstaller - Works after installing [kewlfft.aur](https://galaxy.ansible.com/ui/repo/published/kewlfft/aur/)

- SSHKeys - Works fine. You'll need to create a Vault via ``ansible-vault create group_vars/arch/vault.yml`` where you  add the variable ``ssh_key_passphrase: "PasswordForSSHKey"`` and execute the playbook via ``ansible-playbook -i inventory.ini -b -K --ask-vault-pass snippets/sshkeys.yml``



### Currently not working ###
- gitclone - It fails due to a permission issue when cloning Repos via SSH (even public ones), needs more investigation
