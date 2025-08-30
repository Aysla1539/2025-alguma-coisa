import re

pessoas = []
carrinho_compras = []

print("Seja bem vindo(a) a nossa IGREJA DOS ANJOS 😇⛪!")
print("Na Campanha da Fraternidade deste ano, escolhemos doar roupas!\nTemos diversas opções disponíveis. Faça seu cadastro e aproveite!")

def cadastrar_pessoa():
    
    print("\n--- Cadastro ---")
    
    nome = input("Diga-me seu nome para prosseguirmos com o seu atendimento: ").strip()
    if not nome:
        print("Você precisa adicionar um nome para continuar!")
        return

    cpf = input("Digite seu CPF (apenas números): ")
    if not (cpf.isdigit() and len(cpf) == 11):
        print("CPF inválido. Deve conter 11 dígitos numéricos.")
        return
    
    idade_str = input("Digite sua idade: ")
    try:
        idade = int(idade_str)
        if not 0 <= idade <= 125:
            print("Idade inválida! Digite um número entre 0 e 125.")
            return
    except ValueError:
        print("Idade inválida! Por favor, digite um número.")
        return

    email = input("Digite seu e-mail: ")
    if not (email and "@" in email and "." in email):
        print("Seu email deve conter '@' e '.' e não pode ser vazio.")
        return

    cep = input("Digite seu CEP (ex: 12345-678 ou 12345678): ")
    padrao_cep = re.compile(r'^\d{5}-?\d{3}$')
    if not padrao_cep.match(cep):
        print("CEP inválido. O formato deve ser XXXXX-XXX ou XXXXXXXX.")
        return
    
    sexo = input("Digite seu sexo (fem ou masc): ").lower()
    if sexo not in ["fem", "masc"]:
        print("Sexo inválido. Digite 'fem' para feminino ou 'masc' para masculino.")
        return

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "email": email,
        "cep": cep,
        "sexo": sexo,
    }
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def clothes(sexo_usuario):
    global carrinho_compras

    if sexo_usuario == "fem":
        print("Lista Roupas Femininas:\n")
        print("1- Blusa Manga Longa\n2- Blusa Manga Curta\n3- Moletom\n4- Meia\n5- Vestido\n6- Saia (curta, midi, longa)\n7- Legging\n8- Calça Skinny\n9- Calça Jeans\n10- Cropped")
    else:
        print("Lista de Roupas Masculinas:\n")
        print("1- Blusa Manga Longa\n2- Blusa Manga curta\n3- Moletom\n4- Meia\n5- Calça de moletom\n6- Jaqueta corta-vento\n7- Bermuda\n8- Bermuda Jeans\n9- Regata\n10- Blusa polo")
    
    while True:
        roupa = input("Diga o número da peça a roupa escolhida, caso queira parar de comprar digite 'sair': ").lower()
        
        if roupa == "sair":
            break
        
        feminine_options = {
            '1': ("Blusa Manga Longa", None),
            '2': ("Blusa Manga Curta", None),
            '3': ("Moletom", None),
            '4': ("Meia", "Você prefere meia"),
            '5': ("Vestido", "Você prefere vestido"),
            '6': ("Saia", "Você prefere saia"),
            '7': ("Legging", None),
            '8': ("Calça Skinny", None), 
            '9': ("Calça Jeans", None),
            '10': ("Cropped", None),
        }
        masculine_options = {
            '1': ("Blusa Manga Longa", None),
            '2': ("Blusa Manga Curta", None),
            '3': ("Moletom", None),
            '4': ("Meia", "Você prefere meia"),
            '5': ("Calça de Moletom", None),
            '6': ("Jaqueta Corta-Vento", None),
            '7': ("Bermuda", None),
            '8': ("Bermuda Jeans", None), 
            '9': ("Regata", None),
            '10': ("Blusa Polo", None),
        }

        if sexo_usuario == "fem":
            if roupa in feminine_options:
                item_name, extra_prompt = feminine_options[roupa]
                get_item_details(item_name, extra_prompt)
            else:
                print("Opção inválida. Por favor, escolha um número da lista ou 'sair'.")
        else:
            if roupa in masculine_options:
                item_name, extra_prompt = masculine_options[roupa]
                get_item_details(item_name, extra_prompt)
            else:
                print("Opção inválida. Por favor, escolha um número da lista ou 'sair'.")

