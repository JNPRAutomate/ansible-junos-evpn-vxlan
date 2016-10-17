Templates and Roles used to generate configuration
==================================================

All configurations are generated using Jinja2 templates and variables.
To simplificy the management of these templates and make them reusable in other projects, these templates have been pacakges into several roles, each one is generating a part of the final configuration.

All roles are located under the directory [roles](roles) and are organized as follow

.. code-block:: text

    ├ underlay-ebgp           # Name of the role
      ├── README.md           # Documentation and Instructions to reuse
      ├── meta
      │   └── main.yaml       # Indicate author of the project and dependancies
      ├── defaults
      │   └── main.yaml       # Default variables, can be overwritten for each device
      ├── tasks
      │   └── main.yaml       # Action to execute when calling this Roles
      └── templates
          └── main.conf.j2    # Jinja2 Templates, in most cases, used to generate configuration


Below the list of roles available, classified per function, with a short description and a link to their respective documentation.

Roles to create the underlay configuration
------------------------------------------

There are 3 different roles to create an underlay network, only one is needed and all devices must have the same.
 - _underlay-ebgp role (default)  # Create an Underlay with eBGP with p2p /31 network and 1 ASN per device
 - _underlay-ospf role  # Create an Underlay with OSPF with p2p /31 network and 1 Area
 - _underlay-ospf-unnumbered role # Create an Underlay with OSPF with p2p unnumbered interface and 1 Area

.. _underlay-ebgp: roles/underlay-ebgp
.. _underlay-ospf: roles/underlay-ospf
.. _underlay-ospf-unnumbered: roles/underlay-ospf-unnumbered


Roles to create the overlay configuration (EVPN)
------------------------------------------------

These roles are complementary and are designed to work together.
Each one is specific to a role in the architecture and is specific to device capabilities:
 - ['overlay-evpn-qfx-l3' role](roles/overlay-evpn-qfx-l3)  # Create iBGP & EVPN configuration for QFX devices that  support both L2 & L3 VTEP (QFX10000 today)
 - ['overlay-evpn-qfx-l2' role](roles/overlay-evpn-qfx-l2)  # Create iBGP & EVPN configuration for QFX devices that only support L2 VTEP (QFX5100/QFX5200)
 - ['overlay-evpn-mx-l3' role](roles/overlay-evpn-mx-l3)    # Create iBGP & EVPN configuration for MX devices that only support L2 & L3 VTEP (MX)
 - ['overlay-evpn-access' role](roles/overlay-evpn-access)  # Create access ports configuration to maps existing resources into the overlay (Trunk/LAG/ESI/Vlan mapping)

Roles to generate variables (IPs, vlan )
----------------------------------------

Other Roles
-----------
 - ['common' role](roles/common/)         # Generate base configuration
 - ['build-config' role](roles/build-config)  # Assemble all configuration snippet from other roles
 - ['generate-tenant-vni' role](roles/generate-tenant-vni)   # Generate variables files to scale Tenant and VNI
 - ['generate-p2p-ips' role](roles/generate-p2p=ips)   # Generate network and ip addresses for P2P links
