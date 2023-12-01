def formatdata():
    instructions = []
    with open('./input.txt','r') as file:
        for line in file.readlines():
            instructions.append(line.removesuffix("\n"))
    return instructions

def run_cycle(cycle,reg_X):
    return [cycle+1, reg_X*cycle] if (cycle+20) % 40 == 0 else [cycle+1, 0]

instructions = formatdata()

def emulate_signal(instructions):
    cycle_counter = 1 
    reg_X = 1
    signals = []
    for inst in instructions:
        opcode = inst.split()[0]
        if opcode == "noop":
            res = run_cycle(cycle_counter,reg_X)
            cycle_counter = res[0]
            if res[1] != 0:
                signals.append(res[1])

        elif opcode == "addx":
            for _ in range(2):
                res = run_cycle(cycle_counter,reg_X)
                cycle_counter = res[0]
                if res[1] != 0:
                    signals.append(res[1])
            reg_X = reg_X + int(inst.split()[1])
    return signals

def render_sprite():
    screen = ["." for _ in range(240)]
    sprite_pos = 1
    sprite_span = [0,1,2]
    add_queue = []
    to_add = 0
    cycle = 1
    for inst in instructions:
        curr_instruction = inst.split()[0]
        if curr_instruction == "addx":
            to_add = int(inst.split()[1])
        # begin exec (Cycle = 1)
        # if add_queue not empty skip next step
        # if inst == add: add_queue = [0,num_to_add] else add_queue = [0]
        if len(add_queue) == 0:
            if curr_instruction == "addx":
                add_queue = [to_add,0]
            else: add_queue = [0]
        # CRT Draw  ( "#" if cycle % 40 in sprite_span else ".")
        for curr in add_queue:
            current_pixel = (cycle-1)
            print("Current Pixel:",current_pixel, "Current pixel X location:", current_pixel%40)
            print("Sprite span:", sprite_span)
            screen[cycle-1] = "#" if (cycle) % 40 in sprite_span else "."
            # Finish adding, sprite_pos += add_queue.pop()
            sprite_pos += curr
            sprite_pos = sprite_pos % 40
            # Sprite_Span = [sprite_pos-1, sprite_pos, sprite_pos+1]
            sprite_span = [sprite_pos-1, sprite_pos, sprite_pos+1]
            # After finishing all tasks, increment cycle
            cycle += 1
        add_queue = []
    return screen

print("First answer:", sum(emulate_signal(instructions)))
pixels = render_sprite()
for n in range(6):
    print(pixels[n*40:(n*40)+40])