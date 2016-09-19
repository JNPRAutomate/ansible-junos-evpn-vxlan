
# 'generate-underlay-bgp' role

Generate YAML variables for eBGP underlay template.

This template will generate one YAML file per device named 'underlay-ebgp.yaml' under 'host_vars/device_name'

Template can be found in [roles/generate-p2p-ips/templates/main.conf.j2 ](templates/main.conf.j2)

## Variables needed by the template

Topology and underlay_as.yaml (group_vars/all) files as input

### Example of variable file

**For Group 'all'**
```yaml
# group_vars/all/p2p_ips.yaml
generate_p2p:
  nbr_networks: 10
  network_size: 31
  network_pool: 100.0.0.0/24
```

### Example of output generated
```yaml
underlay:
    leaf: true
    local:
        asn: 60012
    community: target:12345:111
    neighbors:
      - interface: et-0/0/51
        name: spine-02
        asn: 60014
        peer_ip: 172.16.0.6
        local_ip: 172.16.0.7
      - interface: et-0/0/50
        name: spine-01
        asn: 60012
        peer_ip: 172.16.0.2
        local_ip: 172.16.0.3
```
