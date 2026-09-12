\# 🎬 Recipe Cinema



Дипломный проект: подбор рецептов по имеющимся продуктам, привязанным к фильмам и мультфильмам, с AI-адаптацией рецепта и воспроизведением саундтреков.



\## Стек



\- \*\*Backend\*\*: FastAPI, SQLAlchemy, PostgreSQL, Alembic, JWT, OpenAI

\- \*\*Frontend\*\*: React + TypeScript

\- \*\*Infra\*\*: Docker, docker-compose



\## Быстрый старт



\### 1. БД

```bash

docker-compose up -d

```



\### 2. Backend

```bash

cd backend

python -m venv venv

source venv/bin/activate   # Windows: venv\\Scripts\\activate

pip install -r requirements.txt

cp .env.example .env

alembic upgrade head

uvicorn app.main:app --reload

```



\### 3. Frontend

```bash

cd frontend

npm install

npm start

```

