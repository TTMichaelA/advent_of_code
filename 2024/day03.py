import re

if __name__ == "__main__":
    instructions = []
    with open("day3_input.py") as puzzle_input:
        for line in puzzle_input:
            pattern = re.compile("(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))")
            instruction_group = pattern.finditer(line)
            for i in instruction_group:
                instructions.append(i.group(0))
    print(instructions)
    print(len(instructions))
    tot = 0
    semitot = 0
    do = True
    for instr in instructions:
        if instr [:3] == 'mul':
            nums = re.findall("[0-9]+", instr)
            tot += int(nums[0]) * int(nums[1])
            if do:
                semitot += int(nums[0]) * int(nums[1])
        elif instr[:3] == 'do(':
            do = True
        elif instr[:3] == 'don':
            do = False

    print(f"The sum is {tot}")
    print(f"The p2 sum is {semitot}")
