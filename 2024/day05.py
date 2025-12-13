import re
class day5:
    def __init__(self, puzzle_input):
        self.rules, self.lists = self.process_input(puzzle_input)
        self.valid_middles = []
        self.invalid_middles = []
        self.valid_lists = []
        self.invalid_lists = []

    def process_input(self, puzzle_input):
        rules = {}
        lists = []

        for line in puzzle_input.splitlines():
            if line.find("|") != -1:
                rule = re.split("\|", line)

                if rule[0] in rules.keys():
                    rules[rule[0]].add(rule[1])
                else:
                    rules[rule[0]] = set()
                    rules[rule[0]].add(rule[1])
            elif len(line) > 0:
                lists.append(re.split(",",line))
                print(re.split(",",line))
        return rules, lists

    def check_rule(self, list_item):
        seen = set()
        for item in list_item:
            if item not in self.rules.keys():
                seen.add(item)
            else:
                for too_soon in self.rules[item]:
                    if too_soon in seen:
                        return False
                seen.add(item)
        return True

    def check_rules(self):
        for number_list in self.lists:
            if self.check_rule(number_list):
                self.valid_lists.append(number_list)
            else:
                self.invalid_lists.append(number_list)
        return 0

    def return_valid_sum(self):
        for number_list in self.valid_lists:
                mid_ind = len(number_list) // 2
                self.valid_middles.append(int(number_list[mid_ind]))
        print(sum(self.valid_middles))
        return sum(self.valid_middles)


    def reorder(self, list_item):
        seen = set()
        dupe = []
        for item in list_item:
            curr_index = list_item.index(item) 
            earliest_index = list_item.index(item)
            if item not in self.rules.keys():
                seen.add(item)
            else:
                for too_soon in self.rules[item]:
                    if too_soon in seen:
                        earliest_index = min(earliest_index, dupe.index(too_soon)) 
                seen.add(item)
            dupe.insert(earliest_index,item)
        return dupe


    def return_invalid_sum(self):
        replaced_lists = []
        for number_list in self.invalid_lists:
                mid_ind = len(number_list) // 2
                replace = self.reorder(number_list)
                replaced_lists.append(replace)
                self.invalid_middles.append(int(replace[mid_ind]))
        print(sum(self.invalid_middles))
        return sum(self.invalid_middles)


if __name__ == "__main__":
    with open("day04_input.py", "r") as f:
        true_input = f.read().strip("\n")
        puzzle = day5(true_input)
        puzzle.check_rules()
        puzzle.return_valid_sum()
        puzzle.return_invalid_sum()


