import factory
from django.contrib.auth.models import User
from .models import Post,Category
from factory.faker import faker

FAKER= faker.Faker()
class PostsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    title = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username='cxd')[0]
    # category = Category.objects.get_or_create(id=1)[0]

    @factory.lazy_attribute
    def content(self):
        x = ''
        for _ in range(5):
            x += "\n " +FAKER.paragraph(nb_sentences=30)
        return x
    status =  'published'

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.tags.add(extracted)
        else:
            self.tags.add("python","django", "datgabase",)


#x = PostsFactory.create_batch(10)
 #   from blog.factory import PostsFactory