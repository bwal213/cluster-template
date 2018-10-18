import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext

# Describe the parameter(s) this profile script can accept.
portal.context.defineParameter( "n", "Number of VMs", portal.ParameterType.INTEGER, 15 )
#portal.context.defineParameter( "os", "disk image", portal.ParameterType.DISK_IMAGE, "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD")

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Check parameter validity.
if params.n < 4 or params.n > 16:
    portal.context.reportError( portal.ParameterError( "You must choose at least 4 and no more than 15 VMs." ) )

link = request.LAN("lan")
    
for i in range( params.n ):
    
  if i == 0:
    node = request.XenVM("head")
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/setup_firewall.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/setup_firewall.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/install_NFS_head.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/install_NFS_head.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/install_mpi.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/install_mpi.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/ssh_setup.sh"))
    node.addService(pg.Execute(shell="sh", command="sleep 5m && sudo -H -u BW840606 bash -c '/local/repository/ssh_setup.sh'"))
    node.addService(pg.Execute(shell="sh", command="sudo su BW840606 -c 'cp /local/repository/source/* /scratch/'"))
    node.routable_control_ip = "true"
  elif i == 1:
    node = request.XenVM("metadata")
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/ssh_setup.sh"))
    node.addService(pg.Execute(shell="sh", command="sleep 5m && sudo -H -u BW840606 bash -c '/local/repository/ssh_setup.sh'"))
  elif i == 2:
    node = request.XenVM("storage")
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/setup_firewall.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/setup_firewall.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/install_NFS_storage.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/install_NFS_storage.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/ssh_setup.sh"))
    node.addService(pg.Execute(shell="sh", command="sleep 5m && sudo -H -u BW840606 bash -c '/local/repository/ssh_setup.sh'"))
    #node.addService(pg.Execute(shell="sh", command="sudo su BW840606 -c 'cp /local/repository/source/* /users/BW840606'"))
  else:
    node = request.XenVM("compute-" + str(i-2))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/install_NFS_client.sh"))
    node.addService(pg.Execute(shell="sh", command="sleep 3m && sudo /local/repository/install_NFS_client.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/install_NFS_head.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/install_NFS_head.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/source_client.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/source_client.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo /local/repository/passwordless.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/ssh_setup.sh"))
    node.addService(pg.Execute(shell="sh", command="sleep 5m && sudo -H -u BW840606 bash -c '/local/repository/ssh_setup.sh'"))
    #node.addService(pg.Execute(shell="sh", command="sudo su BW840606 -c 'cp /local/repository/source/* /users/BW840606'"))
    node.cores = 2
    node.ram = 4096
    
  node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
    
  iface = node.addInterface("if1")
    
    # Specify the component id and the IPv4 address
  iface.component_id = "eth1"
  iface.addAddress(pg.IPv4Address("192.168.1." + str( i + 1 ), "255.255.255.0"))

  link.addInterface(iface)
  
portal.context.printRequestRSpec()
