from django.urls import re_path

from . import views



urlpatterns = [
    

    # ex: /
    re_path(r'^$', views.review_list, name='review_list'),

    # ex: /review/5/
    re_path(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),

    # ex: /book/
    re_path(r'^book$', views.book_list, name='book_list'),

    # ex: /book/5/
    re_path(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
    re_path(r'^book/(?P<book_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),

    # ex: /review/user - get reviews for the logged user
    re_path(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    re_path
    (r'^review/user/$', views.user_review_list, name='user_review_list'),

]