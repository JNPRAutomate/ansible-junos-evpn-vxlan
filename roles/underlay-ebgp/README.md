
# 'underlay-ebgp' role

Generate the base configuration to build an IP Fabric with EBGP:
 - Point to Point IP per interface
 - Underlay BGP configuration using EBGP
 - BFD for BGP on all interfaces
 - BGP policy options
 - ECMP across Spines

Template can be found in [roles/underlay-ebgp/templates/main.conf.j2 ](templates/main.conf.j2)

Using variable files from :
 - [group_vars/all/underlay.yaml]()
 - `host_vars/*hostname*/main.yaml`
 - `host_vars/*hostname*/underlay.yaml`

Structure of the `underlay.yaml` file is based on the following structure:
```yaml
underlay:
## Default parameters
## All default parameters are available [here](defaults/main.yaml)
    mtu_phy_int:        # MTU of physical interfaces
    mtu_logical_int:    # MTU of logical interfaces
    network_size:       # Network Size for P2P link
    bfd:                # Configuration for BFD
      min_interval:     
      multiplier:
      mode:
    networks:           # Network information used to build policy
      loopbacks:
      underlay:
## User provided parameters
    local:
        asn: 				    # Local ASN configured for the underlay on the device
    neighbors:
      - interface:	    # Interface connected to a remote peer in the IP Fabric
        name: 			    # Hostname of the connected device (useful for comment)
        remote_interface: 	# Remote interface connected to our device
        asn:				    # ASN of the remote device
        peer_ip:		  	# Directly connected IP address of the remote device (DO NOT USE LOOPBACK since it is IP fabric)
        local_ip:			  # Local IP address configured on directly connected interface
      - interface:			# Interface connected to a remote peer in the IP Fabric
        name: 				  # Hostname of the connected device (useful for comment)
        remote_interface: 	# Remote interface connected to our device
        asn:				    # ASN of the remote device
        peer_ip:			  # Directly connected IP address of the remote device (DO NOT USE LOOPBACK since it is IP fabric)
        local_ip:			  # Local IP address configured on directly connected interface

## Optional Parameters based on devices roles
    advertize_local_only: # Recommended for Leaf to avoid re advertising other loopback
    community:            # Recommended for Spine in Multi-pod topology
```

### Example
```yaml
underlay:
    local:
        asn: 60010
    neighbors:
      - interface: "{{ topo[inventory_hostname].port1.name }}"
        name: "{{ topo[inventory_hostname].port1.peer }}"
        asn: 60001
        peer_ip: 171.0.0.0
        local_ip: 171.0.0.1
      - interface: "{{ topo[inventory_hostname].port2.name }}"
        name: "{{ topo[inventory_hostname].port2.peer }}"
        asn: 60002
        peer_ip: 171.0.0.8
        local_ip: 171.0.0.9
```
