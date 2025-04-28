# Versão 2 (Atualizada): Classificação de Sentenças com Bag-of-Words e KNN (scikit-learn)

import re
import numpy as np
import unicodedata
from sklearn.neighbors import KNeighborsClassifier

# --- Funções auxiliares ---

def remover_acentos(texto):
    """Remove acentos de um texto."""
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def tokenizar(frase):
    """Transforma uma frase em tokens (palavras), removendo acentos e convertendo para minúsculas."""
    frase = remover_acentos(frase.lower())
    return re.findall(r'\b\w+\b', frase)

def build_model_lexicon(words, model_lexicon):
    """Adiciona palavras únicas ao lexicon base e ordena."""
    for word in words:
        if word not in model_lexicon:
            model_lexicon.append(word)
    model_lexicon.sort()

def build_feature_vector(words, model_lexicon):
    """Cria vetor de características (bag-of-words) baseado no lexicon."""
    bag_of_words_count = np.zeros(len(model_lexicon))
    for pos in range(len(model_lexicon)):
        for word in words:
            if word == model_lexicon[pos]:
                bag_of_words_count[pos] += 1
    return bag_of_words_count

# --- Corpus de avaliações classificados manualmente (para treino) ---
classified_reviews = [
    {'corpus': "produto excelente e confortavel", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "adorei a blusa linda", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "atendimento otimo e produto perfeito", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "produto ruim e defeituoso", 'review_type': 'negative', 'feature_vector': []},
    {'corpus': "pessima qualidade do tecido", 'review_type': 'negative', 'feature_vector': []},
    {'corpus': "produto diferente do pedido", 'review_type': 'negative', 'feature_vector': []},
    {'corpus': "produto entregue corretamente", 'review_type': 'neutral', 'feature_vector': []},
    {'corpus': "entrega dentro do prazo", 'review_type': 'neutral', 'feature_vector': []},
    {'corpus': "recebi o pedido conforme solicitado", 'review_type': 'neutral', 'feature_vector': []}
]

# --- Corpus de avaliações a serem classificadas ---
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
    "Gola veio descosturada."
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
    "Pequenas falhas no acabamento interno."
]

# --- Construção do lexicon base ---
base_model_lexicon = []
# Adiciona palavras dos reviews classificados ao lexicon
for classified_review in classified_reviews:
    build_model_lexicon(tokenizar(classified_review['corpus']), base_model_lexicon)
# Adiciona palavras dos reviews não classificados ao lexicon
for frase in avaliacoes_vestuario + avaliacoes_carros:
    build_model_lexicon(tokenizar(frase), base_model_lexicon)

# --- Construção dos vetores de características para o corpus de treino ---
for classified_review in classified_reviews:
    classified_review['feature_vector'] = build_feature_vector(tokenizar(classified_review['corpus']), base_model_lexicon)

# Prepara conjuntos de treino
X_train = []  # feature vectors
y_train = []  # classes
for review in classified_reviews:
    X_train.append(review['feature_vector'])
    y_train.append(review['review_type'])

# --- Treinando o modelo KNN ---
knn = KNeighborsClassifier(n_neighbors=3, weights='distance')  # Modelo KNN ponderado pela distância
knn.fit(X_train, y_train)

# --- Função de classificação ---
def classificar_review_knn(frase, base_model_lexicon, knn_model):
    """Classifica uma frase usando o modelo treinado."""
    feature_vector = build_feature_vector(tokenizar(frase), base_model_lexicon)
    return knn_model.predict([feature_vector])[0]

# --- Classificação para loja de vestuário ---
print("\n--- Classificação: Loja de Vestuário (KNN) ---")
for frase in avaliacoes_vestuario:
    tokens = tokenizar(frase)
    classe = classificar_review_knn(frase, base_model_lexicon, knn)
    print(f"Frase: {frase}\nTokens: {tokens}\n -> Classificação: {classe}\n")

# --- Classificação para concessionária automotiva ---
print("\n--- Classificação: Concessionária Automotiva (KNN) ---")
for frase in avaliacoes_carros:
    tokens = tokenizar(frase)
    classe = classificar_review_knn(frase, base_model_lexicon, knn)
    print(f"Frase: {frase}\nTokens: {tokens}\n -> Classificação: {classe}\n")