def validar_cor(cor_input):
    cores_disponiveis = ['preto', 'branco', 'cinza', 'bege', 'azul']
    return cor_input.lower() in cores_disponiveis

def get_item_details(item_name, extra_prompt=None):
    global carrinho_compras
    while True:
        try:
            tamanho = input(f"Qual o tamanho de {item_name} que você usa? ")
            if not tamanho.strip():
                print("Você precisa digitar seu tamanho para prosseguir.")
                continue

            extra_detail = None
            if extra_prompt:
                extra_detail = input(f"{extra_prompt} (curto, medio, longo)? ").lower()
                if not extra_detail.strip():
                    print("Você precisa digitar o tipo para prosseguir.")
                    continue

            cor = input("Qual cor você quer? Temos preto, branco, cinza, bege e azul: ").lower()
            if not validar_cor(cor):
                print("Não temos essa cor. Por favor, escolha uma das cores disponíveis.")
                continue
            
            if extra_detail:
                pedido_confirmado = input(f"Seu pedido: {item_name}\nTamanho: {tamanho}\nTipo: {extra_detail}\nCor: {cor}\nPrecisa trocar? (sim/nao): ").lower()
            else:
                pedido_confirmado = input(f"Seu pedido: {item_name}\nTamanho: {tamanho}\nCor: {cor}\nPrecisa trocar? (sim/nao): ").lower()
            
            if pedido_confirmado == 'nao':
                item_data = {"item": item_name, "tamanho": tamanho, "cor": cor}
                if extra_detail:
                    item_data["tipo"] = extra_detail
                carrinho_compras.append(item_data)
                print(f"{item_name} adicionado ao carrinho!")
                break
            elif pedido_confirmado == 'sim':
                print("Por favor, digite as informações novamente.")
            else:
                print("Opção inválida. Digite 'sim' ou 'nao'.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor válido.")

def mangaL(item_name):
    get_item_details(item_name)

def mangaC(item_name):
    get_item_details(item_name)

def moletom(item_name):
    get_item_details(item_name)

def vestido(item_name):
    get_item_details(item_name, "Você prefere vestido")

def meia(item_name):
    get_item_details(item_name, "Você prefere meia")

def saia(item_name):
    get_item_details(item_name, "Você prefere saia")

def legging(item_name):
    get_item_details(item_name)

def calcaS(item_name):
    get_item_details(item_name)

def calcaJ(item_name):
    get_item_details(item_name)

def cropped(item_name):
    get_item_details(item_name)

def jaquetaCV(item_name):
    get_item_details(item_name)

def calcaM(item_name):
    get_item_details(item_name)

def bermudaJ(item_name):
    get_item_details(item_name)

def bermuda(item_name):
    get_item_details(item_name)

def regata(item_name):
    get_item_details(item_name)

def blusaP(item_name):
    get_item_details(item_name)

def listar_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada ainda.")
    else:
        print("\n--- Lista de Pessoas Cadastradas ---")
        for i, pessoa in enumerate(pessoas):
            print(f"{i+1}. Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}")

