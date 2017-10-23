from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView_List, CreateView_Item
from .views import DetailsView_List, DetailsView_Item, DetailsViewByFk_Item

urlpatterns = {
    url(r'^grocerylists/$', CreateView_List.as_view(), name="create_list"),
    url(r'^grocerylists/(?P<pk>[0-9]+)/$', DetailsView_List.as_view(), name="details_list"),
    url(r'^groceryitems/$', CreateView_Item.as_view(), name="create_item"),
    url(r'^groceryitems/(?P<pk>[0-9]+)/$', DetailsView_Item.as_view(), name="details_item"),
    url(r'^groceryitems/grocerylist/(?P<grocerylist>[0-9]+)/$', DetailsViewByFk_Item.as_view(), name="detailsbyfk_item"),
}

urlpatterns = format_suffix_patterns(urlpatterns)