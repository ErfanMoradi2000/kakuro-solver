from solver.kakuro import KakuroCSP
from solver.utils import print_kakuro_solution


sum_groups1 = {
   ((0, 0), (0, 1)): 15,  # Row 1
   ((1, 0), (1, 1)): 4,  # Row 2
   ((0, 0), (1, 0)): 12,  # Column 1
   ((0, 1), (1, 1)): 7,  # Column 2
}
kakuro1 = KakuroCSP(size=2, sum_groups=sum_groups1)
solution1 = kakuro1.backtracking_search()
print_kakuro_solution(2, solution1)


sum_groups2 = {
    ((0, 0), (0, 1), (0, 2)): 19,  # Row 1
    ((1, 0), (1, 1), (1, 2)): 11,  # Row 2
    ((2, 0), (2, 1), (2, 2)): 7,  # Row 3
    ((0, 0), (1, 0), (2, 0)): 20,  # Column 1
    ((0, 1), (1, 1), (2, 1)): 10,  # Column 2
    ((0, 2), (1, 2), (2, 2)): 7,  # Column 3
}
kakuro2 = KakuroCSP(size=3, sum_groups=sum_groups2)
solution2 = kakuro2.backtracking_search()
print_kakuro_solution(3, solution2)
