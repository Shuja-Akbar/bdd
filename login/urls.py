from django.conf.urls import url


from login import views as login_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^login/$', login_views.login_root, name='login_root'),
	url(r'^login/success/$', login_views.login_success, name='login_success'),
	url(r'^login/fail/$', login_views.login_fail, name='login_fail'),
]
