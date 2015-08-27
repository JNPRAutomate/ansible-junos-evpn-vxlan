# Ansible Junos Configuration for EVPN/VXLAN
Sample project using Ansible and Jinja2 tempalte to automatically generate configurations for Juniper devices deploy in EVPN/VXLAN fabric mode

** Still work in progress // Configurations are not 100% valid yet **

# Info on EVPN/VXLAN

<add brief description>

White Paper on EVPN/VXLAN available on Juniper.net
http://www.juniper.net/assets/us/en/local/pdf/whitepapers/2000606-en.pdf

# How to Start
 - Define your inventory file [hosts](https://github.com/dgarros/ansible-junos-evpn/blob/master/hosts)
 - Adapt common variable in group_vars/all/common.yaml to match your environment
 - Adapt devices variables to match your environment
  - host_vars/*<device>*/main.yaml for management ip and loopback ip
  - host_vars/*<device>*/underlay.yaml Interface IP and underlay BGP information
  - host_vars/*<device>*/overlay.yaml Overlay BGP and VNI/Bridge domains information

**Generate and push configuration**

```
ansible-playbook -i hosts all.commit.p.yaml
```

**Available playbook**

```
make_clean.p.yaml               # Create temp directory for all devices
assemble_and_commit.p.yaml      # Assemble and commit configuration for all devices
all.commit.p.yaml               # Generate, assemble, push and commit configuration to all devices
all.p.yaml                      # Generate configuration parts to all devices
leaves.qfx.l2.p.yaml            # Generate configuration parts for leaf-qfx-l2 group
spines.mx.p.yaml                # Generate configuration parts for spines-mx group
spines.qfx.p.yaml               # Generate configuration parts for leaf-spine-qfx group
```

# Requirements
- Ansible
- juniper.junos module for Ansible

# Implementation detail

### Network configuration
 - The underlay is build using EBGP with one ASN per switch
 - The overlay is build using iBGP without RR and ingress replication

### Ansible
To provide flexibility in configuration different "configuration template" have
have been created and each is associated with a different roles

#### 'common' role
Generate the base configuration, non specific to the EVPN/VXLAN part :
 - Management Interface
 - Loopback Interface
 - Root password
 - timezone
 - Syslog
 - User
 - SNMP

Template can be found in [roles/common/templates/main.conf.j2 ](https://github.com/dgarros/ansible-junos-evpn/blob/master/roles/common/templates/main.conf.j2)

Using variable files from
 - [group_vars/all/common.yaml]((https://github.com/dgarros/ansible-junos-evpn/blob/master/group_vars/all/common.yaml)
- host_vars/*hostname*/main.yaml

#### 'underlay-ebgp' role
Generate the base configuration to build the underlay:
 - interfaces IP between spine and leaf
 - Underlay BGP configuration using EBGP
 - BFD for BGP on all interfaces
 - BGP policy options
 - ECMP across Spines

Template can be found in [roles/underlay-ebgp/templates/main.conf.j2 ](https://github.com/dgarros/ansible-junos-evpn/blob/master/roles/underlay-ebgp/templates/main.conf.j2)

Using variable files from :
 - [group_vars/all/underlay.yaml]((https://github.com/dgarros/ansible-junos-evpn/blob/master/group_vars/all/underlay.yaml)
 - host_vars/*hostname*/main.yaml
 - host_vars/*hostname*/underlay.yaml

#### 'overlay-evpn-access' role  
Generate configuration for access ports of the EVPN/VXLAN fabric
 - Aggregate interface, with or without ESI
 - Trunk interface

Template can be found in [roles/overlay-evpn-access/templates/main.conf.j2 ](https://github.com/dgarros/ansible-junos-evpn/blob/master/roles/overlay-evpn-access/templates/main.conf.j2)

Using variable files from :
 - host_vars/*hostname*/access.yaml

#### 'overlay-evpn-qfx-l2' role  
Generate configuration for EVPN/VXLAN for QFX in L2 mode (no rvi)
 - Overlay iBGP configuration
 - VNI/VLAN creation with associated policy options

Template can be found in [roles/overlay-evpn-qfx-l2/templates/main.conf.j2 ](https://github.com/dgarros/ansible-junos-evpn/blob/master/roles/overlay-evpn-qfx-l2/templates/main.conf.j2)

Using variable files from :
 - host_vars/*hostname*/main.yaml
 - host_vars/*hostname*/overlay.yaml

#### 'overlay-evpn-mx-l3' role
Generate configuration for EVPN/VXLAN for MX in L3 mode (rvi)
 - Overlay iBGP configuration
 - VNI/VLAN creation with associated policy options
 - RVI per VLAN/VNI

Template can be found in [roles/overlay-evpn-mx-l3/templates/main.conf.j2 ](https://github.com/dgarros/ansible-junos-evpn/blob/master/roles/overlay-evpn-mx-l3/templates/main.conf.j2)

Using variable files from :
 - host_vars/*hostname*/main.yaml
 - host_vars/*hostname*/overlay.yaml

#### 'overlay-evpn-qfx-l3' role  
 Not implemented yet
