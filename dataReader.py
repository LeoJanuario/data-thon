from fastapi import FastAPI
import json

app = FastAPI()

# Função auxiliar para carregar os JSONs
def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def raiz():
    return {"API local rodando com FastAPI"}

@app.get("/vagas")
def get_dados1():
    return carregar_json("vagas.json")

@app.get("/applicants")
def get_dados2():
    return carregar_json("applicants.json")

@app.get("/prospects")
def get_dados3():
    return carregar_json("prospects.json")
