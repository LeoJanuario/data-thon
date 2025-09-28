from fastapi import FastAPI
from routes import router

app = FastAPI(title="API Rankeamento de Candidatos")

# inclui as rotas
app.include_router(router)
