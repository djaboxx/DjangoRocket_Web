from django.contrib import admin
from django.urls import path, include
from account.views import Signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', Signup.as_view(), name="account_signup"),
    path('password', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name="account_password_reset")
    # path('organization/create', name='org_create'),
    # path('organizations/invite/(?P<org_id>[0-9]+)', name='org_invite'),
    # path('teams/create', name='team_create'),
    # path('teams/invite/(?P<team_id>[0-9]+)', name='team_invite'),
    # path('teams/list', name='team_list'),
    # path('teams/(?P<team_id>[0-9]+)/users', name='team_list_members'),
    # path('teams/destroy/(?P<team_id>[0-9]+)', name='team_destroy'),
]
