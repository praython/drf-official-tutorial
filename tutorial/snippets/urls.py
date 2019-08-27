from . import views
from django.urls import path, include
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from snippets import views

snippet_list = SnippetViewSet.as_view({
     'get':'list',
     'post':'create'
})

snippet_detail = SnippetViewSet.as_view({
     'get':'retrieve',
     'put':'update',
     'patch':'partial_update',
     'delete':'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
     'get':'highlight'
}, renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
     'get':'list'
})

user_detail = UserViewSet.as_view({
     'get':'retrieve'
})

urlpatterns = [
    path('', views.api_root),
    path('snippets/', 
         snippet_list,
         name='snippet-list'),
    path('snippets/<int:pk>', 
         snippet_detail,
         name='snippet-detail'),
    path('users/', 
         user_list,
         name='user-list'),
    path('users/<int:pk>', 
         user_detail,
         name='user-detail'),
    path('snippets/<int:pk>/highlight/', 
         snippet_highlight,
         name='snippet-highlight'),
]

#Including format_suffix_patterns is an optional 
# choice that provides a simple, DRY way to refer 
# to a specific file format for a URL endpoint. 
# It means our API will be able to handle URls such as 
# http://example.com/api/items/4.json rather than 
# just http://example.com/api/items/4.
urlpatterns = format_suffix_patterns(urlpatterns)