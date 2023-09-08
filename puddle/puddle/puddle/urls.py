from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # сканирует все пути в приложении итемс
    path("items/", include("item.urls")),
    # будет проверять все ссылки в приложении core
    path("", include("core.urls")),
    # сканирует все пути в приложении дашборд
    path("dashboard/", include("dashboard.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
