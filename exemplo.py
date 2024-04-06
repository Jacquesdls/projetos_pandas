import pandas as pd

cidades = pd.Series(['Itapevi', 'Rio de Janeiro', 'BH', \
    'Santo André', 'Itaquaquecetuba', 'Carapicuíba', 'Barueri', 'Itu', \
        'São paulo'])

populacao = pd.Series([260000, 6700000, 2700000, 720000, 80000, \
                        400000, 276000, 175000, 12000000])

data_frame = pd.DataFrame({'Cidade ': cidades, 'População ': populacao})

print(data_frame)

populacao_cidades = dict(zip(cidades, populacao))
print(populacao_cidades)

print(type(populacao_cidades))

print(populacao_cidades['São paulo'])
del populacao_cidades['Carapicuíba']
print('BH' in populacao_cidades)

data_frame.to_csv('data_frame.csv')

populacao_cidades = pd.read_csv('data_frame.csv', index_col = 0)

print(populacao_cidades)

print(populacao_cidades.info())

print(populacao_cidades.columns)

print(populacao_cidades.index)

print(populacao_cidades.head())

print(populacao_cidades.describe())

print(populacao_cidades.tail())










