from rest_framework import serializers
from .models import Script, Comment


class ScriptSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )

    script_url = serializers.ModelSerializer.serializer_url_field(
        view_name='script_detail')

    class Meta:
        model = Script
        fields = ('id', 'title', 'name',
                  'genre', 'logline', 'comments', 'upload', 'script_url')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    script = serializers.PrimaryKeyRelatedField(
        queryset=Script.objects.all(), source='script.id')

    class Meta:
        model = Comment
        fields = ('id', 'script', 'comment', 'script_id')

    def create(self, validated_data):
        comment = Comment.objects.create(script=validated_data['script']['id'],
        comment=validated_data['comment'])
        return comment
