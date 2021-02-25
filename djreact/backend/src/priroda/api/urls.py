# from django.urls import path, include

# from .views import (
#     PrirodaListView,
#     PrirodaDetailView,
#     PrirodaCreateView,
#     PrirodaDeleteView,
#     PrirodaUpdateView
# )

# urlpatterns = [ 
#     path('', PrirodaListView.as_view()),
#     path('create/', PrirodaCreateView.as_view()),
#     path('<pk>/delete', PrirodaDeleteView.as_view()),
#     path('<pk>/update', PrirodaUpdateView.as_view()),
#     path('<pk>', PrirodaDetailView.as_view()),
# ]

from priroda.api.views import PrirodaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PrirodaViewSet, basename='priroda')
urlpatterns = router.urls