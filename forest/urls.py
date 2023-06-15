from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ForestCreateApi.as_view(), name="forest_create"),
    path('<int:forest_id>/update/',
         ForestUpdateApi.as_view(), name='forest_update'),
    path('photos/create/',
         ForestPhotoCreateApi.as_view(), name='forest_photo_create'),
    path('<int:forest_id>/delete/',
         ForestDeleteApi.as_view(), name='forest_delete'),
    path('<int:forest_id>/like/',
         ForestLikeApi.as_view(), name='forest_like'),
    path('<int:forest_id>/',
         ForestDetailApi.as_view(), name='forest_detail'),
    path('',
         ForestListApi.as_view(), name='forest_list'),
    path('categories/',
         CategoryListApi.as_view(), name='category_list'),
    path('semi_categories/',
         SemiCategoryListApi.as_view(), name='semi_category_list'),
    path('<int:forest_id>/comments/',
         ForestCommentListApi.as_view(), name='forest_comment_list'),
    path('<int:forest_id>/comments/create/',
         ForestCommentCreateApi.as_view(), name='forest_comment_create'),
    path('<int:forest_id>/comments/<int:forest_comment_id>/update/',
         ForestCommentUpdateApi.as_view(), name='forest_comment_update'),
    path('<int:forest_id>/comments/<int:forest_comment_id>/delete/',
         ForestCommentDeleteApi.as_view(), name='forest_comment_delete'),
    path('<int:forest_id>/comments/<int:forest_comment_id>/like/',
         ForestCommentLikeApi.as_view(), name='forest_comment_like'),
]
