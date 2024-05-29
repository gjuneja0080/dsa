class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        facing = 0
        x, y = 0, 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for inst in instructions:
            if inst == 'G':
                x += directions[facing][0]
                y += directions[facing][1]
            elif inst == 'L':
                facing = (facing + 3) % 4
            elif inst == 'R':
                facing = (facing + 1) % 4
        return (x == 0 and y == 0) or facing != 0
