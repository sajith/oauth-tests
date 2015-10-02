from django.conf.urls import url, include
from rest_framework import routers

from . import views

# ------------------------------------------------------------

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# ------------------------------------------------------------

urlpatterns = [
    # login URLs for the browsable API - stuff for rest_framework
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

# ------------------------------------------------------------

    # /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /polls/[[:number:]]/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /polls/[[:number:]]/results
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # /polls/[[:number:]]/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# ------------------------------------------------------------
