# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :vagrant do |x|
    x.vm.box = "ubuntu/trusty64"
    x.vm.hostname = "myvagrant"
    x.vm.boot_timeout = 120

    x.vm.provider :virtualbox do |v|
      v.name = "myvagrant"
    end

    x.vm.provider :aws do |aws, override|
      aws.access_key_id = ENV['AWS_KEY']
      aws.secret_access_key = ENV['AWS_SECRET']
      aws.keypair_name = ENV['AWS_KEYNAME']
      aws.security_groups = ENV['AWS_SECURITY_GROUP']
      aws.ami = "ami-64e27e0c"
      aws.region = "us-east-1"
      aws.instance_type = "t1.micro"

      aws.tags = {
        'Name' => 'Vagrant'
      }

      override.vm.box = "dummy"
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = ENV['AWS_KEYPATH']
    end
  end


  config.vm.provision "ansible" do |ansible|

    ansible.extra_vars = {

      app_name: "djangoproject",
      dotname: "dotfiles",
      settings_dir: "prod",
      default_user: "ubuntu",
      password: "",
      db_passwd: ENV['DB_PASS'],

      }

    ansible.playbook = "development.yml"
    ansible.verbose = "vvvv"
  end
end
