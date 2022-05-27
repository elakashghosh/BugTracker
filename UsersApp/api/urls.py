from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from UsersApp.api.views import (Registration_view, Logout_view, 
                                Is_activeList_view, UpdateAccountStatus_view,
                                CustomAuthTokenAV, UserDetails, )

urlpatterns = [
    path('login/', CustomAuthTokenAV.as_view(), name='login'),
    path('register/', Registration_view.as_view(), name='registration'),
    path('logout/', Logout_view.as_view(), name='logout'),
    path('is_activelist/', Is_activeList_view.as_view(), name='is_activelist'),
    path('activate/<str:email>/<int:activate>', UpdateAccountStatus_view.as_view(), name='activateAccount'),
    path('user-details/<int:pk>/', UserDetails.as_view(), name='user-details')
]