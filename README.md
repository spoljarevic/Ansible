# Notes about this Project

All the code gets published to **Codeberg**. All other platforms are just mirrors.

Issues, pull requests, and everything else will only be looked at on **codeberg.org**.


# Ansible Playbooks for Semaphore UI
## Explanation ##
In this playbook, you'll be able to see a lot of Ansible Playbooks for a lot of different use cases.

I designed them to work seamlessly with SemaphoreUI, an RHAAP (Red Hat Ansible Automation Platform) alternative.

That's why in most of the playbook, the host is set to all since the correct Inventory can be added in SemaphoreUI within seconds.

## Branches ##
At the moment, there are two branches.
The **master** branch contains tested and production ready playbooks.

On the **development** branch, I push Playbooks that might not be finished yet.

They are still in the testing phase and should only be used **at your own risk**.

## Goal of this Repository ##
If you're in IT like me, you know that **automation is key**.

I try to automate every task that is repeditive or complicated to reduce time waste and user errors.

For example, the archinstall playbook, which currently revieves a complete overhaul as seen [here](https://codeberg.org/Spoljarevic/Ansible/issues/2), saved me around 5 to 7 hours of manually doing post-installation on my Arch Linux OS.
After this overhaul, it's supposed to save even more time.

So as you can see, these are not just for playing around, but for real world use cases.

## MIT License ##
This Repository is released under the MIT License, which can be viewed [here](https://codeberg.org/Spoljarevic/Ansible/src/branch/master/LICENCE.MIT).

What that means is basically that you can do whatever you want with what's in here, including selling it, as long as you include the copyright notice.
