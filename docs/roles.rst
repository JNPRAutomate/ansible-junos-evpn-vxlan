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

.. _generate-tenant-vni: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/generate-tenant-vni
.. _generate-p2p-ips: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/generate-p2p-ips
.. _generate-underlay-bgp: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/generate-underlay-bgp

.. _underlay-ebgp: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/underlay-ebgp
.. _underlay-ospf: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/underlay-ospf
.. _underlay-ospf-unnumbered: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/underlay-ospf-unnumbered

.. _overlay-evpn-qfx-l3: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/overlay-evpn-qfx-l3
.. _overlay-evpn-qfx-l2: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/overlay-evpn-qfx-l2
.. _overlay-evpn-mx-l3: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/overlay-evpn-mx-l3
.. _overlay-evpn-access: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/overlay-evpn-access

.. _common: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/common/
.. _build-config: https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan/tree/master/roles/build-config

Roles to create the underlay configuration
------------------------------------------

There are 3 different roles to create an underlay network, only one is needed and all devices must have the same.

========================= ==========================================================================
Role                      Description
========================= ==========================================================================
underlay-ebgp_            Create an Underlay with eBGP with p2p /31 network and 1 ASN per device
underlay-ospf_            Create an Underlay with OSPF with p2p /31 network and 1 Area
underlay-ospf-unnumbered_ Create an Underlay with OSPF with p2p unnumbered interface and 1 Area
========================= ==========================================================================

Roles to create the overlay configuration (EVPN)
------------------------------------------------

These roles are complementary and are designed to work together.
Each one is specific to a role in the architecture and is specific to device capabilities:

===================== =====================================================================================================================
Role                   Description
===================== =====================================================================================================================
overlay-evpn-qfx-l3_  Create iBGP & EVPN configuration for QFX devices that  support both L2 & L3 VTEP (QFX10000 today)
overlay-evpn-qfx-l2_  Create iBGP & EVPN configuration for QFX devices that only support L2 VTEP (QFX5100/QFX5200)
overlay-evpn-mx-l3_   Create iBGP & EVPN configuration for MX devices that only support L2 & L3 VTEP (MX)
overlay-evpn-access_  Create access ports configuration to maps existing resources into the overlay (Trunk/LAG/ESI/Vlan mapping)
===================== =====================================================================================================================

Roles to generate variables (IPs, vlan)
----------------------------------------
====================== =========================================================
Role                   Description
====================== =========================================================
generate-tenant-vni_   Generate variables files to scale Tenant and VNI
generate-p2p-ips_      Generate network and ip addresses for P2P links
generate-underlay-bgp_ Generate ebgp underlay input variables
====================== =========================================================

Other Roles
-----------
=============== =========================================================
Role            Description
=============== =========================================================
common_         Generate base configuration
build-config_   Assemble all configuration snippet from other roles
=============== =========================================================