def editar_pessoa():
    if not pessoas:
        print("Nenhuma pessoa cadastrada para editar.")
        return

    listar_pessoas()
    try:
        indice_editar = int(input("Digite o NÚMERO da pessoa que deseja editar: ")) - 1
        if 0 <= indice_editar < len(pessoas):
            pessoa = pessoas[indice_editar]
            print(f"\n--- Editando: {pessoa['nome']} ---")

            novo_nome = input(f"Novo nome (atual: {pessoa['nome']}): ").strip()
            if novo_nome:
                pessoa['nome'] = novo_nome

            novo_cpf = input(f"Novo CPF (atual: {pessoa['cpf']}): ")
            if novo_cpf.isdigit() and len(novo_cpf) == 11:
                pessoa['cpf'] = novo_cpf
            elif novo_cpf:
                print("CPF inválido. Mantendo o CPF anterior.")

            nova_idade_str = input(f"Nova idade (atual: {pessoa['idade']}): ")
            if nova_idade_str:
                try:
                    nova_idade = int(nova_idade_str)
                    if 0 <= nova_idade <= 125:
                        pessoa['idade'] = nova_idade
                    else:
                        print("Idade inválida. Mantendo a idade anterior.")
                except ValueError:
                    print("Idade inválida. Mantendo a idade anterior.")

            novo_email = input(f"Novo e-mail (atual: {pessoa['email']}): ")
            if novo_email and "@" in novo_email and "." in novo_email:
                pessoa['email'] = novo_email
            elif novo_email:
                print("E-mail inválido. Mantendo o e-mail anterior.")

            novo_cep = input(f"Novo CEP (atual: {pessoa['cep']}): ")
            padrao_cep = re.compile(r'^\d{5}-?\d{3}$')
            if novo_cep and padrao_cep.match(novo_cep):
                pessoa['cep'] = novo_cep
            elif novo_cep:
                print("CEP inválido. Mantendo o CEP anterior.")

            novo_sexo = input(f"Novo sexo (fem/masc) (atual: {pessoa['sexo']}): ").lower()
            if novo_sexo in ["fem", "masc"]:
                pessoa['sexo'] = novo_sexo
            elif novo_sexo:
                print("Sexo inválido. Mantendo o sexo anterior.")

            print("Pessoa editada com sucesso!")
        else:
            print("Número de pessoa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
        
def excluir_pessoa():
    listar_pessoas()
    if not pessoas:
        print("Nenhuma pessoa para excluir.")
        return
    
    try:
        indice_excluir = int(input("Digite o NÚMERO da pessoa para excluir: ")) - 1
        if 0 <= indice_excluir < len(pessoas):
            nome_removido = pessoas[indice_excluir]['nome']
            del pessoas[indice_excluir]
            print(f"'{nome_removido}' foi removido do cadastro.")
        else:
            print("Número de pessoa inválido. Nenhuma pessoa excluída.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def carrinho():
    if not pessoas:
        print("Você precisa cadastrar uma pessoa antes de acessar o carrinho de compras.")
        return

    print("\n--- Seleção de Roupas para Doação ---")
    listar_pessoas()
    try:
        indice_pessoa = int(input("Digite o NÚMERO da pessoa para quem você deseja escolher roupas: ")) - 1
        if 0 <= indice_pessoa < len(pessoas):
            pessoa_selecionada = pessoas[indice_pessoa]
            print(f"Você está selecionando roupas para: {pessoa_selecionada['nome']}")
            
            clothes(pessoa_selecionada['sexo'])

            if carrinho_compras:
                print("\n--- Itens Adicionados ao Carrinho ---")
                for i, item in enumerate(carrinho_compras):
                    if "tipo" in item:
                        print(f"{i+1}. {item['item']} (Tamanho: {item['tamanho']}, Tipo: {item['tipo']}, Cor: {item['cor']})")
                    else:
                        print(f"{i+1}. {item['item']} (Tamanho: {item['tamanho']}, Cor: {item['cor']})")
            else:
                print("Seu carrinho de doações está vazio.")
        else:
            print("Número de pessoa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Editar Pessoa")
        print("4. Excluir Pessoa")
        print("5. Selecionar Roupas para Doação (Carrinho)")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            editar_pessoa()
        elif opcao == '4':
            excluir_pessoa()
        elif opcao == '5':
            carrinho()
        elif opcao == '6':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
