# Projeto Gestor Hotel – CRUD Hotel

## 📘 Descrição do Projeto
Este projeto foi desenvolvido com fins pedagógicos para o Curso Profissional de Gestão e Programação de Sistemas Informáticos (GPSI) – 10.º ano.

O objetivo principal é demonstrar como implementar operações CRUD (Create, Read, Update, Delete) em Python utilizando:

- Funções (sem classes)  
- Dicionários  
- Separação por ficheiros  
- Validação de dados  
- Menus em terminal  

O projeto simula a gestão das entidades **Cliente** e **Hotel**.

---

## 🎯 Objetivos Pedagógicos
Com este projeto foi feita por mim para aprender a:

- Organizar código em múltiplos ficheiros Python  
- Utilizar dicionários como estrutura de armazenamento  
- Implementar operações CRUD  
- Validar dados introduzidos pelo utilizador  
- Gerar identificadores automáticos  
- Trabalhar com datas em Python  
- Separar lógica de negócio da interface (menu)  

---

## 📂 Estrutura do Projeto


gestor_hotel/
├── main.py
├── cliente.py
├── hotel.py
├── utils.py
└── README.md


---

## main.py
Contém o menu interativo em terminal.

Responsável apenas por:

- Apresentar opções  
- Recolher dados do utilizador  
- Chamar funções dos módulos `cliente.py` e `hotel.py`  

**Não contém validações.**

---

## cliente.py
Contém todas as operações CRUD da entidade Cliente:

- Criar cliente  
- Listar clientes  
- Consultar cliente  
- Atualizar cliente  
- Remover cliente  

Também inclui validações como:

- Verificação de datas de nascimento  
- Geração automática de ID  

Os clientes são guardados num dicionário em memória.

---

## hotel.py
Contém todas as operações CRUD da entidade Hotel:

- Criar hotel  
- Listar hotéis  
- Consultar hotel  
- Atualizar hotel  
- Remover hotel  

Também inclui validações como:

- Geração automática de ID  

Os hotéis são guardados num dicionário em memória.

---

## utils.py
Contém funções auxiliares:

- Geração automática de IDs  
- Validação de datas no formato `YYYY-MM-DD`  

---

## 👤 Estrutura da Entidade Cliente

| Campo           | Descrição                        |
|-----------------|----------------------------------|
| id_cliente      | Identificador único (ex: C001)  |
| nome            | Nome do cliente                  |
| telefone        | Número de telefone               |
| email           | Email do cliente                 |
| data_nascimento | Data de nascimento (YYYY-MM-DD)  |

---

## 👤 Estrutura da Entidade Hotel

| Campo         | Descrição                          |
|---------------|------------------------------------|
| id_hotel      | Identificador único (ex: H001)    |
| nome          | Nome do hotel                     |
| endereco      | Morada do hotel                   |
| telefone      | Número de telefone                |
| classificacao | Classificação (ex: 1 a 5 estrelas) |

---

## ▶️ Como Executar o Projeto

1️⃣ Garantir que Python está instalado.  

2️⃣ Executar no terminal:

```bash
python main.py

3️⃣ Utilizar o menu apresentado.

📚 Conceitos Trabalhados

Este projeto permite consolidar:

Funções
Dicionários
Módulos Python
Importação entre ficheiros
Validação de dados
Estruturas condicionais
Ciclos (while)
👨‍🏫 Utilização

Este projeto foi feita por mim para:

Introdução ao CRUD
Exercícios guiados
Avaliação prática
Preparação para projetos maiores
📄 Licença Pedagógica

Projeto desenvolvido exclusivamente para fins educativos no curso GPSI – 10.º ano.

Pode ser reutilizado e adaptado livremente.
