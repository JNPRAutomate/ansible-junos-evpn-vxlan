
# 'generate-tenant-vni' role

Generate variable files to scale easily the number of tenant and VNI per tenant.
This template will generate a YAML file for each device under host_vars directory named 'generated_tenant_vni.yaml'

Template can be found in [roles/generate-tenant-vni/templates/main.conf.j2 ](templates/main.conf.j2)

## Variables needed by the template

```yaml
generate_tenant:
  nbr_tenant:             # Number of tenant that will be created
  nbr_vni_tenant:         # Number of VNI to create per tenant
  tenant_start_id:        # Where do we start to create tenant ID
  vlan_start:             # Where do we start to create vlan ID
  vni_prefix:             # VNI will be generated with <vni_prefix><vlan_id>
  vip_id: 1               # Id of the virtual gateway in the subnet

  network_pool:           # Network pool to use to generate one subnet for each VNI
  network_size:           # Size of the network to generate for each VNI

  loopback_pool:          # Network pool to use to generate loopback for each tenant per device
  loopback_size: 24       # Size of the network to use to generate these loopback
```

### Example

**For Group 'all'**
```yaml
# group_vars/all/tenant_vni.yaml
generate_tenant:
  nbr_tenant: 10
  nbr_vni_tenant: 10
  tenant_start_id: 10
  vlan_start: 100
  vni_prefix: 10
  vip_id: 1

  network_pool: 100.0.0.0/16
  network_size: 24

  loopback_pool: 101.0.0.0/16
  loopback_size: 24

```
