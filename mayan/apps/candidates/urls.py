from django.conf.urls import url


from .views import table

urlpatterns_candidates= [
    url(
        regex=r'^candidates/$', name='candidates',
        view=table
    ),
    
]

urlpatterns = []
urlpatterns.extend(urlpatterns_candidates)
