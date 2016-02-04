# -*- mode: ruby -*-
# vi: set ft=ruby :

boxes = [
  {
    :name           =>  'instance-01',
    :primary        =>  'true',
    :instance_type  =>  't2.micro',
    :elastic_ip     =>  false
  },
]

VAGRANTFILE_API_VERSION = "2"
BOX_TIMEOUT = 180

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  boxes.each do |box|
    config.vm.define box[:name], primary: box[:primary] do |config|
      config.vm.box = "dummy"
      config.vm.hostname = box[:name]
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
        aws.instance_type = box[:instance_type]
        aws.elastic_ip = box[:elastic_ip]

        aws.tags = {'Name' => box[:name]}
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
end
