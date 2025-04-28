import re
import unicodedata

# --- Corpus de avaliações ---
avaliacoes_vestuario = [
    "A blusa é linda e confortável.",
    "Tecido de péssima qualidade.",
    "O casaco chegou conforme o esperado.",
    "Costura ruim, desfez com pouco uso.",
    "Muito macio e gostoso de usar!",
    "O zíper quebrou na primeira semana.",
    "Camisa excelente, super recomendo!",
    "Produto adequado ao descrito.",
    "Calça muito apertada, não gostei.",
    "Sapato extremamente confortável.",
    "Cor diferente da mostrada na foto.",
    "Malha de ótima qualidade.",
    "Entrega foi feita corretamente.",
    "O botão soltou no primeiro uso.",
    "Tecido é muito bonito.",
    "Não gostei da estampa.",
    "Vestido perfeito, ficou lindo!",
    "Produto entregue como pedido.",
    "Qualidade aceitável pelo preço.",
    "Gola veio descosturada.",
]

avaliacoes_carros = [
    "Carro entregue na data combinada.",
    "Motor apresentou defeito em uma semana.",
    "Veículo excelente, recomendo!",
    "Arranhões na pintura ao retirar o carro.",
    "Atendimento ótimo e muito rápido.",
    "Consumo mais alto que o esperado.",
    "Concessionária atendeu todas as exigências.",
    "Problemas no freio com poucos dias de uso.",
    "Carro muito potente e confortável.",
    "Manual do carro estava ausente.",
    "Veículo entregue em perfeito estado.",
    "Barulho estranho vindo do motor.",
    "Documentação foi entregue corretamente.",
    "Pneus vieram carecas.",
    "Experiência de compra excelente.",
    "Papelada demorou mais que o prometido.",
    "O carro é bom, mas esperava mais.",
    "Banco do motorista desconfortável.",
    "Atendimento cordial e prestativo.",
    "Pequenas falhas no acabamento interno.",
]

# --- Listas de palavras por setor (manualmente expandidas) ---
positivas_vestuario = [
    "linda",
    "confortável",
    "macio",
    "excelente",
    "ótima",
    "perfeito",
    "gostoso",
    "bonito",
    "recomendo",
]
negativas_vestuario = [
    "péssima",
    "ruim",
    "defeito",
    "apertada",
    "diferente",
    "descosturada",
    "quebrou",
    "soltou",
    "não gostei",
]
neutras_vestuario = [
    "conforme",
    "esperado",
    "adequado",
    "correto",
    "entregue",
    "aceitável",
    "pedido",
]

positivas_carros = [
    "excelente",
    "recomendo",
    "ótimo",
    "potente",
    "confortável",
    "cordial",
    "rápido",
    "perfeito",
    "bom",
    "prestativo",
]
negativas_carros = [
    "defeito",
    "arranhões",
    "consumo alto",
    "problemas",
    "barulho",
    "carecas",
    "falhas",
    "desconfortável",
    "demorou",
    "estranho",
]
neutras_carros = [
    "entregue",
    "data",
    "documentação",
    "atendeu",
    "experiência",
    "papelada",
    "ausente",
    "correto",
]


# --- Funções auxiliares ---
def remover_acentos(texto):
    return "".join(
        c
        for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )


def tokenizar(frase):
    frase = remover_acentos(frase.lower())
    tokens = re.findall(r"\b\w+\b", frase)
    return tokens


def analisar_frase(frase, positivas, negativas, neutras):
    tokens = tokenizar(frase)
    texto = " ".join(tokens)

    # Checar combinações
    if "consumo alto" in texto:
        return "Negativa", ["consumo alto"]

    pos = [t for t in tokens if t in positivas]
    neg = [t for t in tokens if t in negativas]
    neu = [t for t in tokens if t in neutras]

    # Regra de inversão simples
    if "nao" in tokens:
        if pos:
            return "Negativa", pos
        if neg:
            return "Positiva", neg

    if len(pos) > len(neg) and len(pos) > len(neu):
        return "Positiva", pos
    elif len(neg) > len(pos) and len(neg) > len(neu):
        return "Negativa", neg
    else:
        return "Neutra", neu


# --- Classificação para loja de vestuário ---
print("\n--- Classificação: Loja de Vestuário (feito à mão) ---")
for frase in avaliacoes_vestuario:
    classe, palavras = analisar_frase(
        frase, positivas_vestuario, negativas_vestuario, neutras_vestuario
    )
    print(f"Frase: {frase}\n -> Classificação: {classe} (tokens: {palavras})\n")

# --- Classificação para concessionária automotiva ---
print("\n--- Classificação: Concessionária Automotiva (feito à mão) ---")
for frase in avaliacoes_carros:
    classe, palavras = analisar_frase(
        frase, positivas_carros, negativas_carros, neutras_carros
    )
    print(f"Frase: {frase}\n -> Classificação: {classe} (tokens: {palavras})\n")
