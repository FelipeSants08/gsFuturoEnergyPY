from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas
from database import SessionLocal
from crud import criar_tipo_fonte, listar_tipos_fontes, atualizar_tipo_fonte, deletar_tipo_fonte
from crud import criar_regiao_sustentavel, listar_regioes_sustentaveis, atualizar_regiao_sustentavel, deletar_regiao_sustentavel
from crud import criar_projeto_sustentavel, listar_projetos_sustentaveis, atualizar_projeto_sustentavel, deletar_projeto_sustentavel
from crud import criar_emissao_carbono, listar_emissoes_carbono, atualizar_emissao_carbono, deletar_emissao_carbono

# Supondo que `db` é a sua sessão de banco de dados criada no FastAPI, passe-a como parâmetro
# no seu menu ou faça com que seja gerada no início de cada operação

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def menu(db: Session):
    while True:
        print("\nEscolha uma opção:")
        print("1. Gerenciar TipoFonte")
        print("2. Gerenciar RegiaoSustentavel")
        print("3. Gerenciar ProjetoSustentavel")
        print("4. Gerenciar EmissaoCarbono")
        print("5. Sair")
        
        opcao = input("Opção: ")

        if opcao == '1':
            gerenciar_tipo_fonte(db)

        elif opcao == '2':
            gerenciar_regiao_sustentavel(db)

        elif opcao == '3':
            gerenciar_projeto_sustentavel(db)

        elif opcao == '4':
            gerenciar_emissao_carbono(db)

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


