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
    filename = 'juju-status'
    cmd = 'ls -la ~/'
    create_files(filename, cmd)

if __name__ == '__main__':
    main()
