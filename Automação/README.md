##  Automação de Cadastro de Produtos com Python

Este projeto demonstra como automatizar o cadastro de produtos em um sistema web usando Python e a biblioteca PyAutoGUI. Ele simula as ações de um usuário, como abrir o navegador, fazer login, preencher formulários e enviar dados, para agilizar o processo e evitar erros manuais.

### Funcionalidades:

- Abre o navegador Google Chrome.
- Acessa um site específico (neste exemplo, um sistema de cadastro de produtos).
- Realiza login com as credenciais fornecidas.
- Importa uma base de dados de produtos em formato CSV.
- Cadastra cada produto no sistema, preenchendo os campos correspondentes.
- Utiliza a tecla Tab para navegar entre os campos e Enter para enviar os dados.
- Repete o processo para todos os produtos da base de dados.

#

### Dependências:

- Python 3.x
- PyAutoGUI
- Pandas

### Observações:

- O script `main.py` está configurado para o meu sistema. Adapte o código e as coordenadas do mouse para o seu sistema específico.
- A velocidade da automação é controlada pela variável `pyautogui.PAUSE`. Ajuste o valor para um tempo de espera adequado entre as ações.
- Certifique-se de que o sistema web esteja aberto e visível antes de executar o script.
- A biblioteca PyAutoGUI controla o mouse e o teclado de forma global. Evite usar o computador durante a execução do script para evitar interferências.

### Conclusão

Este projeto demonstra o potencial da automação com Python para tarefas repetitivas. Ao automatizar o cadastro de produtos, você pode economizar tempo, reduzir erros e aumentar a produtividade. Experimente adaptar este código para suas próprias necessidades e explore as possibilidades da automação com Python.
