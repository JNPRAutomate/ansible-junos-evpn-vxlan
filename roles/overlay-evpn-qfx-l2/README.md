
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
