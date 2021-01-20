from rest_framework import generics
from django.db.models import Q

from .models import Article
from .serializers import ArticleListSerializers, ArticleDetailSerializers


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializers

    def get_queryset(self):
        queryset = Article.objects.filter(Q(published=True) | Q(author=self.request.user))
        return queryset


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializers
    queryset = Article.objects.all()


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializers
