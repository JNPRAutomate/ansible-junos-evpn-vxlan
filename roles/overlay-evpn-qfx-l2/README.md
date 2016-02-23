
#### 'overlay-evpn-qfx-l2' role  
Generate configuration for EVPN/VXLAN for QFX in L2 mode (no rvi)
 - Overlay iBGP configuration
 - VNI/VLAN creation with associated policy options

Template can be found in [roles/overlay-evpn-qfx-l2/templates/main.conf.j2 ](templates/main.conf.j2)


## Variables Needed by this role

Using variable files from :
 - `host_vars/*hostname*/main.yaml`
 - `host_vars/*hostname*/overlay.yaml`

```yaml

overlay:
## Defined by default
    bfd:
      min_interval:
      multiplier:
      mode:
## Provided by user
    local:
        asn:              # ASN to use for iBGP
    neighbors:            # iBGP neighbors, usually spines loopback addresses
    tenants:              # List of tenants with VLAN per tenants
      <tenant_A_name>:
        id: xx
        bridge_domains:
        - vlan_id:
          vni_id:
        - vlan_id:
          vni_id:
      <tenant_B_name>:
        id: yy
        bridge_domains:
        - vlan_id:
          vni_id:
        - vlan_id:
          vni_id:

## Optional
      remote_gw: [ ip, ip ]   # Recommended for Multi-pod environment to discard loopback from spine that are not local
```
