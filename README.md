ansible_demo
============

Provision an AWS EC2 instance (Ubuntu) using Ansible and Vagrant

Prerequisites:
---

- [VirtualBox](https://www.virtualbox.org/)

- [VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads)

- [Vagrant](https://www.vagrantup.com/)

- [Ansible](http://docs.ansible.com/index.html)

- Git repo

- Vagrant aws plugin

- AWS credentials

Instructions:
---

Make sure your AWS credentials are located in an aws [centralized credential](http://blogs.aws.amazon.com/security/post/Tx3D6U6WSFGOK2H/A-New-and-Standardized-Way-to-Manage-Credentials-in-the-AWS-SDKs) file.

**For example:**

```
echo "[default]\n\
aws_access_key_id = XXXXXXXXXXXXXXX\n\
aws_secret_access_key = XXXXXXXXXXXXXXX" \
>  ~/.aws/credentials
```

Up and running:
---

1) brew update

2) brew install ansible

3) Install or update [VirtualBox](http://download.virtualbox.org/virtualbox/4.3.26/VirtualBox-4.3.26-98988-OSX.dmg), [VirtualBox Extension Pack](http://download.virtualbox.org/virtualbox/4.2.28/Oracle_VM_VirtualBox_Extension_Pack-4.2.28-97679.vbox-extpack) & [Vagrant](https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.2.dmg)

4) Download the git repo: git@github.com:weeksghost/ansible_demo.git

5) Checkout branch "aws_vagrant"

6) Run `Vagrant Up`


### WARNING

If all is working, you will have spun up an EC2 micro instance and it will cost money if you leave it running.

Use the commands to make sure this instance is not running:

`Vagrant halt`

`Vagrant destroy`
