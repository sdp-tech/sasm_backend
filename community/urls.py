from django.urls import path
from .views import BoardPropertyDetailApi, PostListApi, PostDetailApi, PostCreateApi, PostUpdateApi, PostDeleteApi, PostLikeApi, PostHashtagListApi, PostCommentListApi, PostCommentCreateApi, PostCommentUpdateApi, PostCommentDeleteApi, PostReportCreateApi, PostCommentReportCreateApi

urlpatterns = [
     path('boards/<int:board_id>/',
          BoardPropertyDetailApi.as_view(), name='board_property_detail'),
     path('posts/',
          PostListApi.as_view(), name='post_list'),
     path('posts/<int:post_id>/',
          PostDetailApi.as_view(), name='post_detail'),
     path('posts/create/', PostCreateApi.as_view(), name='post_create'),
     path('posts/<int:post_id>/update/',
          PostUpdateApi.as_view(), name='post_update'),
     path('posts/<int:post_id>/delete/',
          PostDeleteApi.as_view(), name='post_delete'),
     path('posts/<int:post_id>/like/',
          PostLikeApi.as_view(), name='post_like'),
     path('post_hashtags/',
          PostHashtagListApi.as_view(), name='post_hashtag_list'),
     path('post_comments/',
          PostCommentListApi.as_view(), name='post_comment_list'),
     path('post_comments/create/',
          PostCommentCreateApi.as_view(), name='post_comment_create'),
     path('post_comments/<int:post_comment_id>/update',
          PostCommentUpdateApi.as_view(), name='post_comment_update'),
     path('post_comments/<int:post_comment_id>/delete',
          PostCommentDeleteApi.as_view(), name='post_comment_delete'),
     path('post_reports/create/',
          PostReportCreateApi.as_view(), name='post_report_create'),
     path('post_comment_reports/create/',
          PostCommentReportCreateApi.as_view(), name='post_comment_report_create'),
]
