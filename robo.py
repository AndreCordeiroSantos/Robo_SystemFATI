import time
import mysql.connector
import subprocess
import shutil

# Dados de conexão
usuario = '#'
senha = '#'
database = '#'
host = '#'

# Loop principal
while True:
    try:
        # Conectando ao banco de dados
        conexao = mysql.connector.connect(
            user=usuario,
            password=senha,
            host=host,
            database=database
        )

        # Obtendo o cursor
        cursor = conexao.cursor()

        # Executa o comando SELECT
        cursor.execute("SELECT id, et_fati, status_fati FROM fati WHERE status_fati = 'aberto'")
        resultados = cursor.fetchall()

        # Processa os resultados
        if len(resultados) > 0:
            for resultado in resultados:
                id, et, status = resultado

                fonte1 = 'C:\sistema fati\instalador\{Nome Programa.exe}'

                destino1 = fr'\\{et}\c$\TEMP\{Nome Programa.exe}'
                nome_programa = 'Nome Programa.exe'
                print(f'Copiando o instalador para o computador {et}')
                shutil.copy2(fonte1, destino1)
                print('Cópia EFETUADA COM SUCESSO')

                print('Finalizando o programa para Atualização.')
                processo_finalizar = subprocess.run(['taskkill', '/F', '/IM', nome_programa, '/S', et], capture_output=True, text=True)

                if processo_finalizar.returncode == 0:
                    print('Erro ao finalizar o processo do programa:')
                    print(processo_finalizar.stderr)
                else:
                    print(f'Processo {nome_programa} finalizando com sucesso no computador {et}')

                print(f"Instalando o aplicativo no computador {et}")

                comando = fr'''
                Invoke-Command -ComputerName "{et}" {{
                    Unblock-File -Path "c:\TEMP\Nome Programa.exe"
                    Start-Process -FilePath "c:\TEMP\Nome Programa.exe" -ArgumentList "/VERYSILENT", "/SP-" -Wait
                }}
                '''

                processo = subprocess.run(["powershell", "-Command", comando], capture_output=True, text=True)

                if processo.returncode != 0:
                    # Ocorreu um erro durante a execução do comando
                    print("Erro ao executar o comando:")
                    print(processo.stderr)
                else:
                    # Comando executado com sucesso
                    print("Instalação concluída com sucesso.")

                # Atualiza o status_fati para "finalizado"
                cursor.execute("UPDATE fati SET status_fati = 'finalizado' WHERE id = %s", (id,))
                conexao.commit()
                print(f"Status do id {id} atualizado para 'finalizado'.")
        else:
            print("Aguardando informações para executar.")
    # Caso ocorre erro de conexão, apresenta uma mensagem.
    except Exception as e:
        print("Ocorreu uma exceção durante a execução:", str(e))

    finally:
        # Fechando a conexão
        if 'conexao' in locals() or 'conexao' in globals():
            conexao.close()

    # Aguarda 20 segundos antes de executar o próximo loop
    time.sleep(20)

