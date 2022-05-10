from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='home_page'),
    path('about/', views.about, name='about'),
    path('boards/<int:board_id>/', views.boardTopics, name='boardTopics'),
    path('boards/<int:board_id>/new/', views.newTopic, name="newTopic"),
    path('boards/<int:board_id>/topics/<int:topic_id>', views.topic_posts, name='topicPosts'),
    path('boards/<int:board_id>/topics/<int:topic_id>/reply/', views.replyTopic, name='replyTopic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]