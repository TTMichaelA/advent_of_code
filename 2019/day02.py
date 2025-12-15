
def execute_operation(operations, index):
    if operations[index] == 99:
        print("CHOGO")
        return 0
    
    if operations[index] == 1:
        operations[operations[index+3]] = operations[index+1] + operations[index+2]
    
    if operations[index] == 2:
        operations[operations[index+3]] = operations[index+1] * operations[index+2]
    print(operations)
    return execute_operation(operations, index+4)

def main():
    operations = {}
    with open("day02.txt") as puzzle_input:
        for line in puzzle_input:
            ops = line.strip().split(",")
            for i, val in enumerate(ops):
                operations[i] = int(val)
    operation_clone = operations.copy()
    ind = 0
    while True:
                    op0 = operations[ind]
                    if op0 == 99:
                        break
                    op1 = operations[ind+1]
                    op2 = operations[ind+2]
                    op3 = operations[ind+3]
                    
                    if op0 == 1:
                        operations[op3] = operations[op1] + operations[op2]
                        ind += 4
                        continue
                    elif op0 == 2:
                        operations[op3] = operations[op1] * operations[op2]
                        ind += 4
                        continue
    print(operations[0])
    
    for i in range(1,9000):
        for j in range(1, 9000):
            operations = operation_clone.copy()
            operations[1] = i
            operations[2] = j 
            ind = 0
            try:
                while True:
                    op0 = operations[ind]
                    if op0 == 99:
                        break
                    op1 = operations[ind+1]
                    op2 = operations[ind+2]
                    op3 = operations[ind+3]
                    
                    if op0 == 1:
                        operations[op3] = operations[op1] + operations[op2]
                        ind += 4
                        continue
                    elif op0 == 2:
                        operations[op3] = operations[op1] * operations[op2]
                        ind += 4
                        continue
            except:
                continue
            if operations[0] == 19690720:
                print(i,j)
                return 0
            

if __name__ == "__main__":
    main()
                
