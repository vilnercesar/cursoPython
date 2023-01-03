list = [
    {'nome':'Vilner César','sobrenome':'Oliveira'},
    {'nome':'Vitor  César','sobrenome':'Oliveira'},
    {'nome':'Vinicius César','sobrenome':'Oliveira'},
    {'nome':'Genildo César','sobrenome':'Oliveira'},
 
]
'''
def ordena(item):
    return item['nome']

list.sort(key=ordena)
print(list)'''

list.sort(key=lambda item: item['nome'])
print(list)

 