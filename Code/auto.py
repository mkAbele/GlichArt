import os

import subprocess

# change - Change bytes in chunk to random values.
# reverse - Reverse order of bytes in chunk.
# repeat - Repeat first X bytes (specfied with --repeat-width) of chunk throughout the chunk.
# remove - Remove the chunk entirely.
# zero - Make the chunk all zeroes.
# insert - Insert random chunk of data at a random point.
# replace - Replace chunk with a chunk of random data.
# move - Remove a chunk from one position to another.

source = 'beyond-repair.bmp'
modes = ['change', 'reverse', 'repeat', 'remove', 'zero', 'insert', 'replace', 'move']
# result = subprocess.check_output('py glitch_tool.py -i "../'+source+'" -m change -c 10 -b 10 -r 10', shell=True, text=True)
# print(result)

for mode in modes:
    print(mode)
    print('-c 1 -b 1 -r 1')
    result = subprocess.check_output('py glitch_tool.py -i "../'+source+'" -m '+mode+' -c 1 -b 1 -r 1', shell=True, text=True)
    print(result)
    print('-c 5 -b 5 -r 5')
    result = subprocess.check_output('py glitch_tool.py -i "../'+source+'" -m '+mode+' -c 5 -b 5 -r 5', shell=True, text=True)
    print(result)
    print('-c 10 -b 10 -r 10')
    result = subprocess.check_output('py glitch_tool.py -i "../'+source+'" -m '+mode+' -c 10 -b 10 -r 10', shell=True, text=True)
    print(result)