# Funções para gerenciar TipoFonte
def gerenciar_tipo_fonte(db: Session):
    while True:
        print("\nGerenciar TipoFonte:")
        print("1. Criar TipoFonte")
        print("2. Listar TipoFontes")
        print("3. Atualizar TipoFonte")
        print("4. Deletar TipoFonte")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Digite o nome do TipoFonte: ")
            tipo_fonte = schemas.tipoFonteCriar(nome=nome)
            try:
                tipo_fonte_criado = criar_tipo_fonte(db, tipo_fonte)
                print(f"TipoFonte '{tipo_fonte_criado.nome}' criado com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '2':
            tipo_fontes = listar_tipos_fontes(db)
            for tipo_fonte in tipo_fontes:
                print(f"ID: {tipo_fonte.id}, Nome: {tipo_fonte.nome}")

        elif opcao == '3':
            tipo_fonte_id = int(input("Digite o ID do TipoFonte a ser atualizado: "))
            nome = input("Digite o novo nome: ")
            tipo_fonte_atualizar = schemas.tipoFonteAtualizar(nome=nome)
            try:
                tipo_fonte_atualizado = atualizar_tipo_fonte(db, tipo_fonte_id, tipo_fonte_atualizar)
                print(f"TipoFonte '{tipo_fonte_atualizado.nome}' atualizado com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '4':
            tipo_fonte_id = int(input("Digite o ID do TipoFonte a ser deletado: "))
            try:
                mensagem = deletar_tipo_fonte(db, tipo_fonte_id)
                print(mensagem["mensagem"])
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '5':
            break

        else:
            print("Opção inválida, tente novamente.")


# Funções para gerenciar RegiaoSustentavel
def gerenciar_regiao_sustentavel(db: Session):
    while True:
        print("\nGerenciar Região Sustentável:")
        print("1. Criar Região Sustentável")
        print("2. Listar Regiões Sustentáveis")
        print("3. Atualizar Região Sustentável")
        print("4. Deletar Região Sustentável")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Digite o nome da Região Sustentável: ")
            regiao = schemas.regioesSustentaveisCriar(nome=nome)
            try:
                regiao_criada = criar_regiao_sustentavel(db, regiao)
                print(f"Região Sustentável '{regiao_criada.nome}' criada com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '2':
            regioes = listar_regioes_sustentaveis(db)
            for regiao in regioes:
                print(f"ID: {regiao.id}, Nome: {regiao.nome}")

        elif opcao == '3':
            regiao_id = int(input("Digite o ID da Região Sustentável a ser atualizada: "))
            nome = input("Digite o novo nome: ")
            regiao_atualizar = schemas.regioesSustentaveisAtualizar(nome=nome)
            try:
                regiao_atualizada = atualizar_regiao_sustentavel(db, regiao_id, regiao_atualizar)
                print(f"Região Sustentável '{regiao_atualizada.nome}' atualizada com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '4':
            regiao_id = int(input("Digite o ID da Região Sustentável a ser deletada: "))
            try:
                mensagem = deletar_regiao_sustentavel(db, regiao_id)
                print(mensagem["mensagem"])
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '5':
            break

        else:
            print("Opção inválida, tente novamente.")


# Funções para gerenciar ProjetoSustentavel
def gerenciar_projeto_sustentavel(db: Session):
    while True:
        print("\nGerenciar Projeto Sustentável:")
        print("1. Criar Projeto Sustentável")
        print("2. Listar Projetos Sustentáveis")
        print("3. Atualizar Projeto Sustentável")
        print("4. Deletar Projeto Sustentável")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Opção: ")

        if opcao == '1':
            descricao = input("Digite a descrição do Projeto Sustentável: ")
            custo = float(input("Digite o custo do projeto: "))
            status = input("Digite o status do projeto: ")
            tipo_fonte_id = int(input("Digite o id do tipo fonte de energia: "))
            regioes_sustentaveis_id = int(input("Digite o id da região sustentável: "))
            projeto = schemas.projetosSustentaveisCriar(descricao=descricao, custo=custo, status=status, tipo_fonte_id=tipo_fonte_id, regioes_sustentaveis_id=regioes_sustentaveis_id)
            try:
                projeto_criado = criar_projeto_sustentavel(db, projeto)
                print(f"Projeto Sustentável '{projeto_criado.nome}' criado com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '2':
            projetos = listar_projetos_sustentaveis(db)
            for projeto in projetos:
                print(f"ID: {projeto.id}, Descrição: {projeto.descricao}, Custo: {projeto.custo}, Status: {projeto.status}, Tipo_fonte_id: {projeto.tipo_fonte_id}, Regioes_sustentaveis_id: {projeto.regioes_sustentaveis_id}")

        elif opcao == '3':
            projeto_id = int(input("Digite o ID do Projeto Sustentável a ser atualizado: "))
            descricao = input("Digite a nova descrição: ")
            custo = float(input("Digite o custo do projeto: "))
            status = input("Digite o status do projeto: ")
            tipo_fonte_id = int(input("Digite o id do tipo fonte de energia: "))
            regioes_sustentaveis_id = int(input("Digite o id da região sustentável: "))
            projeto_atualizar = schemas.projetosSustentaveisAtualizar(descricao=descricao, custo=custo, status=status, tipo_fonte_id=tipo_fonte_id, regioes_sustentaveis_id=regioes_sustentaveis_id)
            try:
                projeto_atualizado = atualizar_projeto_sustentavel(db, projeto_id, projeto_atualizar)
                print(f"Projeto Sustentável '{projeto_atualizado.nome}' atualizado com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '4':
            projeto_id = int(input("Digite o ID do Projeto Sustentável a ser deletado: "))
            try:
                mensagem = deletar_projeto_sustentavel(db, projeto_id)
                print(mensagem["mensagem"])
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '5':
            break

        else:
            print("Opção inválida, tente novamente.")


# Funções para gerenciar EmissaoCarbono
def gerenciar_emissao_carbono(db: Session):
    while True:
        print("\nGerenciar Emissão de Carbono:")
        print("1. Criar Emissão de Carbono")
        print("2. Listar Emissões de Carbono")
        print("3. Atualizar Emissão de Carbono")
        print("4. Deletar Emissão de Carbono")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Opção: ")

        if opcao == '1':
            tipo_fonte_id = int(input("Digite o TipoFonte ID: "))
            emissao_num = float(input("Digite a taxa de emissão: "))
            emissao = schemas.emissoesCarbonoCriar(tipo_fonte_id=tipo_fonte_id, emissao=emissao_num)
            try:
                emissao_criada = criar_emissao_carbono(db, emissao)
                print(f"Emissão de Carbono criada com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '2':
            emissoes = listar_emissoes_carbono(db)
            for emissao in emissoes:
                print(f"ID: {emissao.id}, TipoFonte ID: {emissao.tipo_fonte_id}, Emissao: {emissao.emissao}")

        elif opcao == '3':
            emissao_id = int(input("Digite o ID da Emissão de Carbono a ser atualizada: "))
            tipo_fonte_id = int(input("Digite o novo TipoFonte ID: "))
            emissao_num = float(input("Digite a nova taxa de emissão: "))
            emissao_atualizar = schemas.emissoesCarbonoAtualizar(tipo_fonte_id=tipo_fonte_id, emissao_num=emissao_num)
            try:
                emissao_atualizada = atualizar_emissao_carbono(db, emissao_id, emissao_atualizar)
                print(f"Emissão de Carbono atualizada com sucesso!")
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '4':
            emissao_id = int(input("Digite o ID da Emissão de Carbono a ser deletada: "))
            try:
                mensagem = deletar_emissao_carbono(db, emissao_id)
                print(mensagem["mensagem"])
            except HTTPException as e:
                print(f"Erro: {e.detail}")

        elif opcao == '5':
            break

        else:
            print("Opção inválida, tente novamente.")


def run():
    db = next(get_db())  # Obtemos a sessão do banco de dados
    menu(db)  # Passamos a sessão para o menu

# Rodando o menu
run()