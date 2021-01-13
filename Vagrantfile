Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.network :forwarded_port, guest: 12345, host: 22345
  # config.vm.provision :shell, path: "bootstrap.sh"
end
