# Ansible Junos Configuration for EVPN/VXLAN

Sample project using Ansible and Jinja2 template to generate configurations and manage Juniper devices deployed in EVPN/VXLAN Fabric mode.

In this project you'll find:
- (1) **Sample project for ansible** with Playbooks and variables to generate EVPN/VXLAN configuration for multi-pod EVPN/Fabric in a multi-tenants environment.
- (2) **[Examples of configuration](config)** EVPN/VXLAN for QFX5k, QFX10k & MX.
- (3) Severals **Jinja2 templates**, packaged and documented into [Ansible roles](roles) that can be **reuse in other Ansible projects** to easily generate Overlay & Underlay configuration.
- (4) **Playbook to check the health** of an EVPN/VXLAN Fabric.

# Info on EVPN/VXLAN

White Paper on EVPN/VXLAN available on Juniper.net
http://www.juniper.net/assets/us/en/local/pdf/whitepapers/2000606-en.pdf

# Documentation

The [complete documentation is available here](http://ansible-junos-evpn-vxlan.readthedocs.io/en/latest/index.html)

# Examples of configuration

All [examples of configuration](config) are available in the config directory:
Here are some links to specific features:
- [EVPN/VXLAN configuration for QFX5100 (L2)](config/leaf-02.conf)
- [EVPN/VXLAN Configuration for QFX10000 (L2/L3)](config/spine-01.conf)
- [EVPN/VXLAN Configuration for MX](config/spine-03.conf)
- [eBGP Fabric only configuration](config/fabric-01.conf)
- [Vlan Normalization configuration on access ports](config/leaf-01.conf)
- Active/Active LAG between 2 devices using ESI. [Switch1](config/leaf-03.conf)/[Switch2](config/leaf-04.conf)

# Contributing

Please refer to the file [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

# Requirements
 - Ansible
 - [juniper.junos module for Ansible](https://github.com/Juniper/ansible-junos-stdlib) (min 1.2.2)
 - [junos-eznc](https://github.com/Juniper/py-junos-eznc)
