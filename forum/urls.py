from rest_framework import routers

from .views import (
    ForumThreadViewset, ForumReplyViewset
)

app_name = 'forum'
router = routers.SimpleRouter()
router.register('thread',ForumThreadViewset)
router.register('reply',ForumReplyViewset)

urlpatterns = router.urls
