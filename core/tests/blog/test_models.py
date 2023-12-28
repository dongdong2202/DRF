import pytest
pytestmark = pytest.mark.django_db
from blog.models import Category

class TestPostModel:
    def test_str_return(self, post_factory):
        c = Category()
        c.name = 'django'
        post = post_factory(title='goodaeeesdf22' )
        assert post.__str__() == 'goodaeeesdf22'