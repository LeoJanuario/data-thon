from fastapi import APIRouter
import requests
import traceback
from utils import extrair_features
from trainer import rank_prospects

router = APIRouter()
API_BASE = "http://data-api:8000" 

@router.get("/applicants_por_vaga/{vaga_id}")
def applicants_por_vaga(vaga_id: str):
    try:
        vagas_data = requests.get(f"{API_BASE}/vagas", timeout=15).json()
        prospects_data = requests.get(f"{API_BASE}/prospects", timeout=15).json()
        applicants_data = requests.get(f"{API_BASE}/applicants", timeout=15).json()
    except Exception as e:
        return {"erro": f"Não foi possível acessar a API principal: {str(e)}"}

    try:
        # Seleciona vaga e perfil
        vaga = {}
        if isinstance(vagas_data, dict):
            vaga = vagas_data.get(vaga_id, {})
        elif isinstance(vagas_data, list):
            vaga = next((v for v in vagas_data if v.get("id") == vaga_id), {})

        perfil_vaga = vaga.get("perfil_vaga", {})

        # Seleciona prospects
        prospects_vaga, titulo_vaga = [], ""
        if isinstance(prospects_data, dict):
            vaga_prospect = prospects_data.get(vaga_id, {})
            prospects_vaga = vaga_prospect.get("prospects", [])
            titulo_vaga = vaga_prospect.get("titulo", "")
        elif isinstance(prospects_data, list):
            vaga_prospect = next((p for p in prospects_data if p.get("id") == vaga_id), {})
            prospects_vaga = vaga_prospect.get("prospects", [])
            titulo_vaga = vaga_prospect.get("titulo", "")

        if not prospects_vaga:
            return {"vaga_id": vaga_id, "prospects_rankeados": []}

        all_features, valid_prospects = [], []
        for prospect in prospects_vaga:
            codigo_applicant = prospect.get("codigo")
            applicant_data = {}
            if isinstance(applicants_data, dict):
                applicant_data = applicants_data.get(codigo_applicant, {}).get("infos_basicas", {})
            elif isinstance(applicants_data, list):
                app_item = next((a for a in applicants_data if a.get("codigo") == codigo_applicant), {})
                applicant_data = app_item.get("infos_basicas", {})

            if applicant_data:
                features = extrair_features(applicant_data, perfil_vaga)
                all_features.append(features)
                prospect_copy = prospect.copy()
                prospect_copy["titulo_prospect"] = titulo_vaga
                prospect_copy["applicant"] = applicant_data
                valid_prospects.append(prospect_copy)

        sorted_prospects = rank_prospects(valid_prospects, all_features)
        return {"vaga_id": vaga_id, "prospects_rankeados": sorted_prospects}

    except Exception as e:
        return {"erro": str(e), "trace": traceback.format_exc()}
