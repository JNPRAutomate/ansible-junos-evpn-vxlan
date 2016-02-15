# Documentation for all roles available in this playbook

### Network configuration
 - The underlay is build using eBGP with one ASN per switch
 - The overlay is build using iBGP with RR on MXs and ingress replication

### Konwn limitations
 - Route Target are not suported in YAML files. please, refers to the [following documentation](https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/documentation/static.md)

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

Template can be found in [roles/common/templates/main.conf.j2 ](https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/roles/common/templates/main.conf.j2)

Using variable files from
 -`[group_vars/all/common.yaml](https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/group_vars/all/common.yaml)
 - `host_vars/*hostname*/main.yaml`

Structure of the `main.yaml` file is based on the following structure:
```yaml
host: 
    management:
        ip: 	# IP to configure for management access
        mask: 	# Netmask
        gw: 	# Default Gateway
    loopback:
        ip: 	# IP address of the loopback
```

#### 'underlay-ebgp' role
Generate the base configuration to build the underlay:
 - interfaces IP between spine and leaf
 - Underlay BGP configuration using EBGP
 - BFD for BGP on all interfaces
 - BGP policy options
 - ECMP across Spines

Template can be found in [roles/underlay-ebgp/templates/main.conf.j2 ](https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/roles/underlay-ebgp/templates/main.conf.j2)

Using variable files from :
 - [group_vars/all/underlay.yaml](https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/group_vars/all/underlay.yaml)
 - `host_vars/*hostname*/main.yaml`
 - `host_vars/*hostname*/underlay.yaml`

Structure of the `underlay.yaml` file is based on the following structure:
```yaml
underlay:
    local:
        asn: 				# Local ASN configured for the underlay on the device
    neighbors:
      - interface:			# Interface connected to a remote peer in the IP Fabric
        name: 				# Hostname of the connected device (useful for comment)
        remote_interface: 	# Remote interface connected to our device
        asn:				# ASN of the remote device
        peer_ip:			# Directly connected IP address of the remote device (DO NOT USE LOOPBACK since it is IP fabric)
        local_ip:			# Local IP address configured on directly connected interface
      - interface:			# Interface connected to a remote peer in the IP Fabric
        name: 				# Hostname of the connected device (useful for comment)
        remote_interface: 	# Remote interface connected to our device
        asn:				# ASN of the remote device
        peer_ip:			# Directly connected IP address of the remote device (DO NOT USE LOOPBACK since it is IP fabric)
        local_ip:			# Local IP address configured on directly connected interface
```

#### 'overlay-evpn-access' role  
Generate configuration for access ports of the EVPN/VXLAN fabric
 - Aggregate interface, with or without ESI
 - Trunk interface

Template can be found in `[roles/overlay-evpn-access/templates/main.conf.j2 ]`(https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/roles/overlay-evpn-access/templates/main.conf.j2)

Using variable files from :
 - `host_vars/*hostname*/access.yaml`

Structure of the `access.yaml` file is based on the following structure. It support 3 different methods to connect customer devices to the EVPN fabric:
 - single homed
 - dual homed with LACP
 - dual homed without LACP

YAML Structure:
```yaml
access:
    interfaces:
    	# Single homed attachment
        et-0/0/5:			# Interface name. Interface connected to the customer device
            mode: 			# Interface mode. Must be trunk or aggregate
            vlans: 			# List of vlan-id to configure on this interface. Structure is [ 100, 101, 102]
            description:	# Interface description
        
        # Dual homed attachment with LACP
        ae0:
            mode: 			# Interface mode. Must be trunk
            vlans: 			# List of vlan-id to configure on this interface. Structure is [ 100, 101, 102]
            description:	# Interface description
            esi: 			# ESI value configured manually
            lacp_system_id: # LACP ID configured on both leaves. It must be the same to emulate a normal LACP LAG
            lacp_mode: 		# LACP mode (active|passive)
        et-0/0/4:
            mode: 			# Interface mode. Must be aggregate
            parent:			# Aggregated interface (aeX)
            description: 	# Interface description
        
		# Dual homed attachment without LACP
        et-0/0/6:
            mode: 			# Interface mode. Must be trunk
            esi: 			# ESI value configured manually
            vlans: 			# List of vlan-id to configure on this interface. Structure is [ 100, 101, 102]
            description: 	# Interface description
```

#### 'overlay-evpn-qfx-l2' role  
Generate configuration for EVPN/VXLAN for QFX in L2 mode (no rvi)
 - Overlay iBGP configuration
 - VNI/VLAN creation with associated policy options

Template can be found in [roles/overlay-evpn-qfx-l2/templates/main.conf.j2 ](https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/roles/overlay-evpn-qfx-l2/templates/main.conf.j2)

Using variable files from :
 - `host_vars/*hostname*/main.yaml`
 - `host_vars/*hostname*/overlay.yaml`

Structure of the `overlay.yaml` file is based on the following structure:
```yaml
	overlay:
	    local:
	        asn: 			# Local AS to build control plane of EVPN
	    neighbors: 			# List of IP address to configure BGP sessions. Must be RR if you are on leaves and must be leaves if you are on MXs. In any case, it must be loopback of devices
        bridge_domains:		# List all Bridge domains / vlan / vni
        - vlan_id: 100		# Vlan ID of the first bridge domain
          vni_id: 1000		# VNI associated to this vlan
```

#### 'overlay-evpn-mx-l3' role
Generate configuration for EVPN/VXLAN for MX in L3 mode (rvi)
 - Overlay iBGP configuration
 - VNI/VLAN creation with associated policy options
 - RVI per VLAN/VNI

Template can be found in [roles/overlay-evpn-mx-l3/templates/main.conf.j2 ](https://github.com/titom73/ansible-junos-evpn-vxlan-multitenant/blob/master/roles/overlay-evpn-mx-l3/templates/main.conf.j2)

Using variable files from :
 - `host_vars/*hostname*/main.yaml`
 - `host_vars/*hostname*/overlay.yaml`

Structure of the `overlay.yaml` file is based on the following structure:
```yaml
	overlay:
	    local:
	        asn: 				# Local AS to build control plane of EVPN
	    neighbors: 				# List of IP address to configure BGP sessions. Must be RR if you are on leaves and must be leaves if you are on MXs. In any case, it must be loopback of devices
	    rr_bgp: 				# List of all route reflector -- ONLY for MXs / not supported for leaves
	    tenants:
	      - id: 				# ID of the tenant 
	        bridge_domains:		# List all Bridge domains / vlan / vni
	        - vlan_id: 100		# Vlan ID of the first bridge domain
	          vni_id: 1000		# VNI associated to this vlan
	          vip: 10.1.100.1 	# Virtual Gateway -- ONLY for L3 devices
	          ip: 10.1.100.2 	# Physical IP address of the IRB -- ONLY for L3 devices
	          mask: 24 			# Netmask of the IRB -- ONLY for L3 devices
```

#### 'overlay-evpn-qfx-l3' role  
 Not implemented yet