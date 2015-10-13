from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<inv_id>[0-9]+)/delete$', views.delete_inventory, name="del_inv"),
        url(r'^add$', views.add_inventory, name="add_inv"),
        url(r'^(?P<inv_id>[0-9]+)$', views.inventory, name="inv"),
]
