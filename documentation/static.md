# Documentation for static value in this playbook

Current templates implement some static value or assume a specific structure. This is mainly true for route-target configured to run EVPN control plane.
All those structure can be changed later to match your requirements. But in this case, it is required to edit template since it is not covered by YAML file.

## Route Target
### Target for VRF
Target is encoded based on the following structure:

```
target:10:{{tenant.id}}
```
The 10 is a common value for all VRF and variable is provided by tenant.id

### Target for Virtual Switch
Target is encoded based on the following structure:

```
vrf-target target:11:{{tenant.id}};
```
The 11 is a common value for all VRF and variable is provided by tenant.id

### Target for switch-option on leaves
Target is encoded based on the following structure:

```
vrf-target target:9999:9999;
```
This value is the same for all leaves and it is statically configured in the template.

### Target for VNI
Target is encoded based on the following structure:

```
target:1:{{ bd.vni_id }};
```
The 1 is a common value for all VRF and variable is provided by bd.vni_id

### List of templates
Route target can be changed in the following templates:
 - `roles/overlay-evpn-qfx-l2/templates/main.conf.j2`
 - `roles/overlay-evpn-mx-l3/templates/main.conf.j2`
 - `roles/overlay-evpn-access/templates/main.conf.j2`
