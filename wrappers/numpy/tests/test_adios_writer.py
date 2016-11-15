#!/usr/bin/env python
"""
Example:

$ python ./test_adios_write.py
"""

import adios as ad
import numpy as np

print("\n>>> Prepare ...\n")
fname = 'adios_test_writer.bp'
NX = 100000
size = 2
t = np.array(list(range(NX*size)), dtype=np.float64)
tt = t.reshape((size, NX))

print("\n>>> Writing ...\n")
ad.init_noxml()
ad.set_max_buffer_size (10)

fw = ad.writer(fname)
fw.declare_group('group', method='POSIX1')

fw['NX'] = NX
fw['size'] = size
fw['temperature'] = tt
fw['temperature'].transform = "zfp:accuracy=0.001"
fw.attrs['/temperature/description'] = "Global array written from 'size' processes"
fw.close()

## Reading
print("\n>>> Reading ...\n")

f = ad.file(fname)
for key, val in f.vars.items():
    print(key, '=', val.read())

for key, val in f.attrs.items():
    print(key, '=', val.value)

## Testing
print("\n>>> Done.\n")
