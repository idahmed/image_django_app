from . import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    ## here we simply user django built in login and logout views
    ## https://docs.djangoproject.com/en/5.0/topics/auth/default/#module-django.contrib.auth.views
    path("login/", LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    ## here we include the urls from the img_resizer apps
    path("", include("img_resizer.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
