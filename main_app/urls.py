from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/<int:member_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/update/',
         views.ProfileUpdate.as_view(template_name="main_app/member_form.html"), name='profile_update'),
    path('profile/<int:member_id>/change_photo/',
         views.change_photo, name='change_photo'),
    path('questions/create/', views.QuestionCreate.as_view(),
         name='question_create'),
    path('questions/', views.questions_index, name='questions_index'),
    path('questions/<int:question_id>/',
         views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/add_answer/',
         views.add_answer, name='add_answer'),
    path('questions/<int:pk>/update/',
         views.QuestionUpdate.as_view(template_name="main_app/question_update_form.html"), name='question_update'),
    path('questions/<int:pk>/delete/',
         views.QuestionDelete.as_view(), name='question_delete'),
    path('like/',
         views.like_answer, name='like_answer'),
    path('like_q/',
         views.like_question, name='like_question'),
    path('questions/<str:category>/', views.questions_sort, name='questions_sort')
]
