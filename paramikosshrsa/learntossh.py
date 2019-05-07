#!/usr/bin/env python3

##import paramiko so we can talk to ssh
import paramiko
import os

## shortcut issuing comands to remote
def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()

##mykey is our private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

##if we never went to this SSH host, add the fingerprint to the known host file
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

##creds to connect
sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

## a simple list of commands to issue across our connection
our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

## cycle through our commands, and issue them on the far end
for x in our_commands:
    print(commandissue(x))

print(commandissue(x).decode('utf-8'))
