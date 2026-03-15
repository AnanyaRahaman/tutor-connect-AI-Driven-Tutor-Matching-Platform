# Tutor Connect (AI Driven TutorMatching Platform)

Tutor Connect is a full-stack tutoring platform that connects students with tutors for online or offline learning.
The platform now includes **advanced AI features**, including a machine learning tutor recommendation system, a RAG-powered AI assistant, and an AI analytics agent.

This project demonstrates a **modern AI architecture** combining:

* Machine Learning
* LLMs
* Retrieval-Augmented Generation (RAG)
* LangChain Agents
* Django + React full-stack development

---

# Key Features

## Student Features

* Create tutoring requests
* Search tutors
* Chat with tutors
* Book tutoring sessions
* Pay for sessions securely

## Tutor Features

* Browse student requests
* Manage tutoring schedule
* Chat with students
* Track tutoring income

## Platform Features

* JWT authentication
* Real-time chat (WebSockets)
* Stripe payment integration
* PostgreSQL database
* Docker deployment

---

# AI Features

## 1. Machine Learning Tutor Recommendation System

A **RandomForest model** predicts the most suitable tutors based on:

* Subject match
* Tutor rating
* Price difference
* Availability
* Tutor experience

The system ranks tutors using **predicted probabilities** from the trained model.

---

## 2. AI Chat Assistant (RAG)

A **Retrieval-Augmented Generation (RAG)** assistant allows users to ask natural language questions such as:

```
Find a Python tutor under $40
Who teaches calculus?
```

The assistant:

1. Retrieves tutor data
2. Converts it into vector embeddings
3. Searches using a vector database (FAISS)
4. Uses an LLM to generate the final response

Technologies used:

* LangChain
* OpenAI
* FAISS vector database

---

## 3. AI Analytics Agent

An AI agent allows administrators to query platform analytics using natural language.

Example queries:

```
Which tutor earned the most last month?
Which subject is most requested?
```

The system converts natural language into **SQL queries** and retrieves data from the PostgreSQL database.

---

# AI Architecture

```
User
  │
Frontend (React)
  │
Django API
  │
AI Engine
 ├── ML Recommendation Model
 ├── RAG Chat Assistant
 └── AI SQL Analytics Agent
  │
PostgreSQL Database
```

---

# Technology Stack

## Backend

* Django
* Django REST Framework
* Django Channels
* PostgreSQL

## Frontend

* React
* Axios
* React Router

## AI / Machine Learning

* scikit-learn
* pandas
* numpy

## LLM / RAG

* LangChain
* OpenAI
* FAISS vector database

## DevOps

* Docker
* Environment variables

---

# Project Structure

```
backend
│
├── ai_engine
│   ├── ml_models
│   ├── rag_system
│   └── agents
│
├── users
├── tutoring
├── messaging
├── payments
│
├── tutor_connect
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

---

# Installation

## Clone the Repository

```
git clone https://github.com/AnanyaRahaman/tutor-connect-platform.git
cd tutor-connect-platform
```

---

# Backend Setup

Create virtual environment

```
python -m venv venv
```

Activate

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

Install dependencies

```
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create `.env` file:

```
backend/.env
```

Example:

```
SECRET_KEY=django-secret

DB_NAME=tutorconnect
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

OPENAI_API_KEY=your_openai_key

STRIPE_SECRET_KEY=your_stripe_key
STRIPE_PUBLIC_KEY=your_stripe_key
```

---

# Database Setup

Create PostgreSQL database:

```
CREATE DATABASE tutorconnect;
```

Run migrations:

```
python manage.py migrate
```

Create admin user:

```
python manage.py createsuperuser
```

---

# Train Machine Learning Model

Before running the system, train the recommendation model:

```
python ai_engine/ml_models/train_model.py
```

This generates:

```
tutor_model.pkl
```

---

# Run Backend Server

```
python manage.py runserver
```

Backend API:

```
http://127.0.0.1:8000
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

# Run Frontend

```
cd frontend
npm install
npm start
```

Frontend:

```
http://localhost:3000
```

---

# Example AI API Endpoints

## Tutor Recommendation

```
POST /api/ai/recommend
```

Example request:

```
{
 "subject":"Math",
 "budget":40
}
```

---

## AI Chat Assistant

```
POST /api/ai/chat
```

Example request:

```
{
 "message":"Find a Python tutor under $30"
}
```

---

## AI Analytics

```
POST /api/ai/analytics
```

Example:

```
Which tutor earned the most last month?
```

---

# Future Improvements

* Hybrid ML + vector recommendation
* Personalized tutor ranking
* Tutor performance prediction
* Automatic tutor scheduling
* Reinforcement learning recommendation system

---

# Author

Ananya Rahaman
