from rest_framework import routers

from .views import (
    QuestionViewset,QuizViewset,
    AnswerViewset , UserAnswerViewset
)

app_name = 'quiz'
router = routers.SimpleRouter()
router.register('quiz',QuizViewset)
router.register('question',QuestionViewset)
router.register('answer',AnswerViewset)
router.register('user/answer',UserAnswerViewset)

urlpatterns = router.urls