from django.contrib import admin
from django.urls import path,include
from api.views import InvoiceViewSet, InvoiceDetailsViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'invoices',InvoiceViewSet)
router1=routers.DefaultRouter()
router1.register(r'invoice1',InvoiceDetailsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('<int:id>/',include(router.urls)),
    path('invoice_details/',include(router1.urls))
]