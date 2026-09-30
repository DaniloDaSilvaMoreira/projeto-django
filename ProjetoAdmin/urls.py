from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# 1. Definição das rotas padrão do sistema
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('recipes.urls'))  
]

# 2. Vinculação explícita e obrigatória para servir os arquivos locais de Mídia e Static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
