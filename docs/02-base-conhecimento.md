# Base de Conhecimento

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Organize a base de conhecimento do agente "Edu" usando os 4 arquivos da pasta `data/` (em anexo). Explique pra que serve cada arquivo e monte um exemplo de contexto formatado que será enviado pro LLM. Preencha o template abaixo.
>
> [cole ou anexe o template `02-base-conhecimento.md` pra contexto]

## Dados Utilizados

| Arquivo | Formato | Para que serve no Edu? |
|---------|---------|---------------------|
| `data/Inventario.csv` | CSV | quantidade de produto no estoque |
| `data/Productos.csv` | CSV | informação do produtos. |
| `data/Tiendas.csv` | CSV | informação da lojas. |
| `data/Tiendas.csv`| CSV | vendas do produtos. |

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd

inventario = pd.read_csv('./data/Inventario.csv')
produtos = pd.read_csv('./data/Productos.csv')
lojas = pd.read_csv('./data/Tiendas.csv')
vendas = pd.read_csv('./data/Vientas.csv')
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, agarntindo que o Agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informaçoes sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO INVENTARIO ('./data/Inventario.csv'):
ProductoID,StockActual
1,10


DADOS DOS PRODUTOS ('./data/Productos.csv'):
ProductoID,NombreProducto,Categoría,PrecioUnitario,CostoUnitario
1,Electrónica Blue 1,Electrónica,275.4,116.96

DADOS DAS LOJAS ('./data/Tiendas.csv'):
TiendaID,NombreTienda,Ciudad,Canal
1,Tienda 1,New Michael,Online


DADOS DAS VENDAS('./data/Vientas.csv'):
VentaID,Fecha,ProductoID,TiendaID,Cantidad,PrecioUnitario,Ingreso
1,2025-04-22,21,4,2,360.67,721.34
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montado abaixo, se baiseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
2. Estrutura dos Dados (Esquema)Para realizar cálculos e cruzamentos, utilize as seguintes chaves de ligação:

Produtos: ProductoID (PK), NombreProducto, Categoría (Eletrônica, Roupas, Brinquedos, Lar, Esportes), PrecioUnitario, CostoUnitario.
Lojas: TiendaID (PK), NombreTienda, Ciudad, Canal (Físico ou Online).Vendas: VentaID, Fecha, ProductoID (FK), TiendaID (FK), Cantidad, Ingreso.
Inventário: ProductoID (FK), StockActual.

2. Regras de Negócio e Cálculos ChaveAo realizar análises, considere as seguintes fórmulas:

Margem de Lucro Unitária: $PrecioUnitario - CostoUnitario$Lucro Total da Venda: $(PrecioUnitario - CostoUnitario) \times Cantidad$Status de Estoque:Crítico: Abaixo de 20 unidades (Ex: Produto 1, 24, 31, 39).Saudável: Acima de 100 unidades.
Período dos Dados: As vendas abrangem o final de 2024 e o primeiro semestre de 2025.

4. Insights Extraídos da Base

Categorias Principais: Eletrônica, Roupas, Brinquedos, Lar e Esportes.
Diversidade de Canais: Mix equilibrado entre lojas físicas e e-commerce(Online).
Ticket Médio: Os preços variam significativamente, com produtos de alto valor (ex: Eletrônica) e itens de giro rápido.


5. Diretrizes de RespostaSempre cruze os dados:

 Se perguntarem sobre vendas de um produto, verifique o estoque atual no Inventario.csv para dar uma recomendação completa.
 Foco em Rentabilidade: Priorize destacar produtos com maior margem, não apenas maior volume de vendas.
 Tom de Voz: Profissional, analítico e proativo. Se notar um estoque baixo em um produto de alta saída, avise o usuário imediatamente
```
