# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
BOX_TIMEOUT = 180

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  N = 20
  (1..N).each do |machine_id|
    config.vm.define "machine#{machine_id}" do |config|
      config.vm.box = "dummy"
      config.vm.hostname = "machine#{machine_id}"
      config.vm.boot_timeout = BOX_TIMEOUT

      config.vm.provider :aws do |aws, override|
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = ENV['AWS_KEYPATH']
        override.ssh.forward_agent = true

        aws.access_key_id = ENV['AWS_KEY']
        aws.secret_access_key = ENV['AWS_SECRET']
        aws.keypair_name = ENV['AWS_KEYNAME']
        aws.security_groups = ENV['AWS_SECURITY_GROUP']
        aws.ami = "ami-bb156ad1"
        aws.region = "us-east-1"
        aws.instance_type = "t2.micro"
        aws.elastic_ip = false

        aws.tags = {'Name' => "machine#{machine_id}"}
      end
    end

    if machine_id == N
      config.vm.provision "ansible" do |ansible|
        ansible.extra_vars = {
          app_name: "ops",
          dotname: "dotfiles",
          settings_dir: "local",
          default_user: "ubuntu",
          password: "",
        }
        ansible.limit = "all"
        ansible.playbook = "development.yml"
        ansible.verbose = "vvvv"
      end
    end
  end
end
