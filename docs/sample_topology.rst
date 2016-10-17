Sample Ansible project to generate EVPN/VXLAN configuration
===========================================================

![sample topology](sample-topology-diagram.png?raw=true)

This project is simulating the creation of a 2 pods EVPN/VXLAN Fabric, POD1 & POD2:
 - Each POD is composed of 2 spine and 2 leaf
 - PODs are interconnected with 2 qfx5100 acting as Fabric, these are not running EVPN
**On POD1**
 - Spine are QFX10K and leaf are QFX5000
 - Leaf are configured with Vlan normalization on their access ports facing servers
**On POD2**
 - Spine are MX480 and leaf are QFX5000
 - Leaf are configured with standard trunk interface facing servers,
 - 1 server is dual-attached to both leaf using EVPN/ESI and LACP

All devices names, Ip addresses loopback addresses etc .. are defined in the [inventory file named hosts.ini](hosts.ini).
All physical connections are defined in the [topology file under group_vars/all](group_vars/all/topology.yaml).

Regenerate configurations
-------------------------

Even without real devices, it's possible to regenerate configurations for all devices using ansible playbooks provided with the project

To verify that Ansible & Ansible Junos module for Ansible are properly installed, you can try to regenerate all configs with this command:

.. code-block:: text

    ansible-playbook pb.conf.all.yaml


> By default, all configurations generated will be stored under the directory `config/` and will replace existing > configuration store there

## Scale configurations

The project come with some a solution to easily change the scale of the setup, it's possible to :
 - Change the number of tenants
 - Change the number of VNI per tenants

To scale the configuration, you need to change some input parameters in the file `group_vars/all/tenant_vni.yaml`
*Please refer to instructions in [generate-tenant-vni role](roles/generate-tenant-vni)*

Once the input file is modified, you need to regenerate variables first and them regenerate configurations.

.. code-block:: text

    ansible-playbook pb.generate.variables.yaml
    ansible-playbook pb.conf.all.yaml

**Other Available Playbooks**

All playbooks are stored at the root of the project and are named `pb.*.yaml`

.. code-block:: yaml

    pb.save.config.yaml               # Download configuration for all devices and save them locally

    pb.conf.all.yaml                  # Generate and assemble configuration for all devices
    pb.conf.all.commit.yaml           # Generate, assemble, push and commit configuration to all devices

    pb.conf.fabric.yaml               # Generate configuration for group 'fabric'
    pb.conf.leaf.qfx.l2.yaml          # Generate configuration for group 'leaf-qfx-l3'
    pb.conf.leaf.qfx.l3.yaml          # Generate configuration for group 'leaf-qfx-l3'
    pb.conf.spine.mx.yaml             # Generate configuration for group 'spines-mx'
    pb.conf.spine.qfx.yaml            # Generate configuration for group 'spines-qfx'

    pb.init.make_clean.yaml           # Create temp directory for all devices

    pb.generate.variables.yaml        # Regenerate variables files for p2p links, Tenants and VNI

    pb.check.connectivity.yaml        # Check if all devices are reachable via Netconf
    pb.check.underlay.yaml            # Check the heath of the underlay
    pb.check.overlay.yaml             # Check the health of the overlay

    # This project has been updated to use the new Junos modules available in Ansible 2.1
    # Some playbooks are also provided with the Junipe.junos modules available in Ansible Galaxy.
    pb.conf.all.commit.galaxy.yaml    # Generate, assemble, push and commit configuration to all devices
                                      # using the Junos modules provided in Ansible Galaxy
