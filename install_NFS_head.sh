sudo yum -y install nfs-utils
sudo mkdir /software
sudo chmod -R 755 /software
sudo chown nfsnobody:nfsnobody /software
sudo echo '/software *(ro,sync,no_root_squash)' | sudo tee /etc/exports
sudo mkdir -p /scratch
sudo exportfs -ra
sleep 180s && sudo mount -t nfs 192.168.1.3:/scratch /scratch
sudo echo "192.168.1.3:/scratch /scratch  nfs defaults 0 0" | sudo tee -a /etc/fstab
