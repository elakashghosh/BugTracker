from django.urls import path, include
from BugsApp.api.views import (report_view, my_reports_view, show_all_view, get_bug_view)

urlpatterns = [
    path('report/', report_view.as_view(), name='report'),
    path('my-reports/<int:pk>/', my_reports_view.as_view(), name='my-reports'),
    path('show-all/', show_all_view.as_view(), name='show-all-bugs'),
    path('bug-details/<int:pk>/', get_bug_view.as_view(), name='bug-details'),
]