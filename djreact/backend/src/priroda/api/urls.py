from django.urls import path, include

from .views import PrirodaListView, PrirodaDetailView

urlpatterns = [ 
    path('', PrirodaListView.as_view()),
    path('<pk>', PrirodaDetailView.as_view()),
    path('api/', include('articles.api.urls'))
]