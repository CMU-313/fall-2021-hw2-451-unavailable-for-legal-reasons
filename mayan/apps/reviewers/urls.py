from django.conf.urls import url


from .views import table

urlpatterns_reviewers = [
    url(
        regex=r'^reviewers/$', name='reviewers',
        view=table
    ),
    
]

urlpatterns = []
urlpatterns.extend(urlpatterns_reviewers)
