"""
argument 1:  year
argument 2:  optional: Day Start
argument 3:  optional: Day End
"""

from pathlib import Path
import os
import sys

try:
    year = sys.argv[1]
except:
    print(__doc__)
    exit()
try:
    day_start = int(sys.argv[2])
except:
    day_start = 1
try:
    day_end = int(sys.argv[3])
except:
    day_end = 25

os.mkdir(Path(__file__).parent / year)
os.mkdir(Path(__file__).parent / year / 'in')
os.mkdir(Path(__file__).parent / year / 'in' / 'test')

fin = (Path(__file__).parent / "template.py")

with open(fin, "r") as f1:
    data = f1.read()
    for i in range(day_start,day_end+1):
        with open(Path(__file__).parent / year / 'in' / (f"{i:02}" + '.in'), 'w') as fp:
            pass    
        with open(Path(__file__).parent / year / 'in' / 'test' / (f"{i:02}" + '.in'), 'w') as fp:
            pass    
        
        with open(Path(__file__).parent / year / (f"{i:02}" + '.py'), 'w') as f2:
            f2.write(data.replace("<YEAR>",year))


