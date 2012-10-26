import subprocess
import sys

file = sys.argv[1]
from_line = int(sys.argv[2])
to_line = from_line
if len(sys.argv) > 3:
        to_line = int(sys.argv[3])

lfile = file + '.left'
lf = open(lfile, 'w')
mfile = file + '.middle'
mf = open(mfile, 'w')
rfile = file + '.right'
rf = open(rfile, 'w')

ct = 0
with open(file, 'r') as f:
    for line in f:
        ct += 1
        if ct < from_line:
            lf.write(line)
        elif ct > to_line:
            rf.write(line)
        else:
            mf.write(line)

lf.close()
mf.close()
rf.close()

subprocess.call(['vi', mfile])

lf = open(lfile, 'a')
with open(mfile, 'r') as mf:
    for line in mf:
        lf.write(line)
with open(rfile, 'r') as rf:
    for line in rf:
        lf.write(line)
lf.close()

subprocess.call(['rm', file, mfile, rfile])
subprocess.call(['mv', lfile, file])
