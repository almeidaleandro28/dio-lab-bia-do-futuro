import pandas as pd


inventario = pd.read_csv('./data/Inventario.csv')
produtos = pd.read_csv('./data/Productos.csv')
lojas = pd.read_csv('./data/Tiendas.csv')
vendas = pd.read_csv('./data/Ventas.csv')

print( vendas)