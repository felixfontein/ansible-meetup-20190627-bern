#!/usr/bin/python
from ansible.module_utils.basic import (
  AnsibleModule
)

def main():
  module = AnsibleModule(dict())

  rc, stdout, stderr = module.run_command(
    ['ls', '/'],
    check_rc=True
  )
  # Ansible will fail if rc is != 0

  files = [
    f for f in stdout.split('\n') if f
  ]
  module.exit_json(files=files)

if __name__ == '__main__':
  main()
