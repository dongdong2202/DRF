from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='cxd11', password='12311' )
        test_post = Post.objects.create(category_id=1, 
            title='Post Title', excerpt='abc', 
            content='efzzz',author_id=1,slug='post-title', status='published')
        
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = post.excerpt
        title = post.title
        content = post.content
        status = post.status
        
        self.assertEqual(title, 'Post Title')
        self.assertEqual(author,'cxd11')
        self.assertEqual(content, 'efzzz')
        self.assertEqual(status,'published')
        self.assertEqual(excerpt, 'abc')
        self.assertEqual(str(post),'Post Title')
        self.assertEqual(str(cat),'django')


