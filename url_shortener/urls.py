from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from shortener.api import router as shortener_router


api = NinjaAPI(title="URL Shortener API", version="1.0", description="短網址 API 服務")

api.add_router("/shortener/", shortener_router)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]