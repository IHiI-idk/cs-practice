print('Ввод:')
threshold = float(input())
n = int(input())
mx = -99999999999999
er_cnt = cnt = sr = 0
for i in range(n):
    a = input()
    if a != 'error':
        a = float(a)
        if a > threshold:
            cnt += 1
        sr += a
        if a > mx:
            mx = a
    else:
        er_cnt += 1