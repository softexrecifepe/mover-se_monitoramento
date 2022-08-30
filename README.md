
<h1 align="center"><img src="https://user-images.githubusercontent.com/16292535/150152830-a0077ec7-d677-4e19-b282-04401bb5a060.png" alt="logos Ceweb.br NIC.br CGI.br " width="250" height="auto"></h1>

<h1 align="center">
    <img src="https://ceweb.br/media/imgs/Moverse_na_Web_banner-site.jpg" alt="Vamos transformar Brumadinho. Projeto Mover-se na WEB!" width="450" height="auto">
</h1>

[![Software License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://github.com/mas-cli/mas/blob/main/LICENSE)

<h1 align="center"> Sistema de Monitoramento em Tempo Real de Qualidade de Água de um Rio </h1>

O projeto Sistema de Monitoramento em Tempo Real de Qualidade de Água de um Rio faz parte da chamada pública [CGI.br/NIC.br/Ceweb.br nº 01/2019
Mover-Se na Web – Articulação Pró-Brumadinho](https://ceweb.br/projetos/chamada.html)

<p>Abaixo, liste a licença/s para o projeto. Lembre-se que todas as soluções devem possuir uma licença de código aberto, assim como todos os produtos produzidos com o aporte oferecido pelo Ceweb.br | NIC.br | CGI.br. </p>

#  Descrição da solução

Aqui você deve adicionar uma descrição do projeto. Texto corrido, não maior que ~600 caracteres e/ou ~100 palavras.

### Funcionalidades ativas

- [x] Cadastro de criação de usuário
- [x] Cadastro de Denúncia
- [x] Cadastro de uma fonte

### Funcionalidades em desenvolvimento
- [x] Moderação de comentários
- [x] Moderação de ativos

### Papeis e suas descrições

-  Usuário: Uma breve descrição sobre os papeis do usuário na operação do sistema.
-  Moderador: Uma breve descrição sobre os papeis do Moderador na operação do sistema.
-  Administrador: Uma breve descrição sobre os papeis do Administrador na operação do sistema.

#  Instalação

### Tecnologias utilizadas

- [Django](https://www.djangoproject.com/)
- [PWA](https://reactnative.dev/)
- [Arduino](https://www.arduino.cc/)

## Executando o Projeto

### Pré-requisitos (Software e/ou Hardware)

Sofware:

- [Git](https://git-scm.com)
- [Python](https://nodejs.org/en/). 
- [Redis](https://redis.io/) \* 
\* Funcionalidade de Alerta


Hardware:
- [Arduino](https://www.arduino.cc/)
- [LILYGO® TTGO T-SIM7000G](https://pt.aliexpress.com/item/4000542688096.html)
- [Mini Painel Solar](https://pt.aliexpress.com/item/4001189122748.html)
- [Sensor PH](https://pt.aliexpress.com/item/32957428276.html)
- [Sensor Temperatura](https://pt.aliexpress.com/item/1005004412646322.html)
- [Caixa de Proteção IP68] (https://pt.aliexpress.com/item/4000019605315.html)

### 1. No terminal

```bash
# Clone este repositório
$ git clone https://github.com/cewebbr/mover-se_monitoramento-qualidade-agua

# Acesse a pasta do projeto no terminal
$ cd mover-se_monitoramento-qualidade-agua/web

# Instale as dependências
$ pip install -r requirements.txt

# Crie um arquivo `.env` na bws/bws raiz do projeto
$ cp .env-exemple .env
```

###  2. Configuração das variáveis de ambientes

Abra o arquivo `.env` na raiz do projeto e configure as variáveis de ambiente

```
twitter_api_key=""
twitter_api_secret=""
secret=""
DATABASE_URL=""
```
###  3. Criação do Banco de Dados e Administrador
```bash
# Execute o comando para criar a base de dados
$ python manage.py migrate --run-syncdb

# Cria um administrador do sistema
$ python manage.py createsuperuser
```

###  4. Executando a aplicação
```bash
# Execute a aplicação com o sevidor de desenvolvimento
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse < http://localhost:8000 >
```

</br>

#### Solução de problemas

Descreva aqui caso existam problemas conhecidos, como pacotes, conflitos entre versões e se possível, como resolver ou um artigo que auxilie na solução. Caso não existir, omitir a seção.

<br/>

### Equipe responsável pelo projeto 

- Ana Maria         - UFRJ - Coordenadora - ana@email.com.br
- João da Silva     - UFMG - Pessoa desenvolvedora - joao@email.com.br
- Luciana de Souza  - UFPR - Pessoa desenvolvedora - luciana@email.com.br

</br>


# Sobre o [Ceweb.br](https://ceweb.br/sobre-o-ceweb-br/), [NIC.br](https://www.nic.br/sobre/) e [CGI.br](https://cgi.br/sobre/)

### Ceweb.br - Centro de Estudos sobre Tecnologias Web
O Centro de Estudos sobre Tecnologias Web (Ceweb.br) foi criado como um departamento do Núcleo de Informação e Coordenação do Ponto BR (NIC.br) para viabilizar a participação da comunidade brasileira no desenvolvimento global da Web e subsidiar a formulação de políticas públicas. O Ceweb.br nasce inspirado pelos princípios e projetos já desenvolvidos pelo Escritório Brasileiro do W3C (World Wide Web Consortium), hospedado e apoiado pelo NIC.br no Brasil desde 2008, com a missão de promover atividades que estimulem o uso de tecnologias abertas e padronizadas na Web.


### NIC.br - Núcleo de Informação e Comunicação do Ponto BR
O Núcleo de Informação e Coordenação do Ponto BR - NIC.br foi criado para implementar as decisões e os projetos do Comitê Gestor da Internet no Brasil - CGI.br, que é o responsável por coordenar e integrar as iniciativas e serviços da Internet no País.


### CGI.br - Comitê Gestor da Internet no Brasil
O Comitê Gestor da Internet no Brasil tem a atribuição de estabelecer diretrizes estratégicas relacionadas ao uso e desenvolvimento da Internet no Brasil e diretrizes para a execução do registro de Nomes de Domínio, alocação de Endereço IP (Internet Protocol) e administração pertinente ao Domínio de Primeiro Nível ".br". Também promove estudos e recomenda procedimentos para a segurança da Internet e propõe programas de pesquisa e desenvolvimento que permitam a manutenção do nível de qualidade técnica e inovação no uso da Internet

### Equipe Ceweb.br

<ul>
    <li>Amanda Marques</li> 
    <li>Ana Eliza</li>
    <li>Beatriz Rocha</li>
    <li>Caroline Burle</li>
    <li>Diego Cerqueira</li>
    <li>Diogo Cortiz</li>
    <li>Juliana Ribeiro</li>
    <li>Reinaldo Ferraz</li>
    <li>Selma de Morais</li>
    <li>Vagner Diniz</li>
</ul>
