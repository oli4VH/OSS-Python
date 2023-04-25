#!/usr/bin/python3

import sys


# Dit script neemt auth.log logfiles als command line parameters om hierin te
# tellen hoe vaak door elke user is ingelogd en hoe vaak van elk IP adres is
# ingelogd. Op het einde worden deze aantallen geprint.

# Opdracht:
# Vervolledig dit script volgens de comments die beginnen met "TODO".

'''
Lines indicating successful logins:
Mar 19 08:59:16 bletchley sshd[183804]: Accepted password for s124134 from 91.177.112.120 port 50898 ssh2
Mar 31 15:06:52 bletchley sshd[224703]: Accepted publickey for dieter from 84.198.36.41 port 55042 ssh2: RSA SHA256:vRs4IXI4TVdoCbzjigjd7zKTBr6SLQzPVdKN04CLFjI
'''

def countlogins(log, by_user, by_ip):
    '''
    Count succesful logins by each user and from each IP adress in open
    logfile ``log'' and store the results in dictionaries ``by_user'' and
    ``by_ip''.
    '''
    for line in log:
        words = line.split()
        # Only process lines from sshd service:
        if len(words) < 5 or not words[4].startswith('sshd'):
            continue
        # TODO: skip lines when the word after sshd[...] is not "Accepted"

        user = words[6] # TODO: correct index of user
        # TODO: simplify the following lines by replacing if with the use of
        # dict method setdefault
        if user in by_user:
            by_user[user] += 1
        else:
            by_user[user] = 1

        # TODO: add code for by_ip

logfiles = sys.argv[1:]
usercounts = {}
ipcounts = {}

# TODO: add loop to open each logfile, call countlogins with it, then close it.
# TODO: add exception handling so that when a file cannot be opened, an error
#       is printed and the code skips to the next one.

# TODO: loop over usercounts and print how many times each user logged in
# TODO: loop over ipcounts and print how many times each ip was logged in from
