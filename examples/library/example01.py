#!/usr/bin/python
from ansible.module_utils.basic import (
  AnsibleModule
)

def main():
  module = AnsibleModule(dict())
  module.exit_json(msg="Hello!")

if __name__ == '__main__':
  main()
