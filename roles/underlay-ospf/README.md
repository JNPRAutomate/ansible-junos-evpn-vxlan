
# 'underlay-ospf' role

Generate the base configuration to build an IP Fabric with OSPF:
 - Point to Point IP per interface

Template can be found in [roles/underlay-ospf/templates/main.conf.j2 ](templates/main.conf.j2)

## Variables Needed by this role

```yaml

```

### Example

This template have been designed to used a variable structure mainly composed of hash/dict.  
Leveraging Ansible option to *merge hash*, it become possible to have all required information coming from different variable files, in order to reduce data duplication.

- group_vars/*group_name*/underlay-ospf.yaml   > Information shared across devices
- host_vars/*device_name*/underlay-ospf.yaml   > information specific to single device

**For Group 'all'**
```yaml


```
