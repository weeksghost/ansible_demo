ansible_demo
============

Provision an Ubuntu instance accessible via ssh using Ansible

Instructions
---

1. Make sure your host is listed in the file named local at the root of the project or name your host in the playbook command.

2. Test using the following command

    `ansible all -i local -m ping`

3. Run the playbook using:

    `ansible-playbook -i <HOST> -v development.yml --extra-vars "app_name=<APPNAME> default_user=<USERNAME> db_passwd=<PASSWORD>"`
