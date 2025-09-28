import re
from datetime import datetime

def extrair_features(applicant, perfil_vaga):
    """
    Mesma lógica que você tinha antes: calcula vetor de features
    ponderando academic, inglês, espanhol, área, localidade e faixa etária.
    """
    features = []

    # Pesos
    peso_academico = 1
    peso_ingles = 2
    peso_espanhol = 1
    peso_area = 3
    peso_localidade = 2
    peso_faixa_etaria = 3

    # Nível acadêmico
    nivel_academico_vaga = perfil_vaga.get("nivel_academico", "").lower()
    nivel_academico_applicant = applicant.get("nivel_academico", "").lower()
    score_academico = 1 if nivel_academico_vaga and nivel_academico_vaga in nivel_academico_applicant else 0
    features.append(score_academico * peso_academico)

    # Inglês
    nivel_ingles_vaga = perfil_vaga.get("nivel_ingles", "").lower()
    nivel_ingles_applicant = applicant.get("nivel_ingles", "").lower()
    score_ingles = 0
    if nivel_ingles_vaga == "avançado":
        score_ingles = 1 if "avançado" in nivel_ingles_applicant else 0
    elif nivel_ingles_vaga == "intermediário":
        score_ingles = 1 if "intermediário" in nivel_ingles_applicant or "avançado" in nivel_ingles_applicant else 0
    elif nivel_ingles_vaga == "básico":
        score_ingles = 1
    features.append(score_ingles * peso_ingles)

    # Espanhol
    nivel_espanhol_vaga = perfil_vaga.get("nivel_espanhol", "").lower()
    nivel_espanhol_applicant = applicant.get("nivel_espanhol", "").lower()
    score_espanhol = 1 if nivel_espanhol_vaga and nivel_espanhol_vaga in nivel_espanhol_applicant else 0
    features.append(score_espanhol * peso_espanhol)

    # Área
    areas_vaga = perfil_vaga.get("areas_atuacao", "").lower()
    objetivo_prof = applicant.get("objetivo_profissional", "").lower()
    match_area = 1 if areas_vaga and any(k.strip() in objetivo_prof for k in areas_vaga.split(",")) else 0
    features.append(match_area * peso_area)

    # Estado
    localidade_vaga = perfil_vaga.get("estado", "").lower()
    local = applicant.get("local", "").lower()
    match_localidade = 0
    if localidade_vaga and "," in local:
        try:
            match_localidade = 1 if localidade_vaga == local.split(",")[1].strip() else 0
        except Exception:
            match_localidade = 0
    features.append(match_localidade * peso_localidade)

    # Faixa Etária
    faixa_etaria_vaga = perfil_vaga.get("faixa_etaria", "").lower()
    nascimento = applicant.get("data_nascimento", "")
    match_faixa_etaria = 0
    if faixa_etaria_vaga and nascimento:
        try:
            ano_nasc = int(nascimento.split("-")[0].strip())
            idade = datetime.now().year - ano_nasc
            numeros = re.findall(r"\d+", faixa_etaria_vaga)
            if len(numeros) >= 2:
                faixa_min, faixa_max = map(int, numeros[:2])
                match_faixa_etaria = 1 if faixa_min <= idade <= faixa_max else 0
        except Exception:
            match_faixa_etaria = 0
    features.append(match_faixa_etaria * peso_faixa_etaria)

    return features