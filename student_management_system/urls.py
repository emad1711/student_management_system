from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_management_system import settings

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_management_app.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

