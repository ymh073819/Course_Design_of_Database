"""数据库课程设计 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import include, url
from myproject.views import *
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [                                            #name是命名空间，可以在html文件中引用
    url(r'^verification_code/\d+/$',verification_code,name='verification_code'),
    url(r'^$',index, name='index'),
    url(r'^login/$',do_login,name='login'),
    url(r'^register/$',do_reg,name='register'),
    url(r'^logout/$',do_logout,name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^log_reg/$',log_reg,name='log_reg'),
    url(r'^data_in/$',data_in,name='data_in'),
    url(r'^data_out/$',data_out,name='data_out'),
    url(r'^query/$',query,name='query'),
    url(r'^query2/$',query2,name='query2'),
    url(r'^analyse/$',analyse,name='analyse'),
    url(r'^analyse2/$',analyse2,name='analyse2'),
    url(r'^data2base/$',data2base,name='data2base'),

]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
