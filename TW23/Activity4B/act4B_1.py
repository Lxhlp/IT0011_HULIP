A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'h', 'i', 'j', 'k', 'd', 'f'}

# A. How many elements are there in set A and B
print(f"A. \nNumber of elements in A: {len(A)} \nNumber of elements in B: {len(B)}\n")

# B. How many elements are there in B that is not part of A and C
not_A_and_C = B - (A.union(C))
print(f"B. \nNumber of elements in B not in A and C: {len(not_A_and_C)}\n")

# C. Show the following using set operations
# i. [h, i, j, k]
result_i = C - A
print(f"C.\nI. {list(result_i)}")

# ii. [c, d, f]
result_ii = A.intersection(C)
print(f"II. {list(result_ii)}")

# iii. [b, c, h]
result_iii = (A.intersection(B)).union(B.intersection(C))
print(f"III. {list(result_iii)}")

# iv. [d, f]
result_iv = A.intersection(C) - {'c'}
print(f"IV. {list(result_iv)}")

# v. [c]
result_v = A.intersection(B).intersection(C)
print(f"V. {list(result_v)}")

# vi. [l, m, o]
result_vi = (B-A)-C
print(f"VI. {list(result_vi)}")