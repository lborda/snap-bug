#!/usr/bin/python3

import subprocess
import os

def create_files(filename, cmd):
    print('Running... : %s' % cmd)
    stdout = open(filename + '.out', 'w')
    stderr = open(filename + '.err', 'w')
    proc = Popen(cmd.split(), stdout=stdout, stderr=stderr)
    proc.wait()
    stdout.close()
    stderr.close()

def create_files2(filename, cmd):
    print('Running... : %s' % cmd)
    proc = subprocess.Popen(cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate(cmd.encode())
    proc.wait()
    if stdout:
        with open(filename + '.out', 'w') as file:
            file.write(stdout.decode())
    if stderr:
        with open(filename + '.err', 'w') as file:
            file.write(stderr.decode())

def main():
    snap_user_common = os.getenv('SNAP_USER_COMMON')
    #snap_user_common = '/home/lborda/snap/snap-bug/common'
    filename = 'juju-status'
    cmd = 'juju status'
    create_files2(filename, cmd)

if __name__ == '__main__':
    main()



