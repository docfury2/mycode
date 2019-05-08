#!/usr/bin/env python3

import paramiko
import os
def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()

ipchk = input('Enter an IP address: ')
#if ipchk == ('10.10.2.3'):
 #   print('success')
#else:
#    print('failure')
user = input('Enter a username: ')
passwd = input('Enter your password: ')

mylist = ['ipchk', 'user', 'passwd']
sshsession.connect(hostname=int('ipchk'), username=('user'), password=('passwd'))
#mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

#sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#if ipchk == '10.10.2.3' and user == 'bender' and passwd == 'alta3':
 #   print('success!')
#else:
#    print('done')
#
