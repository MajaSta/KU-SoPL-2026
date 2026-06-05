# Student ID : 52696
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of all digits minus the minimum digit.   ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52696.py


def solve(id: str) -> int:
    """
    Implement your task here.
    Your id is passed as a string.
    Return an integer.
    """
    digits = [int(x) for x in id if x.isdigit()]
    return sum(digits) - min(digits)


if __name__ == "__main__":
    print(solve("52696"))
