"""
aula sobre count - Itertools 
"""

from itertools import count as co #importar

cont= co(start=3, step=0.2) # interador sem fim

'''
for v in cont:
    print(round(v, 2) ,end=', ')
    
    if v >=10:
        break
'''
# exemplo com lista
c= co()
lis = ['Caio','Felipe' ,'José', 'Antonio']
lis = zip(c,lis)
print(dict(lis))