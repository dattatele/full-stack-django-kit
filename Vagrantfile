# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  # Web server
  config.vm.define "web", primary: true do |web|
    web.vm.box = "ubuntu/trusty64"

    web.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"
    web.vm.network "forwarded_port", guest: 443, host: 8443
    web.vm.network "forwarded_port", guest: 80, host: 8080
    web.vm.network "private_network", ip: "192.168.10.10"

    web.vm.provision "ansible" do |ansible|
      ansible.sudo = true
      ansible.inventory_path = "ansible/inventory/vagrant/web.ini"
      ansible.playbook = "ansible/webservers.yml"
      ansible.verbose = "v"
      ansible.limit = "webservers"
      ansible.extra_vars = {
          django_settings_module: "mysite.settings.vagrant",
          enable_docs: true
      }

    end
  end

  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/trusty64"
    db.vm.network "forwarded_port", guest: 22, host: 2200, id: "ssh"
    db.vm.network "private_network", ip: "192.168.10.11"

    db.vm.provision "ansible" do |ansible|
       ansible.sudo = true
       ansible.inventory_path = "ansible/inventory/vagrant/db.ini"
       ansible.playbook = "ansible/dbservers.yml"
       ansible.limit = "databases"
       ansible.verbose = "v"
    end
  end

  config.vm.define "ci" do |ci|
    ci.vm.box = "ubuntu/trusty64"
    ci.vm.network "forwarded_port", guest: 8153, host: 8153
    ci.vm.network "forwarded_port", guest: 22, host: 2201, id: "ssh"
    ci.vm.network "private_network", ip: "192.168.10.12"
    ci.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"]
    end

    ci.vm.provision "ansible" do |ansible|
         ansible.sudo = true
         ansible.inventory_path = "ansible/inventory/vagrant/ci.ini"
         ansible.playbook = "ansible/ciservers.yml"
         ansible.limit = "ciservers"
         ansible.verbose = "v"
      end
    end


end
