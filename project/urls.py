from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('admin/', admin.site.urls),
    path('lists/', include('todo.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Static media in DEBUG mode
