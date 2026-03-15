from rest_framework.decorators import api_view
from rest_framework.response import Response

from tutoring.models import Tutor

from ai_engine.ml_models.recommender import recommend_tutors
from ai_engine.rag_system.vector_store import build_vector_store
from ai_engine.rag_system.rag_chat import ask_rag
from ai_engine.agents.analytics_agent import create_agent


@api_view(['POST'])
def tutor_recommendation(request):

    student = request.data

    tutors = Tutor.objects.all()

    tutor_list = []

    for t in tutors:
        tutor_list.append({
            "name": t.name,
            "subject": t.subject,
            "rating": t.rating,
            "price": t.price,
            "available": t.available,
            "experience": t.experience
        })

    results = recommend_tutors(student, tutor_list)

    return Response(results[:5])


@api_view(['POST'])
def ai_chat(request):

    question = request.data.get("message")

    tutors = Tutor.objects.all()

    tutor_list = []

    for t in tutors:
        tutor_list.append({
            "name": t.name,
            "subject": t.subject,
            "rating": t.rating,
            "price": t.price,
            "experience": t.experience
        })

    vector_store = build_vector_store(tutor_list)

    answer = ask_rag(question, vector_store)

    return Response({"reply": answer})


@api_view(['POST'])
def ai_analytics(request):

    question = request.data.get("query")

    agent = create_agent()

    result = agent.run(question)

    return Response({"answer": result})