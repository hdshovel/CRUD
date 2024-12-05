"""
Estrutura Geral da Aplicação

    teste.py: Contém a interface do usuário (UI) e a lógica de interação com o Streamlit.
    Ele permite que o usuário escolha entre diferentes operações (Inserir, Ler, Apagar, Update) e
    interaja com os dados.
    crud_funcoes.py: Contém as funções que realizam as operações de CRUD no banco de dados
    MySQL. Ele gerencia a conexão com o banco de dados e executa comandos SQL.
"""

# Importando funcoes em crud_funcoes para manipulação do banco de dados,
# Streamlit permite criar interfaces de usuário interativas.
import crud_funcoes
import streamlit as st

# Define o título da aplicação
st.title('EDIÇÃO DE DADOS')

# Cria um menu suspenso onde o usuário pode escolher uma das opções
opcao = st.selectbox('Escolha uma opção', ['Inserir', 'Ler', 'Apagar', 'Update'])

# Executar ações baseadas na opção escolhida
if opcao == 'Inserir':
    produto = st.text_input('Produto')
    valor = st.number_input('Valor', min_value=0.0, format="%.2f")
    if st.button('Adicionar'):
        if produto and valor > 0:
            crud_funcoes.InserirDados(produto, valor)
            st.success(f'Produto "{produto}" adicionado com sucesso!')
        else:
            st.error('Por favor, preencha todos os campos corretamente.')

elif opcao == 'Ler':
    df = crud_funcoes.LerDados()  # Chama a função que retorna um DataFrame
    if not df.empty:
        st.table(df)  # Exibe o DataFrame como uma tabela no Streamlit
    else:
        st.warning('Nenhum dado encontrado.')

elif opcao == 'Apagar':
    id = st.number_input('ID do Produto a ser apagado', min_value=1)
    if st.button('Apagar'):
        crud_funcoes.ApagarDados(id)
        st.success(f'Produto com ID {id} apagado com sucesso!')

elif opcao == 'Update':
    id = st.number_input('ID do Produto a ser atualizado', min_value=1)
    produto = st.text_input('Novo Produto')
    valor = st.number_input('Novo Valor', min_value=0.0, format="%.2f")
    if st.button('Atualizar'):
        crud_funcoes.UpdateDados(id, produto, valor)
        st.success(f'Produto com ID {id} atualizado com sucesso!')
