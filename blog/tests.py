from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your tests here.
class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Post4',
            text='lorem ipsum dolor sit amet',
            status=Post.STATUS_CHOICES[0][0],  # published
            author=user,
        )
        cls.post2 = Post.objects.create(
            title='post6',
            text='lorem ipsum dolor sit amet',
            status=Post.STATUS_CHOICES[1][0],  # draft
            author=user,
        )
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
