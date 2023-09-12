# Ansible Collection

A collection of miscellaneous roles.

## Usage

Create a `requirements.yml` with, for example:

    collections:
      - name: https://github.com/mikavl/ansible-collection.git
        type: git
        version: main

Then just `ansible-galaxy install -r requirements.yml` and use the stuff.
