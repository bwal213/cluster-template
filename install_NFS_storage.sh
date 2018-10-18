sudo yum -y install nfs-utils
sudo mkdir /scratch
sudo chmod 777 /scratch
sudo chown nfsnobody:nfsnobody /scratch
#sudo exportfs -p /mnt/scratch 192.168.1.*(rw,sync,no_root_squash) 
#sudo exportfs *:/mnt/software -o rw,sync,no_root_squash
sudo echo '/scratch *(rw,sync,no_root_squash)' | sudo tee /etc/exports
sudo exportfs -ra
