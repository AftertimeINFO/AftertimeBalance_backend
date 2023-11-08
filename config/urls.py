from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/front/user/', include('core__REST_FRONT_USER.urls')),
    path('api/v1/back/', include('core__REST_BACK.urls')),
    # path('tb/', include('djTaskBrocker.urls')),
    # path('pullgerMSM/api/', include('pullgerMultiSessionManager__REST.urls')),
    # path('pullgerAM/api/', include('pullgerAccountManager__REST.urls')),
    # path('pullgerR/com_linkedin/api/', include('pullgerReflection.com_linkedin__REST.urls')),
    # path('api/account/', include('pullgerAuthJWT.urls')),
]