# Automação de Cadastro de Produtos

## Descrição
Este projeto automatiza o processo de cadastro de produtos em um sistema online. Utilizando a biblioteca **PyAutoGUI**, o script entra no sistema da empresa, realiza o login automaticamente, lê uma base de dados CSV com as informações dos produtos e cadastra cada produto de forma automatizada. Além disso, um código adicional é fornecido para identificar a posição atual do mouse, o que facilita a automação em diferentes telas e sistemas.

## Funcionalidades
1. **Acesso ao Sistema**: O script abre o navegador e acessa o sistema de login da empresa.
2. **Login Automático**: Preenche automaticamente os campos de login e senha.
3. **Importação de Base de Dados**: Utiliza **Pandas** para ler uma base de dados CSV (`produtos.csv`).
4. **Cadastro de Produtos**: Cadastra automaticamente cada produto da tabela CSV no sistema.
5. **Identificação da Posição do Mouse**: Um código adicional fornece as coordenadas do cursor do mouse para ajustar as automações em diferentes resoluções.

## Tecnologias Utilizadas
- **PyAutoGUI**: Para automação de cliques e escrita no navegador.
- **Pandas**: Para manipulação e leitura de arquivos CSV.
- **Google Chrome**: Navegador utilizado para acessar o sistema.

## Requisitos
- Python 3.x
- Bibliotecas:
  - `pyautogui`: Para instalar, execute `pip install pyautogui`
  - `pandas`: Para instalar, execute `pip install pandas`
  
## Como Rodar o Projeto
1. **Instalar Dependências**:
   - Execute o seguinte comando no terminal:
     ```bash
     pip install pyautogui pandas
     ```

2. **Preparar a Base de Dados**:
   - Certifique-se de ter um arquivo `produtos.csv` com as seguintes colunas:
     - `codigo`
     - `marca`
     - `tipo`
     - `categoria`
     - `preco_unitario`
     - `custo`
     - `obs` (opcional)

3. **Rodar o Script de Automação**:
   - Execute o script principal que realiza o login e cadastra os produtos:
     ```bash
     python automacao_cadastro.py
     ```

4. **Obter a Posição do Mouse (opcional)**:
   - Caso seja necessário ajustar as coordenadas do mouse para cliques ou ações específicas, utilize o script que identifica as posições:
     ```bash
     python posicao_mouse.py
     ```
   - O script exibirá no terminal a posição atual do mouse após 4 segundos.

## Explicação do Código

### Passo 1: Entrar no Sistema
- O código utiliza `pyautogui` para abrir o navegador, digitar o endereço e acessar o sistema de login.

### Passo 2: Fazer Login
- Preenche automaticamente o e-mail e senha e, em seguida, clica no botão de login.

### Passo 3: Importar Base de Dados
- A base de dados dos produtos é importada de um arquivo CSV utilizando a biblioteca `pandas`.

### Passo 4: Cadastrar Produtos
- Para cada linha do CSV, o script preenche os campos de cadastro no sistema, como código, marca, tipo, categoria, preço unitário e custo. Se houver observações, elas também são incluídas.

### Passo 5: Repetir o Processo
- O script continua repetindo o processo até que todos os produtos da tabela sejam cadastrados.

### Código de Posição do Mouse
- Um código adicional é incluído para capturar as coordenadas `x` e `y` do mouse, facilitando o ajuste das automações para diferentes resoluções de tela.

## Autor
- **Angelo Sequinel**

## Licença
Este projeto não possui licença.
