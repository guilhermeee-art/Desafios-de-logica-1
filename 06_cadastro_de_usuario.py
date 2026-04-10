'''Crie um sistema de cadastro de usuário que registre as informações de “nome, sexo, endereço, cidade, estado, CEP, telefone, data de nascimento, RG, nome do pai, nome da mãe e grau de escolaridade” do usuário.
O sistema deve exibir as informações do usuário em um texto amigável.'''



info_necss = ["nome"]
info = []



for i in info_necss:
    dado = input('digite o seu',i)
    info.append(dado)
    

print("Para fazermos o seu cadastro, digite as seguintes informações:")

# var_nome = input("digite o seu nome: ")
# var_sexo = input("digite seu sexo: ")
# var_endereço = input("digite o seu endereço: ")
# var_cidade = input("digite sua cidade: ")
# var_estado = input("digite o seu estado: ")
# var_cep = input("digite seu cep: ")
# var_telefone = input("digite seu telefone: ")
# var_nascimento = input("digite sua data de nascimento: ")
# var_rg = input("digite seu RG: ")
# var_nomepai = input("digite o nome do seu pai: ")
# var_nomemae = input("digite o nome da sua mãe: ")
# var_grauescolar = input("digite seu grau de escolaridade: ")

# print(f'usuario:{var_nome},do sexo:{var_sexo},morador do endereço:{var_endereço},no estado:{var_estado}')
      
""" {var_cep}, tel{var_telefone}\n nascimento:{var_nascimento}, Rg{var_rg}\n Filiado:{var_nomepai} e {var_nomemae}\n Grau escolar:{var_grauescolar})"""
      
