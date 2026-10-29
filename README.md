# Fome Zero

Projeto de análise de dados sobre restaurantes de diferentes países, desenvolvido com Python e Streamlit.

### 1. Problema de negócio

A Fome Zero é um marketplace fictício de restaurantes que reúne informações de estabelecimentos localizados em diferentes cidades e países.

Com muitos restaurantes cadastrados, fica mais difícil acompanhar quais regiões possuem mais opções, quais culinárias aparecem com maior frequência, como estão as avaliações e quais restaurantes se destacam.

O desafio deste projeto foi organizar esses dados em um dashboard para facilitar a consulta das principais informações sobre os restaurantes.

Com a ferramenta, é possível analisar indicadores como quantidade de restaurantes, cidades e países cadastrados, tipos de culinária, preços médios, avaliações e localização dos estabelecimentos.

### 2. Premissas assumidas para a análise

1. A análise foi realizada com a base de dados `zomato.csv`, que contém informações sobre restaurantes localizados em diferentes países.

2. Os registros com informações ausentes foram removidos para evitar resultados incompletos nos gráficos e indicadores.

3. Os dados duplicados também foram removidos durante o tratamento da base.

4. Para os restaurantes que possuem mais de um tipo de culinária cadastrado, foi considerado apenas o primeiro tipo informado.

5. As categorias “Drinks Only” e “Mineira” foram retiradas da análise.

6. Os valores de preço médio para duas pessoas foram mantidos na moeda original de cada país. Portanto, essa métrica deve ser analisada com cuidado ao comparar países diferentes.

### 3. Estratégia da solução

A solução foi desenvolvida como um dashboard interativo em Streamlit, dividido em quatro páginas.

- **Visão geral:** resumo da base, indicadores e mapa dos restaurantes.
- **Visão por países:** quantidade de restaurantes e cidades, média de votos e preço médio para duas pessoas.
- **Visão por cidades:** cidades com mais restaurantes, melhores e piores avaliações e variedade de culinárias.
- **Visão por culinárias:** restaurantes em destaque e rankings das culinárias com maiores e menores avaliações médias.

Em todas as páginas, é possível filtrar os dados por país.

### 4. Métricas utilizadas

#### Visão geral

- Quantidade de restaurantes cadastrados;
- Quantidade de países;
- Quantidade de cidades;
- Total de votos recebidos;
- Quantidade de tipos de culinária;
- Localização dos restaurantes no mapa.

#### Visão por países

- Quantidade de restaurantes por país;
- Quantidade de cidades por país;
- Média de votos por país;
- Preço médio para duas pessoas por país.

#### Visão por cidades

- Cidades com maior quantidade de restaurantes;
- Cidades com mais restaurantes com nota maior ou igual a 4;
- Cidades com mais restaurantes com nota menor ou igual a 2,5;
- Cidades com maior variedade de culinárias.

#### Visão por culinárias

- Restaurantes mais bem avaliados por tipo de culinária;
- Ranking das culinárias com maiores avaliações médias;
- Ranking das culinárias com menores avaliações médias;
- Lista de restaurantes de acordo com os países e culinárias selecionados.

### 5. Top 3 insights de dados

1. A Índia concentra 3.111 restaurantes, aproximadamente 44,9% dos registros analisados. Os Estados Unidos aparecem em seguida, com 1.374 restaurantes.

2. A culinária North Indian é a mais frequente na base, com 878 restaurantes. Em seguida aparecem American, com 520, e Cafe, com 465.

3. A Indonésia apresentou a maior média de avaliação, com nota 4,60. O Brasil apresentou a menor média, com 3,34. Esse resultado considera somente os restaurantes presentes na base utilizada no projeto.

### 6. O produto final do projeto

O produto final é um dashboard interativo desenvolvido em Streamlit e hospedado na nuvem.

A ferramenta permite consultar informações sobre restaurantes, países, cidades e tipos de culinária por meio de gráficos, indicadores, filtros e um mapa com a localização dos estabelecimentos.

**Link do dashboard:** https://fome-zero-projects-je.streamlit.app/

### 7. Conclusão

O projeto permitiu organizar os dados da Fome Zero em um dashboard interativo, facilitando a análise de informações sobre restaurantes de diferentes países.

Por meio das páginas do painel, é possível comparar a quantidade de restaurantes, cidades, culinárias, avaliações, preços e localizações dos estabelecimentos.

### 8. Próximos passos

1. Criar filtros por cidade e faixa de avaliação para permitir análises mais específicas.

2. Converter os preços para uma mesma moeda, facilitando a comparação entre países diferentes.

3. Adicionar indicadores sobre reserva de mesa e entrega online, informações que já estão disponíveis na base de dados.

4. Atualizar a base de dados para manter as informações apresentadas no dashboard mais recentes.
