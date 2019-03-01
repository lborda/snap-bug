#!/usr/bin/python3

from subprocess import Popen
import os

def create_files(filename, cmd):
    print('Running... : %s' % cmd)
    stdout = open(filename + '.out', 'w')
    stderr = open(filename + '.err', 'w')
    proc = Popen(cmd.split(), stdout=stdout, stderr=stderr)
    proc.wait()
    stdout.close()
    stderr.close()

def main():
    #snap_user_common = os.getenv('SNAP_USER_COMMON')
    snap_user_common = '/home/lborda/snap/snap-bug/common'
    filename = snap_user_common + '/juju-status'
    cmd = 'juju status'
    create_files(filename, cmd)

if __name__ == '__main__':
    main()
