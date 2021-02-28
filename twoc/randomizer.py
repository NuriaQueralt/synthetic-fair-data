# @name: randomizer.py
# @description: Script to generate random synthetic fair data
# @version: 1.0
# @date: 28-02-2021
# @author: Núria Queralt Rosinach
# @email: n.queralt_rosinach@lumc.nl

# TODO: code to generate synthetic fair data
"""Script to generate synthetic fair data from experimental design 1 ( random numbers of PGE2 on defined conditions ) for twoc"""

N = 5000
S_noticu = N - N*0.02
S_icu = N*0.02

print("Number of patients: {}".format(N))
print("Number of not severe patients (not icu): {}, severe(icu): {}".format(S_noticu, S_icu))
print("Number of not severe patients on D: {}, severe not in D: {}".format(S_noticu*0.9, S_noticu + S_icu*0.9))

i = 1
while i <= N:
#for i in range(N):
    print(i)
    if i <= S_noticu:
       S = 0
       if i <= S_noticu*0.9:
          M = 1
       else:
          M = 0
       P = "gaussian value"
    else:   
       S = 1
       if i <= S_noticu + S_icu*0.9:
          M = 0
       else:
          M = 1
       P = "skewed value"
    
    print("i: {}, S: {}, M: {}, P:{}".format(i, S, M, P))
    i += 1
