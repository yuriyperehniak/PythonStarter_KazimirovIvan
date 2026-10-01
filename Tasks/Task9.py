# Знайти кількість N-значних чисел, у яких сума цифр дорівнює їхньому добутку.
# Також виведіть найменше таке число для заданого N, де 1≤N<10.

N = int(input())
count = 0
min_num = None
if N == 1:
    print("10 0")
else:
    for num in range(10**(N-1), 10**N):
        digits = []
        for d in str(num):
            digits.append(int(d))
        s = sum(digits)
        p = 1
        for d in digits:
            p *= d

        if s == p:
            count += 1
            if min_num is None:
                min_num = num
    print(f"{count} {min_num}")