from django.conf.urls import url, include
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^shop/', include('blog.urls', namespace='shop')),
    url(r'^$', lambda request: redirect('/shop/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
