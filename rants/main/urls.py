from django.urls import path

from .api.views import RantList, RantUpdate, RantDelete
from .models import Rant
from .api.serializers import RantSerializer
from .views import RantListView, RantDetailView

app_name = 'main'


urlpatterns = [
    path('api/rants/', RantList.as_view(queryset=Rant.objects.all(), serializer_class=RantSerializer)),
    #path('api/rants/detail/<int:pk>/', RantDetail.as_view()),
    path('api/rants/update/<int:pk>/', RantUpdate.as_view(queryset=Rant.objects.all(), serializer_class=RantSerializer)),
    path('api/rants/delete/<int:pk>/', RantDelete.as_view(queryset=Rant.objects.all(), serializer_class=RantSerializer)),
    path('list/', RantListView.as_view(), name='list'),
    path('rant/<slug:slug>/', RantDetailView.as_view(), name='detail')
]
