
from pathlib import Path
from time import time
from math import prod

t0 = time()

################ Data Processing #################

points = []
instructions = []

#fin = (Path(__file__).parent / "in/test/16.in") #(ANS1=11,ANS2=9)
fin = (Path(__file__).parent / "in/16.in")
with open(fin, "r") as f:
    data = f.read()
    in_string = list(data)

################ Common Function #################

hex_to_bin = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

master_bit_string = ''
for char in in_string:
    master_bit_string += hex_to_bin[char]

def process_packet(bit_string):

    packet_value = ''

    version, bit_string = bit_string[:3], bit_string[3:]
    version = int(version,2)
    version_list.append(version) #for part 1 of the challenge

    type_id, bit_string = bit_string[:3], bit_string[3:]
    type_id = int(type_id,2)

    if type_id == 4:
        while True:
            packet, bit_string = bit_string[:5], bit_string[5:]
            header = int(packet[:1])
            packet_value = packet_value + packet[1:]
            if header == 0:
                break
        packet_value = int(packet_value,2)
    else:
        packet_values = []

        length_type_id, bit_string = bit_string[:1], bit_string[1:]
        if int(length_type_id) == 0:
            subpacket_len, bit_string = bit_string[:15], bit_string[15:]
            subpacket_bit_len = int(subpacket_len,2)
            sub_bit_string, bit_string = bit_string[:subpacket_bit_len], bit_string[subpacket_bit_len:]
            
            while True:
                packet_value, sub_bit_string = process_packet(sub_bit_string)
                packet_values.append(packet_value)
                if len(sub_bit_string) == 0:
                    break
        else:
            subpacket_len, bit_string = bit_string[:11], bit_string[11:]
            subpacket_count = int(subpacket_len,2)
            for _ in range(subpacket_count):
                packet_value, bit_string = process_packet(bit_string)
                packet_values.append(packet_value)

        if type_id == 0:
            packet_value = sum(packet_values)
        elif type_id == 1:
            packet_value = prod(packet_values)
        elif type_id == 2:
            packet_value = min(packet_values)
        elif type_id == 3:
            packet_value = max(packet_values)
        elif type_id == 5:
            if packet_values[0] > packet_values[1]:
                packet_value = 1
            else:
                packet_value = 0
        elif type_id == 6:
            if packet_values[0] < packet_values[1]:
                packet_value = 1
            else:
                packet_value = 0
        elif type_id == 7:
            if packet_values[0] == packet_values[1]:
                packet_value = 1
            else:
                packet_value = 0

    return packet_value, bit_string

################ Part 1 #################

version_list = []

process_packet(master_bit_string)

print('ans1:',sum(version_list))

################ Part 2 ################

val, _ = process_packet(master_bit_string)

print('ans2:',val)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))