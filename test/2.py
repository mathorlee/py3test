#coding=utf8
'''
Created on 2018年9月20日

@author: Administrator
'''

# lanqiu = [True] * 7
# lanqiu[0] = False
# yumao = [True] * 7
# yumao[1] = False
# zhuo = [True] * 7
# zhuo[3] = False
# swim = [True] * 7
# swim[1] = swim[3] = swim[5] = False
# 
# test_cases = [
#     [swim, lanqiu, yumao, zhuo],
#     [lanqiu, yumao, swim, zhuo],
#     [swim, yumao, lanqiu, zhuo],
#     [zhuo, swim, yumao, lanqiu],
# ]
# 
# def check_case(case):
#     def step(x, y):
#         return (x + y) % 7
#     
#     for today in range(7):
#         arr = case[0]
#         if not(arr[today] and arr[step(today, 1)] == False):
#             continue
#         
#         arr = case[1]
#         if not(arr[today] and arr[step(today, 1)]):
#             continue
#         
#         arr = case[2]
#         if not(arr[today] and arr[step(today, -2)]):
#             continue
#         
#         arr = case[3]
#         if not(all(arr[:today + 1])):
#             continue
#         
#         print('today: %s' % today)
#         return True
#     
#     return False
# 
# for i in range(len(test_cases)):
#     if check_case(test_cases[i]):
#         print(i)

n = 0
m = 0

for i in range(2**16):
    j = i
    one_cnt = 0
    
    digits = []
    while j:
        digits.append(j % 2)
        j >>= 1
    
    for j in range(len(digits)):
        if digits[j]:
            one_cnt += 1
    if one_cnt != 8:
        continue
    
    legal = True
    one_cnt = 0
    for j in range(len(digits)):
        if digits[j]:
            one_cnt += 1
        if one_cnt < j + 1 - one_cnt:
            legal = False
            break
    
    if legal:
        m += 1
    n += 1

print(n, m)
    