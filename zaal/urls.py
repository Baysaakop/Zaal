from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as accounts_views
from courts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # Registration
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    ## Profile
    path('account/', accounts_views.account, name='account'),
    path('mycourt/<int:pk>/', views.mycourt, name='mycourt'),
    ## Courts        
    path('courts/', views.courts, name='courts'),
    path('court/<int:pk>/', views.court, name='court'),
    ## Order

    ## Address
    path('load-districts/', views.load_districts, name='load_districts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)