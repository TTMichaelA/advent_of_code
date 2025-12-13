test_input = """2333133121414131402"""


class day9:

    def __init__(self,puzzle_input):
        self.input_map = self.process_input(puzzle_input)
        
    def process_input(self,inputstr):
        mapping = dict()
        counter = 0
        id = 0
        for i in range(len(inputstr)):
            blocklen = int(inputstr[i])
            if i % 2 == 1:
                counter += blocklen
                continue
            for j in range(blocklen):
                mapping[counter+j] = id
            counter += blocklen
            id += 1
        return mapping
    
    def fragment(self):
        left = 0
        right = max(self.input_map.keys())
        while left < right:
            if left in self.input_map.keys():
                left += 1
            else:
                self.input_map[left] = self.input_map[right]
                del self.input_map[right]
                right = max(self.input_map.keys())

    def calc_frag(self):
        summed_vals = 0
        for k, v in self.input_map.items():
            summed_vals += k * v
        return summed_vals
    

class day9pt2:

    def __init__(self,puzzle_input):
        self.blockmap = self.process_block_input(puzzle_input)

    def process_block_input(self, inputstr):
        blockmap = dict()
        block_ind = 0
        id = 0
        for i in range(len(inputstr)):
            blocklen = int(inputstr[i])
            if i % 2 == 1:
                blockmap[block_ind] = (blocklen, None)
                block_ind += blocklen
                continue
            blockmap[block_ind] = (blocklen, id)
            id += 1
            block_ind += blocklen
        return blockmap
    
    def move_block(self, oldind, newind):
        blocklen = self.blockmap[oldind][0]
        empty_blocklen = self.blockmap[newind][0]
        id = self.blockmap[oldind][1]
        if id is None:
            print("MOVING UNIDENTIFIED BLOCK")
            return 1
        else:
            self.blockmap[newind] = self.blockmap[oldind]
            del self.blockmap[oldind]
            if empty_blocklen > blocklen:
                self.blockmap[newind + blocklen] = (empty_blocklen - blocklen, None)

    def scan_for_block(self, blockind):
        blocklen = self.blockmap[blockind][0]
        i = 0
        
        while i < blockind:
            if i not in self.blockmap.keys():
                i += 1
                continue
            if self.blockmap[i][1] is not None:
                i += 1
                continue
            if self.blockmap[i][0] < blocklen:
                i += 1
                continue
            else:
                return i
    
    def fragment_blocks(self):
        seen_ids = set()
        right = max(self.blockmap.keys())

        while right >= 0:
            if right in self.blockmap.keys():
                if self.blockmap[right] not in seen_ids:
                    if self.blockmap[right][1] is not None:
                        seen_ids.add(self.blockmap[right][1])
                        new_place = self.scan_for_block(right)
                        if new_place is not None:
                            self.move_block(right, new_place)

            right -= 1

    def calc_blocksum(self):
        running_sum = 0
        for blockind, block in self.blockmap.items():
            if block[1] is None:
                continue
            else:
                for j in range(block[0]):
                    running_sum += (blockind + j) * block[1]
        return running_sum

            


if __name__ == "__main__":
    print(true_input)
    # instance = day9(test_input)
    # print(instance.input_map)
    # instance.fragment()
    # print(instance.calc_frag())
    instance2 = day9pt2(true_input)
    print(instance2.blockmap)
    instance2.fragment_blocks()
    print(instance2.calc_blocksum())

    