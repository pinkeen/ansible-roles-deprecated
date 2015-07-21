#!/usr/bin/env python
#coding: UTF-8

import sys

if len(sys.argv) != 3:
    print 'Usage: %s [email] [password]' % (sys.argv[0])
    sys.exit(1)

ccnet_dir = "{{ seafile_ccnet_config_dir }}"
email = sys.argv[1]
password = sys.argv[2]

import ccnet

rpc_client = ccnet.CcnetThreadedRpcClient(ccnet.ClientPool(ccnet_dir))
users = rpc_client.get_emailusers('DB', 0, 1)

if len(users) != 0:
    print "Admin user already exists!"
    sys.exit(2)

rpc_client.add_emailuser(email, password, 1, 1)

lock = open('{{ seafile_home }}/seahub_admin_created.lock', 'w')
lock.write('do not remove')
lock.close()
