from django.urls import include, path

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('', include('blog.urls'))
]
