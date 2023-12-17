def print_kakuro_solution(n, solution):
    if solution:
        for i in range(n):
            for j in range(n):
                print(solution.get((i, j)), end=' ')
            print()
    else:
        print('No solution found')
