from rest_framework import serializers

from articles.models import Article


class ArticleListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'title','body','categories',
            'date_create'
        )


class ArticleDetailSerializers(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Article
        exclude = ('published',)