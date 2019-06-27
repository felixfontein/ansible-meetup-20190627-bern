#!/usr/bin/python
from ansible.module_utils.basic import (
  AnsibleModule
)

def main():
  argument_spec = dict(
    name=dict(type='str',
              required=True),
    some_number=dict(type='int'),
    colors=dict(type='list',
                elements='str'),
    state=dict(type='str',
               default='present',
               choices=['present', 'absent']),
    password=dict(type='str',
                  no_log=True),
  )
  module = AnsibleModule(argument_spec)
  module.exit_json(**module.params)

if __name__ == '__main__':
  main()
