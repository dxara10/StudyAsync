from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
import usuarios
from usuarios.views import cadastro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('flashcard/', include('flashcard.urls')),
    path('apostilas/', include('apostilas.urls')),
    path('', include(usuarios.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)