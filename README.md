# 🪙 Bitcoin ETL Pipeline

## 📝 Descrição do Projeto
Este projeto implementa um pipeline ETL (Extract, Transform, Load) que coleta dados históricos do Bitcoin em intervalos de 15 minutos. Os dados são inicialmente armazenados em um banco NoSQL (TinyDB) e posteriormente migrados para um banco PostgreSQL hospedado no Render. A visualização dos dados é feita através de um dashboard no Streamlit.

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Requests (para chamadas API)
- TinyDB (banco NoSQL local)
- PostgreSQL (banco de dados final)
- Streamlit (dashboard)
- Render (hospedagem do banco PostgreSQL)

## 📊 Funcionalidades
- Extração de dados do Bitcoin a cada 15 minutos
- Armazenamento temporário em TinyDB
- Migração automática para PostgreSQL
- Dashboard interativo com Streamlit
- Histórico de preços do Bitcoin
- Análises estatísticas básicas

## 🚀 Como Executar o Projeto

### Pré-requisitos
pip install requests tinydb psycopg2-binary streamlit python-dotenv

### Configuração do Ambiente
1. Clone o repositório
git clone https://github.com/seu-usuario/bitcoin-etl.git
cd bitcoin-etl

2. Configure as variáveis de ambiente (.env)
DATABASE_URL=sua_url_do_render_postgres
API_KEY=sua_chave_api_se_necessario

### Executando o Pipeline
python etl_pipeline.py

### Iniciando o Dashboard
streamlit run dashboard.py

## 📁 Estrutura do Projeto
bitcoin-etl/
├── etl_pipeline.py # Script principal do ETL
├── database.py # Configurações dos bancos de dados
├── api_handler.py # Gerenciamento de chamadas API
├── dashboard.py # Interface Streamlit
├── .env # Variáveis de ambiente
└── README.md

## 📈 Fluxo de Dados
1. Extração: Coleta de dados via API a cada 15 minutos
2. Transformação: Limpeza e formatação dos dados
3. Carga: 
   - Armazenamento inicial em TinyDB
   - Migração para PostgreSQL no Render
4. Visualização: Dashboard Streamlit

## 🔍 Monitoramento
- Logs de execução do ETL
- Métricas de sucesso/falha das extrações
- Monitoramento de latência do banco de dados

## 📝 Notas de Uso
- O pipeline está configurado para executar a cada 15 minutos
- Os dados históricos são mantidos no PostgreSQL
- O dashboard atualiza automaticamente com novos dados

## 👥 Contribuição
Sinta-se à vontade para contribuir com o projeto:
1. Faça um Fork
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato
Breno Teodomiro - [insights.jobs.ia@gmail.com]