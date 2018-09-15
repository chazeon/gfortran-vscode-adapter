import sys
import subprocess
import re

proc = subprocess.Popen(['gfortran'] + sys.argv[1:], stderr=subprocess.PIPE)
stack = []
while True:
    line = proc.stderr.readline().decode()
    if line == '': break
    if line.startswith(' ') or line.startswith('\n'): continue
    if len(stack) != 0:
        sys.stdout.write(stack.pop().strip() + line)
        continue
    elif re.search(r'^(.+):(\d+):(\d+):$', line.strip()):
        stack.append(line)