from django.contrib import admin
from django.urls import path
from damawka.views import damawka_view

urlpatterns = [
    path('', damawka_view),
    path('admin/', admin.site.urls),
]
