from django.conf.urls import url
from .views import *

urlpatterns = [
  #http://localhost:8000/05-add
  url(r'^05-add/$',add_views,name='add'),
  #http://localhost:8000/06-query
  url(r'^06-query/$',query_views,name='query'),
  #http://localhost:8000/07-queryall
  url(r'^07-queryall/$',queryall_views,name='queryall'),
  #http://localhost:8000/08-update/一位以上數字
  url(r'^08-update/(\d{1,})/$',update_views,name='update'),
  #http://localhost:8000/09-update
  url(r'^09-update/$',update09_views,name='update_au'),
  #http://localhost:8000/10-delete/一位以上數字
  url(r'^10-delete/(\d+)$',delete_views,name='delete'),
]

urlpatterns += [
  url(r'^11-doF/$',doF_views),
  url(r'^12-raw/$',raw_views),
  url(r'^13-authors/$',authors_views),
  url(r'^14-oto/$',oto_views),
  url(r'^15-otm/$',otm_views),
  url(r'^16-mtm/$',mtm_views),
]

urlpatterns += [
  url(r'17-titleCount/$',titleCount_views),
]







