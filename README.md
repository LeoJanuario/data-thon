# Projeto Datathon - Análise de Candidatos para Vagas

## 1. Visão Geral do Projeto

Este projeto foi desenvolvido como parte de um **Datathon da Pós Tech**, com o objetivo de criar uma solução de Inteligência Artificial para otimizar processos de recrutamento e seleção para a empresa **Decision**.

A principal dor de negócio a ser resolvida é a dificuldade de encontrar o candidato ideal para cada vaga em tempo hábil. A solução proposta é um algoritmo de rankeamento de candidatos, que utiliza dados de vagas e perfis para sugerir os talentos mais alinhados.

### **Solução Proposta**

O projeto consiste na construção de uma pipeline de machine learning completa, desde o pré-processamento dos dados até o deploy de um modelo preditivo em produção via API.

### **Stack Tecnológica**

* **Linguagem:** Python 3.X
* **Frameworks de ML:** scikit-learn, pandas, numpy
* **API:** FastAPI
* **Serialização:** pickle ou joblib
* **Empacotamento:** Docker e Docker Compose

---

## 2. Estrutura do Projeto

A estrutura de diretórios do projeto segue um padrão modular para facilitar a manutenção e o desenvolvimento.

```

.
├── datathonFiap/
│   ├── main.py        \# Arquivo principal da API
│   ├── routes.py      \# Rotas e endpoints da API
│   ├── dataReader.py  \# Funções para carregar arquivos de dados (JSON)
│   ├── trainer.py     \# Lógica de treinamento do modelo de rankeamento
│   ├── utils.py       \# Funções auxiliares (extração de features)
│   ├── prospects.json \# Base de dados de candidatos inscritos em vagas
│   ├── vagas.json     \# Base de dados de vagas
│   └── applicants.json \# Base de dados de informações detalhadas dos candidatos
├── Dockerfile         \# Dockerfile para empacotar a API e dependências
├── docker-compose.yml \# Arquivo para orquestrar os containers
└── requirements.txt   \# Dependências do projeto

````

---

## 3. Instruções de Deploy (Como subir o ambiente)

As instruções a seguir detalham como configurar e executar a aplicação usando Docker e Docker Compose.

### **Pré-requisitos**

Para rodar a aplicação, você precisa ter o **Docker Desktop** instalado e em execução na sua máquina.

* **[Baixe o Docker Desktop](https://www.docker.com/products/docker-desktop/)**

---
* **Docker Desktop** (com Docker Compose) instalado e em execução.

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

---

## 4. Exemplos de Chamadas à API

Você pode testar a funcionalidade da API usando ferramentas como o `curl` ou o Postman.

### **Endpoint de Rankeamento (`/applicants_por_vaga/{vaga_id}`):**

Este endpoint recebe um ID de vaga e retorna uma lista de candidatos rankeados.

```bash
# Exemplo de requisição para a vaga com ID '5185'
curl http://localhost:8000/applicants_por_vaga/5185
````

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
