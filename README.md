# NayarIA---RH

##Este projeto é uma IA que prevê promoções de funcionários com base em dados pré-existentes.

### 1. Conceitos utilizados:
- Aprendizado Supervisionado (Árvores de Decisão com Scikit-Learn).
- Separação de Dados com train_test_split para evitar vazamento de respostas (Treino vs. Teste).
- Controle de Aleatoriedade (random_state) para testes consistentes.
- Prevenção de Overfitting limitando a complexidade da árvore.

### 2. Feats (Funcionalidades):
- **Interface de Linha de Comando (CLI) Interativa:** Saídas no terminal formatadas e coloridas para melhorar a experiência do usuário.
- **Importação de Dados Externos:** Leitura e processamento de base de dados realística de RH através de planilhas Excel (`.xlsx`).
- **Feedback Dinâmico de Performance:** O sistema avalia a precisão do modelo a cada execução e exibe a nota com cores indicativas (Verde para alta precisão, Amarelo para média, Vermelho para baixa).
- **Transparência do Modelo (Explainable AI):** Impressão visual das regras lógicas que a IA criou sozinha ("O Cérebro da NayarIA"), permitindo entender exatamente o porquê de cada decisão.
- **Dicas Educativas:** Alertas automáticos no console sobre boas práticas de dados e riscos de modelagem.

### 3. Como rodar o projeto na sua máquina:

**Pré-requisitos:**
Certifique-se de ter o Python instalado. Você precisará instalar as bibliotecas de manipulação de dados, machine learning e leitura de Excel:
```bash
pip install pandas scikit-learn openpyxl
