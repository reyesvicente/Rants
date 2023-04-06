import json
import pytest
from main.models import Rant, Category


@pytest.mark.django_db
def test_add_rant(client):
    rants = Rant.objects.all()
    assert len(rants) == 0

    resp = client.post(
        "http://localhost:8000/api/rants/",
        {
            'title': "First Rant",
            'categories': {
                'title': 'Rant',
            }
        },
        content_type='application/json'
    )
    assert resp.status_code == 201
    assert resp.data['title'] == 'First Rant'

    rants = Rant.objects.all()
    assert len(rants) == 1
