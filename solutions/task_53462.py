# Student ID : 53462
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the absolute difference between the sum of even digits and the sum of odd digits.║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_53462.py


def solve(id: str) -> int:
    odd_sum = 0
    even_sum = 0
    
    for char in id:
        digit = int(char)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
            
    return abs(even_sum - odd_sum)
