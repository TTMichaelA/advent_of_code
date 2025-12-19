t1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
t2 = "U62,R66,U55,R34,D71,R55,D58,R83"


def main():
    pass


if __name__ == "__main__":
    with open("day03.txt") as pi:
        for i, pie in enumerate(pi):
            if i == 1:
                t1 = pie
            else:
                t2 = pie
        
    wire1 = t1.split(",")
    wire2 = t2.split(",")
    coords = set()
    cnt = {}
    pos = (0,0)
    cnt[pos] = 0
    dist = None
    best_cnt = None
    movements = {'U': (1,0), 'D':(-1,0), 'L':(0,-1), 'R': (0,1)}
    cum_cnt = 0
    for w in wire1:
        move = movements[w[0]]
        num = int(w[1:])
        while num > 0:
            pos = (pos[0] + move[0], pos[1] + move[1])
            coords.add(pos)
            cum_cnt += 1
            cnt[pos] = cum_cnt
            num -=1
    pos = (0,0)
    cum_cnt = 0
    for w in wire2:
        move = movements[w[0]]
        num = int(w[1:])
        while num > 0:
            pos = (pos[0] + move[0], pos[1] + move[1])
            num -= 1
            cum_cnt += 1
            if pos in coords:
                dist2 = abs(pos[0]) + abs(pos[1])
                if not dist or dist2 < dist:
                    dist = dist2
                sum_cnt = cum_cnt + cnt[pos]
                if not best_cnt or sum_cnt < best_cnt:
                    best_cnt = sum_cnt
                
    print(dist)
    print(best_cnt)