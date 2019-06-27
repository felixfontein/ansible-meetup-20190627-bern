#!/usr/bin/python
from ansible.module_utils.basic import (
  AnsibleModule
)
from ansible.module_utils.urls import fetch_url

def main():
  module = AnsibleModule(dict())
  # Running against local httpbin docker container
  # (see ../../start-local-httpbin.sh)
  r, i = fetch_url(
    module, 'http://localhost:80/post',
    method='POST', data='x=42'
  )
  # Use headers={'header': 'value'} to set
  # custom headers
  status = i["status"]
  try:
    body = r.read()
  except Exception as e:
    body = i.get('body')
  body = module.from_json(body)
  module.exit_json(status=status, body=body)

if __name__ == '__main__':
  main()
