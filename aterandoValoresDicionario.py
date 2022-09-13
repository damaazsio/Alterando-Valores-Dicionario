import copy
d1 = {'chave1': 'VALOR1', 'chave2': 'VALOR2', 'chave3' : ('outras' 'coisas')}

v = copy.deepcopy(d1)

v['chave3'] ='francisco', 'damasio'

v['chave1'] = 'Willy'

print(d1)
print(v)