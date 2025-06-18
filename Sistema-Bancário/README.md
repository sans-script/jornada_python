## Simulador de Banco em Python

Este código em Python simula operações básicas de um caixa eletrônico, como saque, depósito e visualização de extrato. 

**Funcionalidades:**

* **Depósito:** Permite ao usuário depositar qualquer valor positivo em sua conta.
* **Saque:**
    * Limite de 3 saques por dia.
    * Limite de R$ 500,00 por saque.
    * Verifica saldo antes de realizar o saque.
* **Extrato:** Exibe o saldo atual da conta.

**Como usar:**

1. **Senha:** O código solicita inicialmente uma senha (fixada em 12345678) para acesso à conta.
2. **Menu:** Após a autenticação, um menu interativo é exibido com as opções de saque, depósito e extrato.
3. **Operações:** O usuário escolhe a operação desejada digitando o número correspondente. 
4. **Validações:** O programa realiza validações em cada operação, como limite de saque, saldo disponível e valores de depósito válidos.
5. **Mensagens:** Mensagens informativas são exibidas ao usuário durante a interação, como confirmação de operações, erros e avisos.

**Observações:**

* O código utiliza uma senha fixa. Em um sistema real, essa senha deveria ser armazenada de forma segura e verificada com métodos mais robustos.
* O código não persiste os dados da conta. Ou seja, o saldo é reiniciado a cada execução do programa. 

**Possíveis melhorias:**

* Implementar persistência de dados para armazenar o saldo da conta.
* Implementar um sistema de autenticação mais seguro.
* Adicionar funcionalidades como transferência entre contas, pagamento de contas, etc.

**Exemplo de uso:**

```
Insira sua senha: 12345678
=========== Bem-vindo! ===========

O que você quer fazer hoje?

Digite:
[1] - Saque
[2] - Depósito
[3] - Extrato

2
Insira o valor do depósito (apenas números positivos): 1000
Depósito de R$ 1000.00 realizado com sucesso!

O que você quer fazer hoje?

Digite:
[1] - Saque
[2] - Depósito
[3] - Extrato

3
Seu saldo é de R$ 1000.00
```