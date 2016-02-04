# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :ec2 do |x|
    x.vm.box = "ubuntu/trusty64"
    x.vm.hostname = "grid"
    x.vm.boot_timeout = 120

    x.vm.provider :virtualbox do |v|
      v.name = "grid"
    end

    x.vm.provider :aws do |aws, override|
      aws.access_key_id = ENV['AWS_KEY']
      aws.secret_access_key = ENV['AWS_SECRET']
      aws.keypair_name = ENV['AWS_KEYNAME']
      aws.security_groups = ENV['AWS_SECURITY_GROUP']
      aws.ami = "ami-bb156ad1"
      aws.region = "us-east-1"
      aws.instance_type = "t2.micro"

      aws.tags = {
        'Name' => 'grid'
      }

      override.vm.box = "dummy.box"
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = ENV['AWS_KEYPATH']
    end
  end

  config.vm.provision "ansible" do |ansible|

    ansible.extra_vars = {

      app_name: "jenkins",
      dotname: "dotfiles",
      settings_dir: "local",
      default_user: "ubuntu",
      password: "",
    }

    ansible.playbook = "development.yml"
    ansible.verbose = "vvvv"
  end
end
