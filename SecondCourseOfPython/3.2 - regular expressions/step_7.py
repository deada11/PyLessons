import re
import sys
pattern = r'((cat).*){2}'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

# N = int(input())
# A = [True]*N
# print(A)
# A[0] = A[1] = False
# for k in range(2, N):
#     if A[k]:
#         for m in range(2*k, N, k):
#             A[m] = False
#     print(k, '-', "простое" if A[k] else "составное")
# print(A)
