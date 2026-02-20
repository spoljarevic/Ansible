## Execute Playbooks ##
Since the playbooks here will only be ran **locally**, you don't need to change the inventory file
Just run the following command.. good luck.

Use for playbooks that don't need priviliged rights
```
ansible-playbook yourPlaybook.yml
```
Use for those who need it
```
ansible-playbook yourPlaybook.yml -K
```
