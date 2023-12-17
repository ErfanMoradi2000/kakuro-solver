class KakuroCSP:

    def __init__(self, size, sum_groups):
        self.variables = [(i, j) for i in range(size) for j in range(size)]
        self.domains = {v: set(range(1, 10)) for v in self.variables}
        self.sum_groups = sum_groups
        self.assignment = {}

    def update_domains(self):
        for group in self.sum_groups:
            possible_numbers = self.sum_groups[group]
            for cell in group:
                self.domains[cell] = self.domains[cell] & possible_numbers

    def is_consistent(self, var, assignment, value):
        assignment_copy = assignment.copy()
        assignment_copy[var] = value

        for group, target_sum in self.sum_groups.items():
            group_values = list(filter(None, [assignment_copy.get(v) for v in group]))

            if len(group_values) != len(set(group_values)):
                return False

            if sum(group_values) > target_sum:
                return False

            if set(group).issubset(set(assignment_copy)) and sum(group_values) != target_sum:
                return False

        return True

    def get_legal_values(self, var, assignment):
        if var in assignment:
            return []

        legal_values = set(range(1, 10))
        for group in self.sum_groups:
            if var in group:
                group_vals = [assignment[v] for v in group if v in assignment]
                legal_values -= set(group_vals)

                target_sum = self.sum_groups[group]
                max_possible_val = target_sum - sum(group_vals)
                legal_values = {val for val in legal_values if val <= max_possible_val}

        return legal_values

    def forward_check(self, var, value, assignment):
        pruned = {}
        for group in self.sum_groups:
            if var in group:
                for neighbor in group:
                    if neighbor != var and neighbor not in assignment:
                        if value in self.domains[neighbor]:
                            if neighbor not in pruned:
                                pruned[neighbor] = set()
                            pruned[neighbor].add(value)
                            self.domains[neighbor].remove(value)
        return pruned

    def backtrack(self, pruned):
        for neighbor, values in pruned.items():
            self.domains[neighbor].update(values)

    def backtracking_search(self, pruned=None):
        assignment = self.assignment
        if pruned is None:
            pruned = {}

        if len(assignment) == len(self.variables):
            return assignment

        var = min([v for v in self.variables if v not in assignment],
                  key=lambda v: len(self.get_legal_values(v, assignment)))

        for value in self.get_legal_values(var, assignment):
            if not self.is_consistent(var, assignment, value):
                continue

            assignment[var] = value
            pruned[var] = self.forward_check(var, value, assignment)

            result = self.backtracking_search(pruned)
            if result is not None:
                return result

            self.backtrack(pruned[var])
            del pruned[var]
            del assignment[var]

        return None
