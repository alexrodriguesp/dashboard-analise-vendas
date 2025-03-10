# dashboard-analise-vendas
Projeto em Python para análise de vendas e visualização de dados interativa.


Este projeto é uma ferramenta em Python que ajuda a analisar dados de vendas e visualizar os resultados de forma simples e interativa. Com este dashboard, você poderá facilmente entender como estão as vendas dos seus produtos e tomar decisões mais rápidas e assertivas!

🚀 Funcionalidades
Análise de Vendas: Mostra os totais de vendas por categoria de produtos.
Gráficos Interativos: Exibe gráficos fáceis de entender sobre o desempenho das vendas.
Interface Simples: Não é necessário instalar ou configurar nada. O dashboard será executado com apenas um clique.

🧑‍💻 Tecnologias Usadas
Este projeto foi feito utilizando as seguintes tecnologias:
Python: Linguagem de programação utilizada para processar os dados.
Pandas: Biblioteca para manipulação dos dados.
Matplotlib & Seaborn: Bibliotecas para criar gráficos.
Streamlit: Ferramenta para criar o dashboard de forma simples e interativa.

📂 Estrutura do Projeto
app.py: Código principal que executa o dashboard.
vendas.xlsx: Arquivo de dados que contém informações sobre as vendas (ex: produtos, categoria e total de vendas).
requirements.txt: Lista de bibliotecas necessárias para rodar o projeto.

🛠 Como Usar (Passo a Passo)
Para Usuários Avançados (com Python instalado)
Clone ou baixe o projeto:

Se você tem experiência com Git, pode clonar o repositório diretamente.
Caso contrário, baixe o arquivo ZIP e extraia em seu computador.
Instale as dependências:

Abra o terminal (prompt de comando no Windows ou terminal no macOS/Linux) e navegue até a pasta do projeto.
Execute o seguinte comando para instalar as bibliotecas necessárias:

pip install -r requirements.txt

Execute o Dashboard:
No terminal, rode o seguinte comando para abrir o dashboard:

streamlit run app.py

Abra no Navegador:
Após rodar o comando, o dashboard será aberto automaticamente no seu navegador. Caso não abra, acesse http://localhost:8501


📊 Como Funciona
Após abrir o dashboard, você verá uma tela com:
Tabela de Dados: Uma tabela exibindo as informações de vendas, como o nome do produto, a categoria e o número de vendas.
Gráfico de Vendas por Categoria: Um gráfico de barras que mostra o total de vendas por cada categoria de produto (ex: Eletrônicos, Acessórios, Móveis, etc.).
Filtros Interativos: Você pode selecionar diferentes categorias de produtos e visualizar apenas as vendas daquela categoria específica.

⚙️ Personalizações (Para Usuários Avançados)
Se você tem conhecimento em Python e deseja personalizar o dashboard, basta editar o arquivo app.py:
Alterar os Dados: Você pode substituir o arquivo vendas.xlsx por outro arquivo de dados (deve estar no formato Excel).
Adicionar Novos Gráficos: Utilize bibliotecas como Matplotlib e Seaborn para criar novos gráficos e visualizações.


