
from django.contrib import admin
from django.urls import path ,include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view



API_TITLE = 'Blog API'
API_DESCRIPTION = 'Blog API That Using For Post Articles and Picture and Make Comments On Its'

schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('posts.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('registration/',include('rest_auth.registration.urls')),
    path('docs/',include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
    path('swagger-docs/',schema_view),

]

