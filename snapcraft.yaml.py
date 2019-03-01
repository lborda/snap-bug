name: snap-bug
version: git
summary: Snap bug permissions
description: Attempts to create a file using python popen.

confinement: classic

base: core18

parts:
  cdk-field-agent:
    plugin: python
    python-version: python3
    source: .
    override-build: |
      snapcraftctl build
      mkdir -p $SNAPCRAFT_PART_INSTALL/bin
      cp collect.py $SNAPCRAFT_PART_INSTALL/bin/
apps:
  cdk-field-agent:
    command: bin/collect.py
