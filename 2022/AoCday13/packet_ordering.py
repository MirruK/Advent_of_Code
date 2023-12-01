def formatdata():
    packet_pairs, buffer = [], []
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            if len(buffer) > 1:
                packet_pairs.append(buffer)
                buffer = []
            else:
                buffer.append(line.removesuffix("\n"))
    return packet_pairs


def find_list(packet):
    brackets = []
    for ind, char in enumerate(packet):
        if char == "[":
            brackets.append(ind)
        if char == "]":
            if len(brackets) == 1:
                curr_list = packet[brackets[0] : ind + 1]
                return (curr_list, brackets[0], ind + 1)
            else:
                brackets.pop()
    return ("", -1, -1)


def packet_is_list(packet):
    return (
        True
        if find_list(packet)[1] == 0
        and len(find_list(packet)[0]) == len(packet)
        else False
    )


def wrap_packet(packet):
    return "[" + packet + "]"


def unwrap_packet(packet):
    if packet_is_list(packet):
        return packet[1:-1]
    return packet


def drop_data(packet):
    return ",".join(packet.split(",")[1:])


def drop_list(packet):
    ind = find_list(packet)[2]
    return packet[ind + 1 :] if ind != -1 else packet


def iterate_list(packet):
    if find_list(packet)[1] == 0:
        return find_list(packet)[0]
    else:
        return packet.split(",")[0]
    # if packet_is_list(packet) == False:
    #    return [char for char in find_list(packet)[0][1:-1].split(",")]
    # else: return find_list(packet)


def equalize(packet1, packet2):
    new_packet1, new_packet2 = "", ""
    while True:
        if packet1 == new_packet1 and new_packet2 == packet2:
            return new_packet1, new_packet2
        if packet_is_list(packet1) and packet_is_list(packet2):
            new_packet1, new_packet2 = unwrap_packet(packet1), unwrap_packet(
                packet2
            )
        elif packet_is_list(packet1) and not packet_is_list(packet2):
            new_packet1, new_packet2 = packet1, wrap_packet(packet2)
        elif not packet_is_list(packet1) and packet_is_list(packet2):
            new_packet1, new_packet2 = wrap_packet(packet1), packet2
        else:
            new_packet1, new_packet2 = packet1, packet2


def parse_packet(packet_pair):
    packet1, packet2 = packet_pair[0], packet_pair[1]
    while True:
        packet1, packet2 = equalize(packet1, packet2)


packet_pairs = formatdata()
