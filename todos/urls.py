from django.urls import path
from . import views #viewsにあるすべてを持ってくる

#  listings

urlpatterns = [
    path('', views.index, name='index'),
    path('done', views.done, name='done'),
    path("update_todos/<int:todo_id>/", views.update_todos, name="update_todos"),
    path("update_categories", views.update_categories, name="update_categories"),
]

