def mostra_argumentos_nomeados(*args,**kwargs):
  for key, value in kwargs.items():
    print(key, value)


mostra_argumentos_nomeados(1,nome='vilner',idade=14)

configuracoes = {
    'config1': 1,
    'config2': 2,
    'config3': 3,
    'config4': 4,
}

mostra_argumentos_nomeados(**configuracoes)
'''dict = {
    'nome1': 'Vilner',
    'nome2': 'Genildi',
    'nome3': 'Adalia',
}



dict2 = {
    'nome4': 'R9',
    'nome5': 'N10',
    'nome6': 'R11',
}
dict3 = {
    **dict2, 
    **dict,
    'nome7':'Wallace',
    'nome': {'chave1':'valor1'},
}
dict4,*dic5 = dict.items()

print(dict4,dic5)'''