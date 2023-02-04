"""
Write a program that will display the results of multiplication of two numbers (1-10).

We should use:
- nested for loop
- range function

Sample output:
1*1=1
1*2=2
...
3*4=12
...
10*10=100
"""

for a in range(1, 11):
    for b in range(1, 11):
        print(f'{a}*{b}={a*b}')
