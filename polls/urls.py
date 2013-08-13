from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # /polls/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/<number>/
    # url(r'^(?P<poll_id>\d+)/$', views.detail, name="detail"),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/<number>/results/
    # url(r'^(?P<poll_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/<number>/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name="vote"),
    # test one for understanding
    url(r'^(?P<poll_id>\d+)/test/$', views.test, name="test"),
)
