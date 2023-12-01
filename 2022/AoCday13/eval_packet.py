def eval_packets(packet_pair):
    return [eval(packet_pair[0]),eval(packet_pair[1])]


def formatdata():
    packet_pairs, buffer = [], []
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            if len(buffer) > 1:
                packet_pairs.append(eval_packets(buffer))
                buffer = []
            else:
                buffer.append(line.removesuffix("\n"))
    return packet_pairs


def det_type(subpacket):
    return 0 if type(subpacket) == list else 1


def get_action(packet_pair):
    p1 = packet_pair[0]
    p2 = packet_pair[1]
    t1 = det_type(p1)
    t2 = det_type(p2)
    if t1 == 0 and t2 == 0:
        # 0 means both are lists
        return 0
    elif t1 == 1 and t2 == 1:
        # 1 means both are integers
        return 1
    elif t1 > t2:
        # 2 means first packet is int and other is list
        return 2
    else: 
        # 3 means first packet is list and other is int
        return 3


def det_order(packet_pair, new_pair):
    p1 = packet_pair[0]
    p2 = packet_pair[1]
    length = len(p1) if len(p1)<len(p2) else len(p2)
    if len(p1) == 0 or len(p2) == 0:
        return 0
    for val in range(length):
        p1 = packet_pair[0][val]
        p2 = packet_pair[1][val]
        match get_action(packet_pair):
            case 0:
                #Start interating lists
                pass              
            case 1:
                pass # Compare values 
                # If same continue, else return
            case 2:
                pass # Stay at p1 val, start iterating p2
            case 3:
                pass # Same as prev. but vice versa


packet_pairs = formatdata()

"""
recursive func f
base cases 
f(pair) 
return value: 0 --> packets in order
return value: 1 --> wrong order
return value: -1 --> undetermined


"""
