python
CATEGORIAS = {
    "Acesso": ["senha", "login", "acesso", "bloqueado", "conta", "e-mail", "email"],
    "Hardware": ["computador", "notebook", "mouse", "teclado", "monitor", "impressora", "não liga", "nao liga"],
    "Rede": ["internet", "wifi", "wi-fi", "rede", "vpn", "lenta"],
    "Software": ["programa", "sistema", "aplicativo", "instalar", "erro", "travando", "excel", "word"],
}

PALAVRAS_CRITICAS = ["parou", "todos", "fora do ar", "urgente", "servidor", "ninguém", "ninguem"]

SLA_HORAS = {"Crítica": 2, "Alta": 4, "Média": 8, "Baixa": 24}


def classificar_categoria(texto):
    texto = texto.lower()
    for categoria, palavras in CATEGORIAS.items():
        if any(p in texto for p in palavras):
            return categoria
    return "Outros"


def definir_prioridade(texto, categoria):
    texto = texto.lower()
    if any(p in texto for p in PALAVRAS_CRITICAS):
        return "Crítica"
    if categoria in ("Rede", "Acesso"):
        return "Alta"
    if categoria == "Hardware":
        return "Média"
    return "Baixa"


def triar(descricao):
    categoria = classificar_categoria(descricao)
    prioridade = definir_prioridade(descricao, categoria)
    return {
        "categoria": categoria,
        "prioridade": prioridade,
        "sla_horas": SLA_HORAS[prioridade],
    }
