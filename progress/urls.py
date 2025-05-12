from rest_framework import routers

from .views import ProgressViewset

app_name = 'progress'
router = routers.SimpleRouter()
router.register('progress',ProgressViewset)

urlpatterns = router.urls