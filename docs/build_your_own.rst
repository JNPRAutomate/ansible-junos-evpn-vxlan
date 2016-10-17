How to use this project on my own topology
==========================================

This project has been designed to be easily deploy on multiple topologies, physical or virtual.
As much as possible, all information related to a given topology (interface names, device names etc ..) are centralized in 2 files:

**The topology file [sample-topology.yaml]**, this file contains:
 - Information required to construct the base configuration (login, dns, ntp etc ..)
 - All physical interface names
 - Directories to use to generate the configuration

**The inventory file [hosts.ini]**, this file contains:
 - Device names
 - Device roles in the architecture (using ansible groups)
 - Management IP addresses and loopback
 - Login, password, management gateway etc ..
 - The name of the topology file

When you call an Ansible playbook, you can specify explicitly the inventory file by using the option `-i`

  To align, the name of the topology file needs to be define inside the inventory file

.. code-block:: text

    # Generate configurations for the sample-topology
    ansible-playbook -i hosts.ini pb.conf.all.yaml

    # Generate configurations for your own topology
    ansible-playbook -i mytopology.ini pb.conf.all.yaml


It's very easy to create your own inventory and topology files to adapt device IP, device type and interface names to your environment assuming you have the same base design.

  it's not recommended to change device names because all variables directories depend on the name

  It's also possible to generate your own design but it will require a little bit more customization.
  Documentation is not yet available on this part, Please open start a discussion on the issue tracker if you need help with that
