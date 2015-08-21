# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.network "public_network", bridge: 'en1: Wi-Fi (Airport)'

  config.vm.define :vagrant do |x|
    x.vm.box = "ubuntu/trusty64"
    x.vm.hostname = "myvagrant"
    x.vm.boot_timeout = 120

    x.vm.provider :virtualbox do |v|
      v.name = "myvagrant"
      v.memory = 2048
      v.cpus = 2
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
