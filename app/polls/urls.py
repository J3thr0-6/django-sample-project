from django.urls import path, include
from .views import (
    QuestionView,
    QuestionDetailView,
    ChoiceView,
    ChoiceDetailView,
    ChoiceByQuestionView,
)

urlpatterns = [
    path("question/", QuestionView.as_view(), name="questions"),
    path("question/<int:pk>/", QuestionDetailView.as_view(), name="question details"),
    path("choice/", ChoiceView.as_view(), name="choices"),
    path("choice/<int:pk>/", ChoiceDetailView.as_view(), name="choice details"),
    path(
        "question/<int:question_id>/choices/",
        ChoiceByQuestionView.as_view(),
        name="question choices",
    ),
]
