from django.conf import settings
from django.conf.urls.static import static
from core.views import index, contact
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('contact/', contact, name='contact'),
    # Add a space after the comma in the include function
    path('items/', include('item.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
