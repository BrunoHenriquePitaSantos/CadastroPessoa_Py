# 1 - Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair
# 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Sair
# 1 - Cadastar Pessoa Juridica / 2 - listar Pessoa Juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica


def main():
    lista_pf = []
    while True:
        opcao = int(input("Escolha uma opcao: 1 - Pessoa Fisica / 2- Pessoa Juridica / 0 - Sair " ))
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 Listar Pessoa Fisica / 3 - Voltar ao menu anterior "))
                #  1 - Cadastrar uma Pessoa Fisica
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros): "))

                    data_nascimento = input("Digite a data de nascimento (dd/MM/aaaa): ") # solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A Pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")  
                        continue # Retornar ao inicio do loop  

                    # Cadastro do endereco
                    novo_end_pf.logradouro = input("Digite o Logradouro: ")
                    novo_end_pf.numero = input("Digite o numero: ")
                    end_comercial = input("Este endereco e comercial: S/N ?")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S' # define se o endereco e comercial

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!!")

                # Listar pessoa fisica
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago R$: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para Sair")
                            input()
                    else:
                        print("Lista Vazia")    

                # Sair do menu atual
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")   
                    break      

                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas:")   
        elif opcao == 2:
            print("Funcionalidade para pessoa juridicia nao implementadas")
            pass

        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema! Valeu!")
            break

        else:
            print("Opcao invalida, por favor digite uma das opcoes validas! ")

if __name__ == "__main__":
    main() # Chama a funcao principal            