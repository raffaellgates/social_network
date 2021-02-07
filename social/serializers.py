from rest_framework import serializers

from .models import Profile, Comment, Post
from social import views

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Profile
		fields = (
	        'id',
	        'name',
	        'username',
	        'email',
	        'street',
            'suite',
            'city',
            'zipcode'
        )


class CommentSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Comment
		fields = (
			'id',
			'name',
			'email',
			'body'
		)



class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    total_posts = serializers.IntegerField(read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    class Meta:
        model = Profile
        fields = (
        	'id',
        	'name',
        	'total_posts',
        	'total_comments'
        )

class PostProfileSerializer(serializers.ModelSerializer):
	post = serializers.StringRelatedField(many=True)

	class Meta:
		model = Profile
		fields = ['id', 'name', 'username', 'email', 'street', 'suite', 'city', 'zipcode' ,'post']



class PostCommentsSerializer(serializers.HyperlinkedModelSerializer):
	commet = serializers.StringRelatedField(many=True)
	
	class Meta:
		model = Post
		fields = ['user', 'id', 'title', 'body', 'commet',]


class AllCommentsPostSerializer(serializers.HyperlinkedModelSerializer):
	commet = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
	
	class Meta:
		model = Post
		fields = fields = ['user', 'id', 'title', 'body', 'commet',]