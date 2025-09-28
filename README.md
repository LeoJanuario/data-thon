# Projeto Datathon - Análise de Candidatos para Vagas

## 1\. Visão Geral do Projeto

[cite\_start]Este projeto foi desenvolvido como parte de um **Datathon da Pós Tech** [cite: 2][cite\_start], com o objetivo de criar uma solução de Inteligência Artificial para otimizar processos de recrutamento e seleção para a empresa **Decision**[cite: 7].

[cite\_start]A principal dor de negócio a ser resolvida é a dificuldade de encontrar o candidato ideal para cada vaga em tempo hábil[cite: 16]. [cite\_start]A solução proposta é um algoritmo de rankeamento de candidatos, que utiliza dados de vagas e perfis para sugerir os talentos mais alinhados[cite: 30].

### **Solução Proposta**

[cite\_start]O projeto consiste na construção de uma pipeline de machine learning completa [cite: 65][cite\_start], desde o pré-processamento dos dados até o deploy de um modelo preditivo em produção via API[cite: 66].

### **Stack Tecnológica**

  * [cite\_start]**Linguagem:** Python 3.X [cite: 68]
  * [cite\_start]**Frameworks de ML:** scikit-learn, pandas, numpy [cite: 69]
  * [cite\_start]**API:** FastAPI [cite: 70]
  * [cite\_start]**Serialização:** pickle ou joblib [cite: 43]
  * [cite\_start]**Empacotamento:** Docker e Docker Compose [cite: 73]

-----

## 2\. Estrutura do Projeto

[cite\_start]A estrutura de diretórios do projeto segue um padrão modular para facilitar a manutenção e o desenvolvimento[cite: 48].

```
.
├── datathonFiap/
[cite_start]│   ├── main.py        # Arquivo principal da API [cite: 79]
[cite_start]│   ├── routes.py      # Rotas e endpoints da API [cite: 79]
│   ├── dataReader.py  # Funções para carregar arquivos de dados (JSON)
│   ├── trainer.py     # Lógica de treinamento do modelo de rankeamento
[cite_start]│   ├── utils.py       # Funções auxiliares (extração de features) [cite: 49]
[cite_start]│   ├── prospects.json # Base de dados de candidatos inscritos em vagas [cite: 103]
[cite_start]│   ├── vagas.json     # Base de dados de vagas [cite: 103]
[cite_start]│   └── applicants.json # Base de dados de informações detalhadas dos candidatos [cite: 104]
[cite_start]├── Dockerfile         # Dockerfile para empacotar a API e dependências [cite: 52]
├── docker-compose.yml # Arquivo para orquestrar os containers
[cite_start]└── requirements.txt   # Dependências do projeto [cite: 84]
```

-----

## 3\. Instruções de Deploy (Como subir o ambiente)

[cite\_start]As instruções a seguir detalham como configurar e executar a aplicação usando Docker e Docker Compose[cite: 82].

### **Pré-requisitos**

  * [cite\_start]**Docker Desktop** (com Docker Compose) instalado e em execução[cite: 83].

### **Comandos para Executar a Aplicação**

1.  **Construir e Iniciar os Containers:**
    Navegue até o diretório raiz do projeto no terminal e execute o comando para construir as imagens e iniciar os serviços definidos no `docker-compose.yml`.

    ```bash
    docker-compose up --build
    ```

    Este comando iniciará dois serviços:

      * `data-api`: A API que serve os dados das bases JSON, na porta `8001`.
      * `main-api`: A API principal que contém a lógica de rankeamento, na porta `8000`.

2.  **Verificar o Status dos Containers:**
    Em um novo terminal, você pode verificar se ambos os serviços estão em execução:

    ```bash
    docker-compose ps
    ```

3.  **Parar a Aplicação:**
    Para parar os containers, use o seguinte comando:

    ```bash
    docker-compose down
    ```

-----

## 4\. Exemplos de Chamadas à API

[cite\_start]Você pode testar a funcionalidade da API usando ferramentas como o `curl` ou o Postman[cite: 51, 87].

### **Endpoint de Rankeamento (`/applicants_por_vaga/{vaga_id}`):**

Este endpoint recebe um ID de vaga e retorna uma lista de candidatos rankeados.

```bash
# Exemplo de requisição para a vaga com ID '5185'
curl http://localhost:8000/applicants_por_vaga/5185
```

**Output esperado:** Um JSON com os candidatos rankeados, baseados na lógica implementada no código.

### **Endpoints de Dados:**

Estes endpoints expõem os dados brutos das bases JSON e podem ser acessados na porta `8001`.

```bash
# Exemplo para obter dados de vagas
curl http://localhost:8001/vagas

# Exemplo para obter dados de prospects
curl http://localhost:8001/prospects

# Exemplo para obter dados de candidatos
curl http://localhost:8001/applicants
```
