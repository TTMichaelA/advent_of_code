import re

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

class day7:

    def __init__(self, puzzle_input):
        self.operations = self.process_input(puzzle_input)

    def process_input(self, input):
        operations = []
        for line in input.splitlines():
            operands = re.findall("\d+", line)
            print(operands)
            operations.append(operands)
        return operations
    
    def check_single_pattern_pt1(self, pattern):
        tgt = pattern[0]
        ops = pattern[1:]
        eval_set = set()
        for i in range(len(ops)):
            next_set = set()
            if i == 0:
                eval_set.add(int(ops[i]))
                continue
            for item in eval_set:
                next_set.add(item + int(ops[i]))
                next_set.add(item * int(ops[i]))
            eval_set = next_set
        for evals in next_set:
            if int(tgt) == evals:
                return True
        return False
    
    def check_single_pattern_pt2(self, pattern):
        tgt = pattern[0]
        ops = pattern[1:]
        eval_set = set()
        for i in range(len(ops)):
            next_set = set()
            if i == 0:
                eval_set.add(int(ops[i]))
                continue
            for item in eval_set:
                next_set.add(item + int(ops[i]))
                next_set.add(item * int(ops[i]))
                next_set.add(int(str(item) + ops[i]))
            eval_set = next_set
        for evals in next_set:
            if int(tgt) == evals:
                return True
        return False

    # def check_single_pattern_correctly(self, pattern):
    #     tgt = pattern[0]
    #     ops = pattern[1:]
    #     eval_set = set()
    #     for i in range(len(ops)):
    #         next_set = set()
    #         if i == 0:
    #             eval_set.add(ops[i])
    #             continue
    #         for item in eval_set:
    #             next_set.add(item + "+" + ops[i])
    #             next_set.add(item + "*" + ops[i])
    #         eval_set = next_set
    #     for evals in next_set:
    #         if int(tgt) == eval(evals):
    #             return True
    #     return False
            
    def check_patterns(self):
        running_sum = 0
        for operation in self.operations:
            if self.check_single_pattern_pt2(operation):
                running_sum += int(operation[0])
        return running_sum


if __name__ == "__main__":
    instance = day7(true_input)
    print(instance.check_patterns())
