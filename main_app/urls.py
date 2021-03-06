from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.GroupList.as_view(), name='groups_index'),
    path('groups/<int:group_id>/', views.groups_detail, name='groups_detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:group_id>/update/', views.groups_update, name='groups_update'),
    path('groups/<int:group_id>/delete/', views.groups_delete, name='groups_delete'),
    path('groups/<int:group_id>/add_event/', views.add_event, name='add_event'),
    path('groups/<int:group_id>/add_photo/', views.add_photo, name='add_photo'),
    path('groups/<int:group_id>/apply/', views.apply_group, name='apply_group'),
    path('groups/<int:group_id>/leave/', views.leave_group, name='leave_group'),
    path('groups/<int:application_id>/accept/', views.accept_app, name='accept_app'),
    path('groups/<int:application_id>/decline', views.decline_app, name='decline_app'),
    path('groups/<int:event_id>/update_event/', views.update_event, name='update_event'),
    path('groups/<int:event_id>/delete_event/', views.delete_event, name='delete_event'),
    path('groups/<int:event_id>/attend/', views.attend_event, name='attend_event'),
    path('groups/<int:event_id>/unattend/', views.unattend_event, name='unattend_event'),
    path('accounts/signup/', views.signup, name='signup'),
]