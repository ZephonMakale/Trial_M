from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # url(r'^home/$', views.home, name='home'),
    
    url(r'^$', views.home_projects, name='homePage'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile/(?P<username>[0-9]+)$',
        views.individual_profile_page, name='individual_profile_page'),
    url(r'^new/project$', views.new_project, name='new_project'),  
    url(r'^image(\d+)', views.project, name='project'), 
    url(r'^new/image$', views.new_image, name='new_image'), 
    url(r'^api/project/$', views.ProjectList.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)    