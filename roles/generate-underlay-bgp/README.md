
# 'generate-underlay-bgp' role

Generate YAML variables for eBGP underlay template.

This template will generate one YAML file per device named 'generated-underlay-ebgp.yaml' under 'host_vars/device_name'

Template can be found in [roles/generate-p2p-ips/templates/main.conf.j2 ](templates/main.conf.j2)

## Input needed by this role

To generate work properly, this role needs:
- A topology file defined, following the syntax below
- A table of p2p IP addresses, __it can be generated with the role `generate-p2p-ips`__
- An AS number assigned to every device in the variable: `underlay_as`

#### topology file

The topology file regroup all physical information related to a given topology.
```yaml
topo:
  spine-03:
    port1: { name: xe-0/0/0,     peer: leaf-01,   pport: port1 }
    port2: { name: xe-0/0/1,     peer: leaf-02,   pport: port1 }
```

This role will extend the information provided inside the topo file to also indicate which IP addresses
needs to be allocated per interface.  
To do so, tree additional parameters have been added: `type`, `link` and `linkend`
Those parameters needs to be define for all interfaces that are part of the eBGP setup.
```yaml
topo:
  spine-03:
    port1: { name: xe-0/0/0,     peer: leaf-01,   pport: port1, type: ebgp, link: 11, linkend: 1 }
    port2: { name: xe-0/0/1,     peer: leaf-02,   pport: port1, type: ebgp, link: 13, linkend: 1 }
```


```yaml
  type: indicate that this interface should be consider by the role
- link: link id to represent where this part is connected
- linkend: link-end id to indicate on which side of the link this device is.
```

### p2p IP addresses table
```yaml
p2p:
  1: { 1: 172.16.0.0,  2: 172.16.0.1 }
  2: { 1: 172.16.0.2,  2: 172.16.0.3 }
  3: { 1: 172.16.0.4,  2: 172.16.0.5 }
  4: { 1: 172.16.0.6,  2: 172.16.0.7 }
  5: { 1: 172.16.0.8,  2: 172.16.0.9 }
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
