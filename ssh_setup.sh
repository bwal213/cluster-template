ssh-keyscan -H 192.168.1.1 >> ~/.ssh/known_hosts
ssh 192.168.1.1
exit
ssh-keyscan -H 192.168.1.2 >> ~/.ssh/known_hosts
ssh 192.168.1.2
exit
ssh-keyscan -H 192.168.1.3 >> ~/.ssh/known_hosts
ssh 192.168.1.3
exit
ssh-keyscan -H 192.168.1.4 >> ~/.ssh/known_hosts
ssh 192.168.1.4
exit
ssh-keyscan -H 192.168.1.5 >> ~/.ssh/known_hosts
ssh 192.168.1.5
exit
ssh-keyscan -H 192.168.1.6 >> ~/.ssh/known_hosts
ssh 192.168.1.6
exit
