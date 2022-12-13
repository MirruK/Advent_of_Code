def formatdata():
    packet_pairs, buffer = [], []
    with open('./input.txt','r') as file:
        for line in file.readlines():
            if len(buffer) > 1:
                packet_pairs.append(buffer)
                buffer = []
            else: buffer.append(line.removesuffix('\n'))
    return packet_pairs

def parse_packet(packet_pair):
    packet1, packet2 = packet_pair[0],packet_pair[1]
    bracket_queue = []



print(formatdata())
