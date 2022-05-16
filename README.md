# DjangoRocket
Basic Paas to allow developers to quickly create industry standard CI/CD pipelines for Django based web apps. 
For initial MVP we will focus on deploying into GCP from a Github Webhook. In order to do this, we will need to
create our own Django App. The main mechanism that will allow this whole thing to work well is the settings.py.

## Configuring Django Projects
Django's configuration all happens in a script called settings.py. This is normal Python code and use all of the 
normal Python libraries that are available to any other script. Some of the settings that are in this file are 
sensitive in nature. Hence, we will need to take careful consideration to make this happen. 

## Backend Services
### Google Secrets Manager
We want to manage as little infrastructure as possible. At first, I was thinking using Vault. But that requires managing both a Vault and a Consul cluster. 
For now we will leverage Google Secrets Manager. As Terraform stores sensitive material in state, we will only create the secrets through Terraform. All secret versions will actually be created using python. https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets. For customer owner secrets, both the secret and the secret versions will be created in Python. We need to do this as they will be much more dynamically created.

### GCP CloudSQL
Our Django App will be backed by CloudSQL.


## Sub Repos
https://github.com/djaboxx/DjangoRocket_Infra
