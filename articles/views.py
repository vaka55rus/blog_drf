from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleListSerializers, ArticleDetailSerializers


class ArticleListView(APIView):
    """
    Вывод списка статей
    """

    def get(self, request):
        queryset = Article.objects.filter(published=True)
        serializer = ArticleListSerializers(queryset, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    """
    Вывод деталей статей
    """

    def get(self, request, pk):
        queryset = Article.objects.get(id=pk, published=True)
        serializer = ArticleDetailSerializers(queryset)
        return Response(serializer.data)