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

.. NOTE::
  To align, the name of the topology file needs to be define inside the inventory file

.. code-block:: text

    # Generate configurations for the sample-topology
    ansible-playbook -i hosts.ini pb.conf.all.yaml

    # Generate configurations for your own topology
    ansible-playbook -i mytopology.ini pb.conf.all.yaml

It's easy to create your own inventory and topology files to adapt device IP, type and interface names to your environment assuming you have the same base design.

1/ Create your inventory file
-----------------------------

The inventory file contains a lot of information and variables but most importantely
it define the parsonnality of each device depending on which groups a device belong to.

Different playbooks will be executed for each groups, and each playbook will generate a different part of the configuration.

All devices in the group ``spine-mx`` will get their configuration from these group
- common
- underlay-ebgp
- overlay-evpn-mx-l3
- build-config

All devices in the group ``leaf-qfx-l3`` will get their configuration from these group
- common
- underlay-ebgp
- overlay-evpn-qfx-l3
- overlay-evpn-access
- build-config

The complete list of role per group is available in the playbook ``pb.conf.all.yaml``

**Unique ID**
Each device in the inventory file needs to have a unique ID define inside the variable ``id``.
This ID is used to automatically generate:
- Loopback address
- ASN number

2/ Create your own topology file
--------------------------------

To properly generate the configuration, it's important to define all information related to your topology in this file:
Interface names, dns, login, static route etc ...

Please refer to the documentation of role ``generated-underlay-ebgp`` to understand how to define
in the topology file the information that will be used to generate the underlay

.. NOTE::
  if you define ``vqfx: true`` in the inventory file, DHCP will be automatically configured on the management interface.

3/ Define your IP address plan
------------------------------

You can define your own IP address plan and automatically regenerate all variables by using the playbook
``pb.generate.variables.yaml``.

All information can be defined inside the playbook itself in the ``vars:`` section.
