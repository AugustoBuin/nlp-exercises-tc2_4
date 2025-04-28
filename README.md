# Comparativo: Classificação de Avaliações - Códigos e Exercício TC.2.4

---

## 🔹 Objetivo

Este projeto compara duas abordagens para a classificação de avaliações de produtos de vestuário e automóveis, baseado no exercício **TC.2.4** do material de Processamento de Linguagem Natural (PLN).

Também apresenta a resolução solicitada no enunciado do exercício.

---

## 🔹 Descrição dos Códigos

### 1. **Versão Manual (Tradicional/Artesanal)**
- ✅ Usa apenas `re` e `unicodedata`.
- ✅ Tokeniza frases manualmente (regex).
- ✅ Compara tokens às listas manuais de palavras positivas, negativas e neutras.
- ✅ Regras básicas para inverter sentidos quando "não" aparece.
- ✅ Classifica baseado no número de palavras encontradas.

**Pontos fortes:**
- Controle total sobre os tokens e listas.
- Fácil de entender e modificar.

**Pontos fracos:**
- Baixa escalabilidade para muitos dados.
- Dependência de listas manuais.

### 2. **Versão Automatizada com scikit-learn (KNN)**
- ✅ Usa `numpy` e `scikit-learn`.
- ✅ Tokeniza frases manualmente (regex).
- ✅ Gera vetores de características (bag-of-words).
- ✅ Treina um classificador KNN ponderado por distância.
- ✅ Prediz a classe baseada na similaridade do vetor da frase com os vetores de treino.

**Pontos fortes:**
- Robusto para grandes bases de dados.
- Capacidade de generalização melhorada.

**Pontos fracos:**
- Requer corpus de treino adequado.
- Menos controle direto sobre palavras individuais.

---

## 🔹 Resolução do Exercício TC.2.4

### Exemplos de Tokens de Frases e Palavras

**a) Opinião negativa referente a vestuário:**
- **Frases:**
  - "A qualidade do tecido é horrível."
  - "A costura desfez na primeira lavagem."
- **Palavras:**
  - ["horrível", "desfez", "ruim", "defeito", "péssimo"]

**b) Opinião positiva referente a vestuário:**
- **Frases:**
  - "A blusa é linda e muito confortável."
  - "O tecido é macio e de ótima qualidade."
- **Palavras:**
  - ["linda", "confortável", "macio", "ótima", "perfeita"]

**c) Opinião neutra referente a vestuário:**
- **Frases:**
  - "Recebi o produto conforme o pedido."
  - "O tamanho está correto."
- **Palavras:**
  - ["aceitável", "conforme", "esperado", "correto", "adequado"]

**d) Opinião negativa referente a carro:**
- **Frases:**
  - "O carro apresentou problemas no motor logo após a compra."
  - "A pintura veio com arranhões."
- **Palavras:**
  - ["problemas", "falhas", "arranhões", "defeito", "quebrado"]

**e) Opinião positiva referente a carro:**
- **Frases:**
  - "Estou satisfeito com o desempenho do veículo."
  - "Ótimo atendimento e o carro é excelente."
- **Palavras:**
  - ["satisfeito", "confortável", "ótimo", "excelente", "recomendado"]

**f) Opinião neutra referente a carro:**
- **Frases:**
  - "O carro foi entregue na data combinada."
  - "Recebi todos os documentos do veículo adequadamente."
- **Palavras:**
  - ["entregue", "combinado", "adequado", "correto", "recebido"]

---

# 🔹 Conclusão

- A abordagem **manual** é ótima para pequenos corpus e estudos didáticos.
- A abordagem **KNN com sklearn** é adequada para quando o corpus é maior ou o problema precisa ser mais automatizado.

Ambas ajudam a consolidar conceitos fundamentais de PLN como tokenização, representação vetorial e classificação supervisionada.

