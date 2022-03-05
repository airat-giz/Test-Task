from django.urls import path
from . import views


urlpatterns = [
    path('table/', views.TableList.as_view()),
    path('table/<int:pk>/', views.TableDetail.as_view())
]
