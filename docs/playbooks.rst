Playbooks
=========

All playbooks are stored at the root of the project and are named `pb.*.yaml`

Configure
---------

.. code-block:: yaml

    pb.save.config.yaml               # Download configuration for all devices and save them locally

    pb.conf.all.yaml                  # Generate and assemble configuration for all devices
    pb.conf.all.commit.yaml           # Generate, assemble, push and commit configuration to all devices

    # This project has been updated to use the new Junos modules available in Ansible 2.1
    # Some playbooks are also provided with the Junipe.junos modules available in Ansible Galaxy.
    pb.conf.all.commit.galaxy.yaml    # Generate, assemble, push and commit configuration to all devices
                                      # using the Junos modules provided in Ansible Galaxy

Test
----

.. code-block:: yaml

    pb.check.connectivity.yaml        # Check if all devices are reachable via Netconf
    pb.check.underlay.yaml            # Check the heath of the underlay
    pb.check.overlay.yaml             # Check the health of the overlay


Generate Variables
------------------

.. code-block:: yaml

    pb.generate.variables.yaml        # Regenerate variables files for p2p links, Tenants and VNI

Misc
----

.. code-block:: yaml

    pb.init.make_clean.yaml           # Create temp directory for all devices
