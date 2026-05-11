# Heuristic Function
def calculate_cost(mat, goal):

    cost = 0

    for i in range(3):
        for j in range(3):

            if mat[i][j] != 0 and \
               mat[i][j] != goal[i][j]:

                cost += 1

    return cost


# Convert matrix to string
def matrix_to_string(mat):

    s = ""

    for row in mat:
        for val in row:

            s += str(val)

    return s


# Print matrix
def print_matrix(mat):

    for row in mat:

        for val in row:

            print(val,end=" ")

        print()


# A* Algorithm
def astar(start, goal, x, y):

    open_list = []

    visited = []

    # Node format:
    # [f, level, matrix, x, y]

    cost = calculate_cost(start, goal)

    open_list.append(
        [cost,0,start,x,y]
    )

    row = [-1,1,0,0]
    col = [0,0,-1,1]

    while len(open_list) > 0:

        # Find minimum f(n)
        min_index = 0

        for i in range(len(open_list)):

            if open_list[i][0] + \
               open_list[i][1] < \
               open_list[min_index][0] + \
               open_list[min_index][1]:

                min_index = i

        current = open_list.pop(min_index)

        mat = current[2]
        x = current[3]
        y = current[4]
        level = current[1]

        print("\nCurrent State:")
        print_matrix(mat)

        # Goal Check
        if calculate_cost(mat,goal)==0:

            print("\nGoal State Reached")
            return

        state = matrix_to_string(mat)

        if state in visited:
            continue

        visited.append(state)

        # Generate child states
        for i in range(4):

            newx = x + row[i]
            newy = y + col[i]

            if newx>=0 and newx<3 and \
               newy>=0 and newy<3:

                temp = []

                for r in mat:
                    temp.append(r[:])

                # Swap
                temp[x][y],temp[newx][newy] = \
                temp[newx][newy],temp[x][y]

                child = matrix_to_string(temp)

                if child not in visited:

                    cost = calculate_cost(
                        temp,goal
                    )

                    open_list.append(
                        [cost,
                         level+1,
                         temp,
                         newx,
                         newy]
                    )


# Main
start = []

goal = []

print("Enter Start State:")

x = 0
y = 0

for i in range(3):

    row = list(
        map(int,input().split())
    )

    start.append(row)

    for j in range(3):

        if start[i][j] == 0:

            x = i
            y = j


print("Enter Goal State:")

for i in range(3):

    row = list(
        map(int,input().split())
    )

    goal.append(row)


astar(start,goal,x,y)