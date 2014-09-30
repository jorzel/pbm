from django.conf.urls import patterns, include, url
from django.contrib import admin

print admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pbm.views.about', name="about"),
    url(r'^o-nas/', 'pbm.views.about', name="about"),
    url(r'^aktualnosci/', 'pbm.views.news', name="news"),
    url(r'^badania/', 'pbm.views.research', name="research"),
    url(r'^wydarzenia/', 'pbm.views.events', name="events"),
    url(r'^aparatura/', 'pbm.views.equipment', name="equipment"),
    url(r'^kontakt/', 'pbm.views.contact', name="contact"),
    url(r'^admin/', include(admin.site.urls)),
)
