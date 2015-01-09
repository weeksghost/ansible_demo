# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  #config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "vagrant"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.

  #config.vm.network "public_network", bridge: 'en0: Ethernet'

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  #config.ssh.username = ENV['USER']

  #config.ssh.private_key_path = ['~/.vagrant.d/insecure_private_key', '~/.ssh/id_rsa']
  #config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true

  #config.vm.provision "ansible" do |ansible|

  #  ansible.extra_vars = {

  #    app_name: "djangoproject",
  #    dotname: "dotfiles",
  #    settings_dir: ENV['USER'],
  #    default_user: ENV['USER'],
  #    password: "",
  #    db_passwd: "Fukst1k",

  #    }

  #  ansible.playbook = "development.yml"
  #  ansible.verbose = "vvvv"

  #end

Vagrant.configure("2") do |config|

  config.vm.box = "aws-precise-32"
  config.vm.hostname = "brooklyndelta.com"
  config.vm.boot_timeout = 120

  end

  config.vm.provider :aws do |aws, override|

    aws.access_key_id = "AKIAICXCV3KLYXQDSO2Q"
    aws.secret_access_key = "1SVe8sOBu0rJnSI/svWbtWWgRh+cPqhkfCdTk2x"
    aws.ami = "ami-4ceaed4d"
    aws.keypair_name = "bdelta"
    aws.security_groups = ["default", "sg-0033e065"]
    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "~/.keys/bdelta.pem"

  end

  config.vm.provision "ansible" do |ansible|

    ansible.extra_vars = {

      app_name: "djangoproject",
      dotname: "dotfiles",
      settings_dir: ENV['USER'],
      default_user: ENV['USER'],
      password: "",
      db_passwd: "Fukst1k",

      }

    ansible.playbook = "development.yml"
    ansible.verbose = "vvvv"

  end

  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
  #   vb.customize ["modifyvm", :id, "--memory", "1024"]
  # end
  #
  # View the documentation for the provider you're using for more
  # information on available options.

  #config.vm.provider :virtualbox do |vb|
  #  vb.customize ["modifyvm", :id, "--name", "bwy-local-dev", "--memory", "2048"]
  #end

  # Enable provisioning with CFEngine. CFEngine Community packages are
  # automatically installed. For example, configure the host as a
  # policy server and optionally a policy file to run:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.am_policy_hub = true
  #   # cf.run_file = "motd.cf"
  # end
  #
  # You can also configure and bootstrap a client to an existing
  # policy server:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.policy_server_address = "10.0.2.15"
  # end

  # Enable provisioning with Puppet stand alone.  Puppet manifests
  # are contained in a directory path relative to this Vagrantfile.
  # You will need to create the manifests directory and a manifest in
  # the file default.pp in the manifests_path directory.
  #
  # config.vm.provision "puppet" do |puppet|
  #   puppet.manifests_path = "manifests"
  #   puppet.manifest_file  = "site.pp"
  # end

  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.
  #
  # config.vm.provision "chef_solo" do |chef|
  #   chef.cookbooks_path = "../my-recipes/cookbooks"
  #   chef.roles_path = "../my-recipes/roles"
  #   chef.data_bags_path = "../my-recipes/data_bags"
  #   chef.add_recipe "mysql"
  #   chef.add_role "web"
  #
  #   # You may also specify custom JSON attributes:
  #   chef.json = { mysql_password: "foo" }
  # end

  # Enable provisioning with chef server, specifying the chef server URL,
  # and the path to the validation key (relative to this Vagrantfile).
  #
  # The Opscode Platform uses HTTPS. Substitute your organization for
  # ORGNAME in the URL and validation key.
  #
  # If you have your own Chef Server, use the appropriate URL, which may be
  # HTTP instead of HTTPS depending on your configuration. Also change the
  # validation key to validation.pem.
  #
  # config.vm.provision "chef_client" do |chef|
  #   chef.chef_server_url = "https://api.opscode.com/organizations/ORGNAME"
  #   chef.validation_key_path = "ORGNAME-validator.pem"
  # end
  #
  # If you're using the Opscode platform, your validator client is
  # ORGNAME-validator, replacing ORGNAME with your organization name.
  #
  # If you have your own Chef Server, the default validation client name is
  # chef-validator, unless you changed the configuration.
  #
  #   chef.validation_client_name = "ORGNAME-validator"
end
