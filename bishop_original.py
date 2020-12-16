import sys


def taking_input():
    string = []
    print("Enter 4 numbers such that 1 <= N <=8, where N "
          "is a positive integer")
    for i in range(4):
        try:
            get_num = int(input("Enter number %s: " % i))
            if not 1<= get_num <= 8:
                sys.exit(print("Number out of range..exiting"))
            string.append(get_num)

        except ValueError:
            print("wrong input...exiting!")
            sys.exit()
    print(string)
    return string



class cell:

    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist


def isInside(x, y, N):
    '''checks whether given position is
       inside the board'''
    if (x >= 1 and x <= N and
        y >= 1 and y <= N):
        return True
    return False

bishop_dx = [i for i in range(8)]
bishop_dy = [i for i in range(8)]
dx = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]
dy = [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
print(len(bishop_dx),len(bishop_dy))

def minimum_moves(dx,dy, bishop_dx, bishop_dy, initial, final, N):
    '''This function returns minimum steps to reach
       target position.'''
    stack = []
    stack2 = []
    stack.append(cell(initial[0], initial[1], 0))
    visited = [[False for i in range(N + 1)]
                      for j in range(N + 1)]
    visited[initial[0]][initial[1]] = True
    t = stack[-1]
    # print(t.x, t.y)
    if(t.x == final[0] and t.y == final[1]):
        return t.dist
    for i in range(len(bishop_dx)):
        x = t.x + bishop_dx[i]
        y = t.y + bishop_dy[i]
        if(isInside(x, y, N) and not visited[x][y]):
            visited[x][y] = True
            stack.append(cell(x, y, t.dist + 1))
    while(len(stack) > 0):
        k = stack[-1]
        stack.pop()
        if(k.x == final[0] and k.y == final[1]):
            return k.dist
        for i in range(len(dx)):
            x = k.x + dx[i]
            y = k.y + dy[i]
            if(isInside(x, y, N) and not visited[x][y]):
                visited[x][y] = True
                stack.append(cell(x, y, k.dist + 1))
                print(x,y)
                print(visited[x][y])







if __name__=='__main__':
    x1, y1, x2, y2 = taking_input()
    N = 8
    initial = [x1, y1]
    final = [x2, y2]
    print("Bishop's minimum moves: "+ str(minimum_moves(dx, dy, bishop_dx,
           bishop_dy ,initial, final, N)))
