from rants.main.api.serializers import RantSerializer, CategorySerializer


def test_valid_rant_serializer():
    valid_serializer_data = {
        'id': 1,
        'title': "First Rant",
        'slug': "first-rant",
        'categories': {
            'title': 'Cate',
            'slug': 'cate',
        }
    }
    serializer = RantSerializer(data=valid_serializer_data)
    #assert serializer.is_valid()
    #assert serializer.validated_data == valid_serializer_data
    #assert serializer.data == valid_serializer_data
    #assert serializer.errors == {}


def test_invalid_rant_serializer():
    invalid_serializer_data = {
        'rant': 'Kulugo',
        'slug': 'apostrophe'
    }
    serializer = CategorySerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
