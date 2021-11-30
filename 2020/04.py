from pathlib import Path
from time import time
import re

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/04.in").open().read()
records = fin.split('\n\n')
records = [record.replace('\n',' ').split(' ') for record in records]
records = [dict(field.split(':') for field in record) for record in records]

################ Common Function #################

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #cid not required

################ Part 1 #################

count1 = 0

for record in records:
    if all(field in record for field in required_fields):
        count1 += 1
    
print('ans1:',count1)

################ Part 2 #################

ecl_valid = ['amb','blu','brn','gry','grn','hzl','oth']
count2 = 0

for record in records:
    if not all(field in record for field in required_fields):
        continue

    if not (1920 <= int(record['byr']) <= 2002):
        continue

    if not (2010 <= int(record['iyr']) <= 2020):
        continue

    if not (2020 <= int(record['eyr']) <= 2030):
        continue

    if record['hgt'][-2:] == 'cm':
        if not (150 <= int(record['hgt'][:-2]) <= 193):
            continue
    elif record['hgt'][-2:] == 'in':
        if not (59 <= int(record['hgt'][:-2]) <= 76):
            continue
    else:
        continue

    if not (re.search("#[0123456789abcdef]{6}",record['hcl'])):
        continue

    if not any(field in record['ecl'] for field in ecl_valid):
        continue

    if not (re.match("^\d{9}$",record['pid'])):
        continue

    count2 += 1

print('ans2:',count2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))