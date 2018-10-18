sudo yum -y install nfs-utils
sudo mkdir -p /software
sudo mkdir -p /scratch
sudo mount -t nfs 192.168.1.1:/software /software
sudo mount -t nfs 192.168.1.3:/scratch /scratch
sudo echo "192.168.1.1:/software /software  nfs defaults 0 0" | sudo tee -a /etc/fstab
sudo echo "192.168.1.3:/scratch /scratch  nfs defaults 0 0" | sudo tee -a /etc/fstab
