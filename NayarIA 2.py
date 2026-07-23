# ///////////////////////////////////////////////
# TESTE DE ML - NAYARIA
# ÁRVORE DE DECISÃO -- APRENDIZADO SUPERVISIONADO
# AGORA IMPORTANDO UMA PLANILHA DO EXCEL COM OS DADOS DE TREINO E TESTE
# ///////////////////////////////////////////////

import pandas as pd
from sklearn import tree
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
import config

planilha = pd.read_excel('dados_rh_ml.xlsx')  # Lendo a planilha do Excel

# Separando os dados em treino e teste (sempre lembrar a ordem: x_train, x_test, y_train, y_test), sendo x = dados e y = gabarito | test_size (Quantos % serão destinados para o teste) | random_state (roda uma semente fixa de aleatoriedade toda vez q rodar o código (importantíssimo))
dados_treino, dados_teste, gabarito_treino, gabarito_teste = train_test_split(planilha[['projetos_entregues', 'anos_empresa', 'atrasos_no_mes']], planilha['promovido'], test_size=0.2, random_state=42)

cerebroIA = tree.DecisionTreeClassifier()  # --> da pra colocar max_depth=2 como parametro dentro do DecisionTreeClassifier() para limitar a profundidade da árvore (evita overfitting)
cerebroIA = cerebroIA.fit(dados_treino, gabarito_treino)  # Treinando o modelo com os dados de treino

previsao = cerebroIA.predict(dados_teste) # botando os dados de teste pra ver se a IA acerta o gabarito teste

print("\n--- PREVISÃO DA NAYARIA ---\n")
for i in range(len(dados_teste)):
    if previsao[i] == 1:
        print(f"{config.Cores.AZUL}[NayarIA]: acredito que o funcionário {i+1} será promovido!{config.Cores.FIM}")
    else:
        print(f"{config.Cores.AZUL}[NayarIA]: acredito que o funcionário {i+1} NÃO será promovido.{config.Cores.FIM}")

nota = cerebroIA.score(dados_teste, gabarito_teste)
if nota*100 >= 70:
    cor = config.Cores.VERDE
elif nota*100 >= 50:
    cor = config.Cores.AMARELO
else:
    cor = config.Cores.VERMELHO
print(f"\n{cor}A NayarIA acertou {nota * 100}% da prova!{config.Cores.FIM}")

regras = export_text(cerebroIA, feature_names=['projetos_entregues', 'anos_empresa', 'atrasos_no_mes'], class_names=['Não promovido', 'Promovido'])

print("\n--- O CÉREBRO DA NAYARIA ---\n")
print(regras)
print("-----------------------")

print(f"\n{config.Cores.VERMELHO}Lembre-se: a IA acerta ou erra as previsões dependendo de diversos fatores.\nFique de olho em: overfitting, underfitting, pouco volume de dados, random_state com semente 'azarada'.{config.Cores.FIM}")
print(f"{config.Cores.NEGRITO}Tente mudar o random_state para ver qual nota a NayarIA é capaz de obter com dados de treino/teste diferentes!{config.Cores.FIM}\n")