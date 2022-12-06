def formatdata():
    with open('./input.txt','r') as file:
        data = file.readlines()[0]
    return data


def detect_packet(data,span):
    answer = -1
    for n in range(len(data)):
        head = set(data[n:n+span])
        if len(head) == span:
            answer = n+span
            break
    return answer

datastream = formatdata()
print("First answer:", detect_packet(datastream,4))
print("Second answer:", detect_packet(datastream,14))