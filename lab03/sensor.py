threshold = float(input())
n = int(input())
mx = -99999999999999
er_cnt = cnt = sr = 0
for i in range(n):
    a = input()
    if a != 'error':
        a = float(a)
        sr += a
        if a > threshold:
            cnt += 1
        if a > mx:
            mx = a
    else:
        er_cnt += 1
print(n)
print(er_cnt)
print(cnt)
print(f'{mx:.1f}')
print(f'{(sr/n):.1f}')
print(f'{(sr/n):.1f}')