from django.urls import path, include
from RelationApp.api.views import (AssignAV, myWorkAV, allAssignedWorkAV, UpdateBugStatusAV, )

urlpatterns = [
    path('assign/', AssignAV.as_view(), name='assign'),
    path('jobs/<int:myId>/', myWorkAV.as_view(), name='my-work'),
    path('all-jobs/', allAssignedWorkAV.as_view(), name='all-jobs'),
    path('update-bug-status/<int:pk>/', UpdateBugStatusAV.as_view(), name='update-bug-status'),
]