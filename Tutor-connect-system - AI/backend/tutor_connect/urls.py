from django.contrib import admin
from django.urls import path,include
from tutoring.ai_views import tutor_recommendation, ai_chat, ai_analytics

urlpatterns = [

path('admin/',admin.site.urls),

path('api/users/',include('users.urls')),

path('api/tutoring/',include('tutoring.urls')),

path('api/messages/',include('messaging.urls')),

path('api/payments/',include('payments.urls')),
path("api/ai/recommend/", tutor_recommendation),
path("api/ai/chat/", ai_chat),
path("api/ai/analytics/", ai_analytics),

]