from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your tests here.
class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Post4',
            text='lorem ipsum dolor sit amet',
            status=Post.STATUS_CHOICES[0][0],  # published
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title='post6',
            text='lorem ipsum dolor sit amet',
            status=Post.STATUS_CHOICES[1][0],  # draft
            author=cls.user,
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEquals(str(post), post.title)

    def test_post_datail(self):
        self.assertEquals(self.post1.title, 'Post4')
        self.assertEquals(self.post1.text, 'lorem ipsum dolor sit amet')

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)

    def test_post_list_view_by_name(self):
        response = self.client.get(reverse('posts_list'))

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, 'Post4')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post1.pk}))
        self.assertContains(response, 'Post4')
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_not_found(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': 999}))
        self.assertEquals(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):  # TDD-test
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
        'title': 'some title',
        'text': 'lorem ipsum dolor sit amet',
        'status': Post.STATUS_CHOICES[0][0],  # published
        'author': self.user.id,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.last().text, 'lorem ipsum dolor sit amet')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'some title',
            'text': 'this is updated text',
            'status': Post.STATUS_CHOICES[0][0],  # published
            'author': self.post2.author.id,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.last().text, 'this is updated text')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post1.id]))
        self.assertEquals(response.status_code, 302)
    