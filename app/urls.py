from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import NewCarCreateView, CarsListView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view
# from cars.urls import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("cars/", CarsListView.as_view(), name="cars_list"),
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car_update"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
