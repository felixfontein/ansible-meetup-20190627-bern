#!/usr/bin/python
from ansible.module_utils.basic import (
  AnsibleModule
)

import os

def main():
  argument_spec = dict(
    file=dict(type='path',
              required=True),
  )
  module = AnsibleModule(argument_spec)

  fn = module.params['file']
  if not os.path.exists(fn):
    module.fail_json(
      msg='"%s" does not exist!' % fn
    )
  module.exit_json(msg='"%s" exists' % fn)

if __name__ == '__main__':
  main()
