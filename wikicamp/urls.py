from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikicamp.views.home', name='home'),
    # url(r'^wikicamp/', include('wikicamp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#   (r'^admin/', include(admin.site.urls)), 
(r'^wikicamp/(?P<page_name>[^/]+)/edit/$', 'wikicamp.wiki.views.edit_page'),
(r'^wikicamp/(?P<page_name>[^/]+)/save/$', 'wikicamp.wiki.views.save_page'),
(r'^wikicamp/(?P<page_name>[^/]+)/$', 	   'wikicamp.wiki.views.view_page'),
)       

#	 (r'^wikicamp/(?P<page_name>[^/]+)/edit/$', 'wikicamp.wiki.views.edit_page'),
#        (r'^wikicamp/(?P<page_name>[^/]+)/save/$', 'wikicamp.wiki.views.save_page'),
#        (r'^wikicamp/(?P<page_name>[^/]+)/$', 'wikicamp.wiki.views.view_page'),
#       	(r'^wikicamp/page/(?P<page_name>[^/]+)/edit/$', 'wikicamp.wiki.views.edit_page'),
#        (r'^wikicamp/page/(?P<page_name>[^/]+)/save/$', 'wikicamp.wiki.views.save_page'),        
#        (r'^wikicamp/page/(?P<page_name>[^/]+)/$', 'wikicamp.wiki.views.view_page'),
#)
