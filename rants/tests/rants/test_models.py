import pytest

from main.models import Rant, Category


@pytest.mark.django_db
def test_rant_model():
    rant = Rant(title="Rant first", slug='rant-first')
    rant.save()
    assert rant.title == "Rant first"
    assert rant.slug == 'rant-first'



@pytest.mark.django_db
def test_category_model():
    category = Category(title='Category', slug='category')
    category.save()
    assert category.title == 'Category'
    assert category.slug == 'category'
    assert str(category) == category.title