# 🖼️ Removedor de Fundo com IA (FastAPI + Rembg)

Um projeto simples e poderoso que remove o fundo de qualquer imagem usando **Inteligência Artificial**, totalmente gratuito e open-source.  
Backend em **Python + FastAPI** e frontend leve em **HTML/JS**.

---

## 🚀 Funcionalidades

- Remove o fundo de qualquer imagem (PNG, JPG, WebP…)
- Processamento rápido usando `rembg`
- API REST simples com retorno em PNG
- Frontend pronto com preview antes/depois
- 100% gratuito, sem dependências externas de IA

---

## 🧠 Tecnologias usadas

### **Backend**
- Python 3.10+
- FastAPI
- Uvicorn
- Rembg (U²Net)
- Pillow

### **Frontend**
- HTML / CSS / JavaScript
- fetch API para envio da imagem

---

## 📂 Estrutura do projeto

```
remover-fundo/
│── main.py               # API FastAPI
│── venv/                 # Ambiente virtual
│── static/
│    └── index.html       # Frontend
│── requirements.txt      # Dependências do Python
└── README.md
```

---

## ⚙️ Como instalar e rodar

### 1. Clone o projeto
```bash
git clone https://github.com/seu-usuario/remover-fundo.git
cd remover-fundo
```

### 2. Crie o ambiente virtual
```bash
python -m venv venv
```

### 3. Ative o ambiente

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Rode o servidor FastAPI
```bash
uvicorn main:app --reload
```

A API ficará em:

👉 **http://localhost:8000/remove-bg**  
Interface gráfica:

👉 **http://localhost:8000**

Documentação:

👉 **http://localhost:8000/docs**

---

## 🧪 Testando pela API (Swagger)

Acesse:

```
http://localhost:8000/docs
```

Use o endpoint:

```
POST /remove-bg
```

Envie um arquivo de imagem e receba um PNG com fundo removido.

---

## 🎨 Frontend (Preview Antes/Depois)

O projeto inclui uma interface simples com:

- Upload da imagem
- Preview da imagem original
- Preview da imagem sem fundo
- Botão para baixar o PNG resultante

---

## 📌 Melhorias futuras

- Interface mais bonita (Tailwind)
- Suporte a remover objetos específicos
- Trocar o fundo por outra imagem
- Ajustar bordas automaticamente
- Otimizar modelo com ONNX Runtime

---

## 🧑‍💻 Autor

Criado por **Vinicius** como primeiro projeto prático no caminho para se tornar um **AI Engineer**.

---

## 📝 Licença

Este projeto é open-source e pode ser usado livremente.

---
