Essa aplicação web foi desenvolvida em Django para o gerenciamento completo de produtos de um restaurante.
O sistema permite cadastrar, listar, editar e excluir produtos, além de controlar sua disponibilidade.
Conta com uma interface moderna e responsiva, pensada para facilitar o uso diário por administradores e funcionários.

# 🍽️ Restaurant Manager (Gerenciamento de Restaurante)

Sistema web para gerenciamento de produtos de restaurante, desenvolvido com **Django**.  
A aplicação oferece uma interface intuitiva para realizar **operações CRUD** (criar, ler, atualizar e deletar) de produtos, controlando também sua disponibilidade.

---

## 🚀 Funcionalidades

- ✅ Cadastro de novos produtos  
- 📝 Edição de informações de produtos existentes  
- 🗑️ Exclusão de produtos  
- 📋 Listagem de produtos com nome, preço e status de disponibilidade  
- 🎨 Interface moderna e responsiva utilizando HTML e CSS  

---

## 🧠 Tecnologias Utilizadas

- **Python 3.14**
- **Django 5.2**
- **SQLite3** (banco de dados padrão)
- **HTML5**
- **CSS3 (Custom + Bootstrap-like Design)**
- **Virtualenv** (para isolamento do ambiente)

---

## 📁 Estrutura do Projeto

restaurant_manager/  
│  
├── manage.py  
├── db.sqlite3  
│  
├── restaurant_manager/ # Configurações principais do Django  
│ ├── init.py  
│ ├── settings.py  
│ ├── urls.py  
│ ├── wsgi.py  
│ └── asgi.py  
│  
└── products/ # App principal  
├── init.py  
├── admin.py  
├── apps.py  
├── forms.py  
├── models.py  
├── tests.py  
├── urls.py  
├── views.py  
├── migrations/  
│ └── ...  
└── templates/  
└── products/  
├── base.html  
├── product_list.html  
├── product_form.html  
├── product_confirm_delete.html  


---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório
```
git clone https://github.com/DeyvisonSSilva/restaurant_Manager.git
cd restaurant-manager
```
### 2. Crie e ative um ambiente virtual
```
python -m venv venv
```
No Windows:
```
venv\Scripts\activate
```
No Linux/macOS:
```
source venv/bin/activate
```
### 3. Instale as dependências
```
pip install django
```
### 4. Realize as migrações do banco de dados
```
python manage.py makemigrations
python manage.py migrate

```
### 5. Inicie o servidor
```
python manage.py runserver

```

### 6. Acesse no navegador
```
http://127.0.0.1:8000/

```
### 🧩 Estrutura das Telas

Tela Inicial: Lista todos os produtos cadastrados.

Novo Produto: Formulário para adicionar um novo item.

Editar Produto: Permite alterar dados de um produto existente.

Excluir Produto: Exibe confirmação antes da exclusão.

### 📞 Meus Contatos

👤 Deyvison Silva 

💼 Área: Educação e Desenvolvimento de Software 

🎓 Cursando Análise e Desenvolvimento de Sistemas — Uninassau  

📍 Pernambuco, Brasil  

📧 E-mail: deyvisonper@hotmail.com

💻 GitHub: [github.com/deyvisonsilva](https://github.com/DeyvisonSSilva)

💼 LinkedIn: [linkedin.com/in/deyvisonsilva](https://www.linkedin.com/in/deyvison-francisco-74a9b0230/)

### 🏆 Licença

O uso desse projeto é livre para fins educacionais e aprendizado.
