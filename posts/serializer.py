from rest_framework import serializers
from posts.models import Post ,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','author','title','body','image','create_at')
        extra_kwargs={'author':{'read_only':True},
        'Type':{'read_only':True}
        }

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('user','post','comment','status','make_comment','create_at')
        extra_kwargs={'user':{'read_only':True},
        'Type':{'read_only':True},
        'make_comment':{'read_only':True},
        'Type':{'read_only':True}
        }