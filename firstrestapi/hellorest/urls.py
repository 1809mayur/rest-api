from django.urls import path,include

from . import views
from firstrestapi.urls import router

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
	path('',views.hello,name='hello'),
	path('router',include(router.urls)),

]
