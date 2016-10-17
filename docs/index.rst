.. Ansible EVPN/VXLAN documentation master file, created by
   sphinx-quickstart on Thu Oct 13 21:17:00 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Ansible EVPN/VXLAN's documentation!
==============================================

Sample project using Ansible and Jinja2 template to generate configurations and manage Juniper devices deployed in EVPN/VXLAN Fabric mode.

In this project you'll find:
- (1) **Sample project for ansible** with Playbooks and variables to generate EVPN/VXLAN configuration for multi-pod EVPN/Fabric in a multi-tenants environment.
- (2) **[Examples of configuration](config)** EVPN/VXLAN for QFX5k, QFX10k & MX.
- (3) Severals **Jinja2 templates**, packaged and documented into [Ansible roles](roles) that can be **reuse in other Ansible projects** to easily generate Overlay & Underlay configuration.
- (4) **Playbook to check the health** of an EVPN/VXLAN Fabric.

Contents:

.. toctree::
   :maxdepth: 2

   sample_topology
   roles
   playbooks
   topology_independant
   build_your_own


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
