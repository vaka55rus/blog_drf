from django.urls import path

from articles.views import *

urlpatterns = [
    path('list/', ArticleListView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
    path('create/', ArticleCreateView.as_view()),
]