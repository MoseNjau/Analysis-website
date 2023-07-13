from django.urls import path
from . import views

app_name="core"
urlpatterns=[
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("pricing/",views.pricing, name='pricing'),
    path("trainers/",views.trainers, name='trainers'),
    path("courses/",views.courses, name='courses'),
    path("events/", views.about, name='events')
]