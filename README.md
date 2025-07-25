# ChatBot_PT

Proyecto de chatbot personalizado utilizando **Angular** en el frontend y **FastAPI** en el backend, con almacenamiento de contexto en Redis y embeddings gestionados localmente.

---

## 📂 Estructura del proyecto

```

ChatBot_PT/
├── backend/               # API con FastAPI
│   ├── app/
│   ├── tests/             # Pruebas unitarias
│   └── Dockerfile
├── frontend/              # Interfaz Angular
│   └── Dockerfile
├── docker-compose.yml     # Orquestador de servicios
└── README.md

````

---

## 🚀 Despliegue local

### Backend

1. Entra al directorio:

```bash
cd backend
````

2. Crea un entorno virtual e instala dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Crea los embeddings (si no existen):

```bash
python app/training/prepare_data.py
```
o
```bash
python -m app.training.prepare_data
```

4. Levanta el backend:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

### Frontend

1. Entra al directorio:

```bash
cd frontend
```

2. Instala dependencias:

```bash
npm install
```

3. Corre el servidor Angular:

```bash
ng serve
```

Abre en tu navegador: [http://localhost:4200](http://localhost:4200)

---

## 🐳 Despliegue con Docker y Docker Compose

### 1. Clona el repositorio

```bash
git clone https://github.com/oxgerrero/ChatBot_PT.git
cd ChatBot_PT
```

### 2. Levanta todo con un solo comando:

```bash
docker compose up --build
```

Esto levantará:

* FastAPI en `localhost:8000`
* Angular en `localhost:4200`
* Redis como almacenamiento del contexto

---

## 🧪 Pruebas (backend)

Dentro del directorio `/backend`:

### 1. Instala dependencias (si no lo hiciste):

```bash
pip install -r requirements.txt
```

### 2. Ejecuta los tests con `pytest`:
```bash
pip install pytest httpx pytest-mock
```

luego ejecutar las pruebas

```bash
pytest tests/
```

---

## 🔧 Variables importantes

Puedes usar `.env` para manejar configuraciones como:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
EMBEDDINGS_FILE=app/embeddings/data.pkl
```

---

## 📦 Tecnologías

* 🧠 FastAPI + LangChain + OpenAI API
* 🎨 Angular
* 🧰 Redis
* 🐋 Docker + Compose
* ✅ Pytest

---

## ✍️ Autor

Hecho con 💻 por [David Gomez](https://github.com/oxgerrero)

---