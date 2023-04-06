from django.urls import path

from .views import RantList, RantUpdate, RantDelete
from .models import Rant
from .serializers import RantSerializer

app_name = 'main'


urlpatterns = [
    path('api/rants/', RantList.as_view(queryset=Rant.objects.all(), serializer_class=RantSerializer)),
    #path('api/rants/detail/<int:pk>/', RantDetail.as_view()),
    path('api/rants/update/<int:pk>/', RantUpdate.as_view(queryset=Rant.objects.all(), serializer_class=RantSerializer)),
    path('api/rants/delete/<int:pk>/', RantDelete.as_view(queryset=Rant.objects.all(), serializer_class=RantSerializer)),
]
