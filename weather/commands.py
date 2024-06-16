import subprocess
from dotenv import dotenv_values

envVariables = dotenv_values()

def svn_add_commit(repository_url, file_path, commit_message):
    # Comando para adicionar o arquivo ao repositório SVN
    add_command = [
        'svn', 'add', file_path, repository_url,
        '--username', envVariables['SVN_USERNAME'],
        '--password', envVariables['SVN_PASSWORD'],
        '--no-auth-cache',
        '--non-interactive'
    ]

    # Comando para fazer o commit do arquivo com a mensagem especificada
    commit_command = [
        'svn', 'commit', '-m', commit_message, repository_url,
        '--username', envVariables['SVN_USERNAME'],
        '--password', envVariables['SVN_PASSWORD'],
        '--no-auth-cache',
        '--non-interactive'
    ]

    try:
        # Execute o comando para adicionar o arquivo
        subprocess.run(add_command, check=True)
        print("Arquivo adicionado ao repositório SVN.")

        # Execute o comando para fazer o commit do arquivo
        subprocess.run(commit_command, check=True)
        print("Arquivo commitado com sucesso.")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar comando SVN:", e)
        exit(1)

url = "https://linkoftheurl.ddns.me:12345000000/svn/aaaaa"
file_path = 'weather_data.json'
repository_url = url
commit_message = 'Atualizando dados meteorológicos coletados via API Weatherstack'

# Chamada da função para adicionar e commitar o arquivo
svn_add_commit(repository_url, file_path, commit_message)

