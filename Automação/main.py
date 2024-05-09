# Passo a passo do programa
# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2. Fazer login
# 3. Abrir/Importar a base de dados e de produtos para cadastrar
# 4. Cadastrar um produto
# 5. Repetir isso tudo até acabar a lista de produtos

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

# Abrindo o Navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Entrando no site do sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Espera a página carregar
time.sleep(3)

# Pega a posição do input, coloca as informações e loga
pyautogui.click(x=2548, y=464)
pyautogui.write('exemplo@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha1234')
pyautogui.press('tab')
pyautogui.press('enter')

# Espera a página carregar
time.sleep(3)

# Importa a base de dados
table = pd.read_csv('produtos.csv')
# print(table)

# Cadastra um produto
for linha in table.index:
    # clicar no campo de código
    pyautogui.click(x=2574, y=323)
    # pegar da tabela o valor do campo que a gente quer preencher
    code = table.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(code))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(table.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(table.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
