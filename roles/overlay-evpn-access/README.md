
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
