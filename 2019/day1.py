def main():
    fuel = 0
    fuel1 = 0
    fuel2 = 0
    with open("day1i.txt") as puzzle_input:
        for line in puzzle_input:
            mass = int(line.strip("\n").strip(" "))
            
            fuel = mass // 3 -2
            fuel1 += fuel
            fuel2 += fuel
            new_fuel = fuel // 3 - 2

            while new_fuel >= 0:
                fuel2 += new_fuel
                new_fuel = new_fuel //3 - 2

    print("Part one fuel is ", fuel1)
    print("Part two fuel is ", fuel2)

if __name__ == "__main__":
    main()