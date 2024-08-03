#!/usr/bin/env python3
#AuthorID-167976216

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = p.communicate()
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
