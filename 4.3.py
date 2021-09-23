import random

list_sotunhien = {}
for i in range(10):
    sotunhienduoctao = random.randint(1,10)
    i +=1
    list_sotunhien.update({str(i) : sotunhienduoctao})
    
print(list_sotunhien)