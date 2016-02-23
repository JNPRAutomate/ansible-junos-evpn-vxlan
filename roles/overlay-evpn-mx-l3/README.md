
# 'overlay-evpn-mx-l3' role
Generate configuration for EVPN/VXLAN for MX in L3 mode (rvi)
 - Overlay iBGP configuration
 - VNI/VLAN creation with associated policy options
 - RVI per VLAN/VNI

Template can be found in [overlay-evpn-mx-l3/templates/main.conf.j2](templates/main.conf.j2)

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
      <tenant_A_name>:
        id: 				      # ID of the tenant
        bridge_domains:		# List all Bridge domains / vlan / vni
        - vlan_id: 		    # Vlan ID of the first bridge domain
          vni_id: 		    # VNI associated to this vlan
          network:  	    # Physical IP address of the IRB -- ONLY for L3 devices
          mask: 24 			  # Netmask of the IRB -- ONLY for L3 devices

# Default parameters
    bfd:
      min_interval:
      multiplier:
      mode:
```
