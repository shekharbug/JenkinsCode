#!/usr/bin/python3
import os
import sys
import subprocess
import shlex

def run_os_process(cmd: str, shell_cmd:bool =True) -> None| bool:
    if not shell_cmd:
        p1 = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    else:
        p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, error = p1.communicate()
    if error:
        print(f'failed to execute: {cmd}') 
        return False
    print(f'output : {out}')
    return True

def main():
    # free space
    free_cmd = "free -g"
    process_cmd = 'ps -ef'
    run_os_process(free_cmd)
    run_os_process(process_cmd)

if __name__ == '__main__':
    main()