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

### 5. Fluxo do Programa (Como a IA funciona por baixo dos panos)

Para quem quiser entender a arquitetura do código, o fluxo de execução segue os seguintes passos lógicos:

1. **Extração e Leitura:** O script utiliza a biblioteca `pandas` para importar o histórico de funcionários direto da planilha `dados_rh_ml.xlsx`.
2. **Isolamento de Dados (Train/Test Split):** Os dados são separados em 80% para estudo (Treino) e 20% para a prova final (Teste). A variável `random_state` garante que o sorteio seja reprodutível em outras máquinas.
3. **Treinamento (Fit):** O modelo `DecisionTreeClassifier` analisa as características (features) dos dados de treino e constrói internamente a lógica matemática que leva a uma promoção.
4. **Simulação e Previsão (Predict):** A máquina recebe os dados dos 20% de teste (apenas as pistas, sem o gabarito) e tenta prever o destino de cada funcionário.
5. **Avaliação de Desempenho (Score):** O sistema cruza as previsões da IA com o gabarito real oculto. A nota final de precisão é calculada e exibida no terminal com cores dinâmicas (utilizando o módulo `config`).
6. **Abertura da "Caixa Preta" (Export Text):** Por fim, o script imprime em formato de texto toda a lógica ramificada que a árvore de decisão criou sozinha, tornando o algoritmo totalmente transparente e auditável.
