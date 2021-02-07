from django.shortcuts import render
from rest_framework import views
from social.models import Profile, Comment, Post
from rest_framework.reverse import reverse
from .serializers import ProfileSerializer, CommentSerializer, PostSerializer, UserStatisticsSerializer, AllCommentsPostSerializer, PostProfileSerializer, PostCommentsSerializer
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

class ProfileList(ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profile-list'


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'

class ProfilePostsList(ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = PostProfileSerializer
	name = 'profile-posts-list'

	def list(self, request):
		queryset = self.get_queryset()
		serializer = PostProfileSerializer(queryset, many=True)
		return Response(serializer.data)

class ProfilePostsDetail(RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = PostProfileSerializer
	name = 'profile-posts-detail'

	def list(self, request):
		queryset = self.get_queryset()
		serializer = PostProfileSerializer(queryset, many=True)
		return Response(serializer.data)


class PostCommentsList(ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCommentsSerializer
	name = 'posts-comments-list'

	def list(self, request):
		queryset = self.get_queryset()
		serializer = PostCommentsSerializer(queryset, many=True, context={'request': request})
		return Response(serializer.data)


class PostCommentsDetail(RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCommentsSerializer
	name = 'posts-comments-detail'

	def list(self, request):
		queryset = self.get_queryset()
		serializer = PostCommentsSerializer(queryset, many=True, context={'request': request})
		return Response(serializer.data)


class AllCommentsPostDetail(RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = AllCommentsPostSerializer


class AllCommentsAllPostsDetail(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = AllCommentsPostSerializer

    multiple_lookup_fields = ('pk', 'postId')

    def get_object(self):
        queryset = self.get_queryset()

        obj = get_object_or_404(queryset, **self.kwargs)

        return obj


class UserStatisticsList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserStatisticsSerializer
    name = 'user-statistics-list'


    def list(self, request, *args, **kwargs):
        profile = self.get_object()
        
        posts = profile.posts
        comments_count = sum([post.comments.count() for post in posts.all()])

        serializer = self.get_serializer(profile)
        
        data = serializer.data.copy()
        data.update({
            'total_posts': posts.count(),
            'total_comments': comments_count
        })
        
        return Response(data)

class ApiRoot(GenericAPIView):
	name = 'ApiRoot'

	def get(self, request,*args, **kwargs):
		return Response({
			'profile': reverse(ProfileList.name, request=request),
			'comment': reverse(CommentList.name, request=request),
			'post': reverse(PostList.name, request=request),
			'profile-posts-list': reverse(ProfilePostsList.name, request=request),
			'posts-comments-list': reverse(PostCommentsList.name, request=request),
			})