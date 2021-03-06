from django.conf.urls import patterns, url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'carname', api.carNameViewSet)
router.register(r'manufacturer', api.ManufacturerViewSet)


urlpatterns = patterns('',
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += patterns('',
    # urls for carName
    url(r'^carlist/$', views.carNameListView.as_view(), name='car_carname_list'),
    url(r'^create/$', views.carNameCreateView.as_view(), name='car_carname_create'),
    url(r'^detail/(?P<slug>\S+)/$', views.carNameDetailView.as_view(), name='car_carname_detail'),
    url(r'^update/(?P<slug>\S+)/$', views.carNameUpdateView.as_view(), name='car_carname_update'),
    url(r'^carname/(?P<num>[0-9]+)/$', views.cardetails),
    url(r'^compare/$', views.compare1),
    url(r'^compare/(?P<num1>[0-9]+)/$', views.compare2),
    url(r'^compare/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', views.compareresult),
    url(r'^$', views.cargrid, ),
)

urlpatterns += patterns('',
    # urls for Manufacturer
    url(r'^manufacturer/$', views.ManufacturerListView.as_view(), name='car_manufacturer_list'),
    url(r'^manufacturer/create/$', views.ManufacturerCreateView.as_view(), name='car_manufacturer_create'),
    url(r'^manufacturer/detail/(?P<slug>\S+)/$', views.ManufacturerDetailView.as_view(), name='car_manufacturer_detail'),
    url(r'^manufacturer/update/(?P<slug>\S+)/$', views.ManufacturerUpdateView.as_view(), name='car_manufacturer_update'),
)

