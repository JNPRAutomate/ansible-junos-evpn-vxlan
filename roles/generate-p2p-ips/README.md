
# 'generate-p2p-ips' role

Generate a list of IP addresses to use for Point to Point link.  
This is especially useful to construct and IP fabric.

This template will generate one YAML file named 'generated_p2p_ips.yaml' under 'group_vars/all'

Template can be found in [roles/generate-p2p-ips/templates/main.conf.j2 ](templates/main.conf.j2)

## Variables needed by the template

```yaml
generate_p2p:
  nbr_networks:         # Number of p2p link to generate`
  network_size:         # Network size for each p2p link
  network_pool:         # Netlwork pool to use to generate one network per link
```

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
p2p:
  link1: { 1: 172.16.0.0,  2: 172.16.0.1 }
  link2: { 1: 172.16.0.2,  2: 172.16.0.3 }
  link3: { 1: 172.16.0.4,  2: 172.16.0.5 }
  link4: { 1: 172.16.0.6,  2: 172.16.0.7 }
  link5: { 1: 172.16.0.8,  2: 172.16.0.9 }
  link6: { 1: 172.16.0.10,  2: 172.16.0.11 }
  link7: { 1: 172.16.0.12,  2: 172.16.0.13 }
  link8: { 1: 172.16.0.14,  2: 172.16.0.15 }
  link9: { 1: 172.16.0.16,  2: 172.16.0.17 }
  link10: { 1: 172.16.0.18,  2: 172.16.0.19 }
  link11: { 1: 172.16.0.20,  2: 172.16.0.21 }
```
