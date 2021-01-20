from rest_framework import generics

from .models import Article
from .serializers import ArticleListSerializers, ArticleDetailSerializers, ArticleCreateSerializer


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializers
    queryset = Article.objects.filter(published=True)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializers
    queryset = Article.objects.all()


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleCreateSerializer