from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post , Comment

# Create your tests here.

class Blog_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create user for test
        testuser=User.objects.create(username='test_user1',password='123')
        testuser.save()

        #create post
        test_post=Post.objects.create(author=testuser,title='Habit',body='I love Swimming')

        #create comment with Authanticated User
        test_comment1=Comment.objects.create(post=test_post,user=testuser,comment="Beautiful Commented by Authanticated User!!",status='Love')

        #create comment with Anonymous User
        test_comment2=Comment.objects.create(post=test_post,comment="Beautiful Commented by Anonymous User!!",status='Love')

    def test_blog_content(self):
        user=User.objects.get(username='test_user1')
        post=Post.objects.get(author=user)
        author=f'{post.author}'
        title=f'{post.title}'
        body=f'{post.body}'

        #Test
        self.assertEqual(author,'test_user1')
        self.assertEqual(title,'Habit')
        self.assertEqual(body,'I love Swimming')



    def test_comment_with_anonymous_user(self):
        user=User.objects.get(username='test_user1')
        post=Post.objects.get(author=user)
        comment=Comment.objects.get(post=post)
        user=f'{comment.user}'
        com=f'{comment.comment}'
        status=f'{comment.status}'
        person=f'{comment.make_comment}'

        # Test
        self.assertEqual(user,'None')  
        self.assertEqual(com,'Beautiful Commented by Anonymous User!!')
        self.assertEqual(status,'Love')
        self.assertEqual(person,'Anonymous User')

    def test_comment_with_authanticated_user(self):
        test_user=User.objects.get(username='test_user1')
        comment=Comment.objects.get(user=test_user)
        user=f'{comment.user}'
        com=f'{comment.comment}'
        status=f'{comment.status}'
        person=f'{comment.make_comment}'

        # Test
        self.assertEqual(user,'test_user1') 
        self.assertEqual(com,'Beautiful Commented by Authanticated User!!')
        self.assertEqual(status,'Love')
        #self.assertEqual(person,'Authanticated User') I Change it im my view When save comment .



