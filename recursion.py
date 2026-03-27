import math

def recursion_tree(n):
    level = 0
    total_cost = 0
    output_lines = []

    header = f"{'Level':<10}{'Subproblems':<15}{'Subproblem Size':<20}{'Cost at Level':<20}"
    print(header)
    print("-" * 65)

    output_lines.append(header)
    output_lines.append("-" * 65)

    while n >= 1:
        num_subproblems = 2 ** level
        subproblem_size = n
        cost_per_subproblem = subproblem_size ** 2
        cost_at_level = num_subproblems * cost_per_subproblem

        total_cost += cost_at_level

        row = f"{level:<10}{num_subproblems:<15}{subproblem_size:<20}{cost_at_level:<20}"
        print(row)

        output_lines.append(row)

        n = n // 2
        level += 1

    print("-" * 65)
    print(f"Total Cost T(n) = {total_cost}")

    output_lines.append("-" * 65)
    output_lines.append(f"Total Cost T(n) = {total_cost}")

    # Save to file
    with open("recursion_tree_output.txt", "w") as file:
        for line in output_lines:
            file.write(line + "\n")

    print("\nOutput saved to recursion_tree_output.txt")


# ---- Main Program ----
n = int(input("Enter value of n (power of 2 recommended): "))
recursion_tree(n)
