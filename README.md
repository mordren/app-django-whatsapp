# app-django-whatsapp
App para criar um cadastro e enviar de acordo um vencimento uma mensagem automática via whatsapp.

Utilizando postgress

Uma criação de clientes e outras manipulações.

Para testes manda uma mensagem aqui no github :D

Para windows: 

Dê um clone no git

Em uma pasta no mesmo folder do projeto crie uma Virtual Environments através do terminal:

py -m venv venv

Depois dê o comando de iniciar usar a sua venv:

.\venv\Scripts\activate

Se você nunca criou uma venv, pode dar esse erro:
 + CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], UnauthorizedAccessException
  + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.SetExecutionPolicyCo  
 mmand

Basta executar uma nova instância do powershell ou terminal como administrador e rodar:

Set-ExecutionPolicy RemoteSigned

Abra a pasta do projeto onde existe o txt: requirements-dev.txt

pip install -r requirements-dev.txt

Para testar o aplicativo:

py manage.py runserver

O retorno do terminal tem que ser:

Starting development server at http://127.0.0.1:8000/

Para criar o banco de dados é necessário usar:

py manage.py migrate

Cria um admin:

py manage.py createsuperuser

Após isso o software estará funcionando! 
