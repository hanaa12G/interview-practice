from pprint import pprint
class Solution:

    def makeState(self, t1, t2):
        return (t1, t2, )

    def numTilings(self, n):

        grid = {}
        MODULO = pow(10, 9) + 7

        tab_cnt = 0
        tab_char = '>'

        def step(i, t1, t2):
            nonlocal tab_cnt
            nonlocal tab_char

            tab_cnt += 1

            print(f'{tab_cnt * tab_char} step(i={i}, t1={t1}, t2={t2}')
            if i >= n:
                tab_cnt -= 1
                print(f'<- Accept')
                return 1

            state = self.makeState(t1, t2)
            if i in grid and state in grid[i]:
                tab_cnt -= 1
                print(f'<- Grid[{i}][{state}] = {grid[i][state]}')
                return grid[i][state]

            count = 0

            next_ = i + 1 < n


            if not t1 and not t2:
                # Try vertical domino
                count += step(i + 1, False, False)
                if next_:
                    # Try A-tromino
                    count += step(i + 1, False, True)
                    # Try B-tromino
                    count += step(i + 1, True, False)
                    # Try 2 horizontal domino, so next column will be occupied
                    count += step(i + 1, True, True)
            elif t1 and t2:
                count += step(i + 1, False, False)
            elif t1 and not t2:
                if next_:
                    # Try C-tromino
                    count += step(i + 1, True, True)
                    # Try horizontal domino
                    count += step(i + 1, False, True)
            else:
                if next_:
                    # Try D-tromino
                    count += step(i + 1, True, True)
                    # Try horizontal domino
                    count += step(i + 1, True, False)

            if i not in grid:
                grid[i] = {}
            grid[i][state] = count % MODULO

            tab_cnt -= 1

            return grid[i][state]

        

        return step(0, False, False)

if __name__ == "__main__":
    solution = Solution()
    print(f'numTilings(3) -> { solution.numTilings(3) }')
