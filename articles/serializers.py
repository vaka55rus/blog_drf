from rest_framework import serializers

from articles.models import Article


class ArticleListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title',)


class ArticleDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'