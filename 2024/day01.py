import re


if __name__ == "__main__":
    left = []
    right = []
    with open("day1_input.py") as input:
        for line in input:
            inputs = re.findall("[0-9]+", line)
            left.append(int(inputs[0]))
            right.append(int(inputs[1]))

    left.sort()
    right.sort()
    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    print(f"sum is {sum}")

    r_counts = {}
    for num in right:
        if num in r_counts.keys():
            r_counts[num] += 1
        else:
            r_counts[num] = 1
    sim = 0
    for num in left:
        if num in r_counts.keys():
            sim += r_counts[num] * num
    
    print(f"sim is {sim}")