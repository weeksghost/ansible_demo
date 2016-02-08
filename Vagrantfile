# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
BOX_TIMEOUT = 180

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    N = 2
    (1..N).each do |machine_id|
      config.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
      config.vm.define "machine_id#{machine_id}" do |local|
        local.vm.define "machine_id1", primary: true
        local.vm.box = "ubuntu/trusty64"
        local.vm.hostname = "loadtest"
        local.vm.boot_timeout = BOX_TIMEOUT

        local.vm.provider "virtualbox" do |virtualbox|
        virtualbox.name = "machine_id#{machine_id}"
        virtualbox.memory = 2048
        virtualbox.cpus = 2
      end

      if machine_id == N
        local.vm.provision "ansible" do |ansible|
          ansible.extra_vars = {
              app_name: "loadtest",
              dotname: "dotfiles",
              settings_dir: "local",
              default_user: "vagrant",
              password: "",
            }
          ansible.limit = "all"
          ansible.playbook = "development.yml"
          #ansible.verbose = "vvvv"
        end
      end
    end
  end
end

# Code below brings up multiple ec2 instances, provided you got the cred

#    N = 2
#    (1..N).each do |machine_id|
#      config.vm.define "machine#{machine_id}" do |cloud|
#        cloud.vm.box = "dummy"
#        cloud.vm.hostname = "machine#{machine_id}"
#        cloud.vm.boot_timeout = BOX_TIMEOUT
#
#        cloud.vm.provider :aws do |aws, override|
#        override.ssh.username = "ubuntu"
#        override.ssh.private_key_path = ENV['AWS_KEYPATH']
#        override.ssh.forward_agent = true
#        aws.access_key_id = ENV['AWS_KEY']
#        aws.secret_access_key = ENV['AWS_SECRET']
#        aws.keypair_name = ENV['AWS_KEYNAME']
#        aws.security_groups = ENV['AWS_SECURITY_GROUP']
#        aws.ami = "ami-bb156ad1"
#        aws.region = "us-east-1"
#        aws.instance_type = "t2.micro"
#        aws.elastic_ip = false
#        aws.tags = {'Name' => "machine#{machine_id}"}
#      end
#
#      if machine_id == N
#        cloud.vm.provision "ansible" do |ansible|
#          ansible.extra_vars = {
#             app_name: "ops",
#             dotname: "dotfiles",
#             settings_dir: "local",
#             default_user: "ubuntu",
#             password: "",
#          }
#          ansible.limit = "all"
#          ansible.playbook = "development.yml"
#          ansible.verbose = "vvvv"
#        end
#      end
#    end
#  end
#end
