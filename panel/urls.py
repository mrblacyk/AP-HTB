from django.urls import path

from . import views

urlpatterns = [
    # Dashboards
    path('statistics/', views.statistics, name='statistics'),

    # News
    path('', views.news, name='news'),
    path('news/compose/', views.news_compose, name='news_compose'),

    # Machine related URLs
    path('machines/', views.machines, name='machines'),
    path('machines/start/<uuid:machine_id>/', views.start_machine,
         name='start_machine'),
    path('machines/stop/<uuid:machine_id>/', views.stop_machine,
         name='stop_machine'),
    path('machines/reset/<uuid:machine_id>/', views.reset_machine,
         name='reset_machine'),
    path('machines/cancel/<uuid:machine_id>/', views.cancel_reset_machine,
         name='cancel_reset_machine'),
    path('machines/flag/<uuid:machine_id>/', views.send_flag,
         name='send_flag'),

    # Mailbox
    path('mailbox/', views.mailbox_inbox, name='mailbox_inbox'),
    path('mailbox/trash/', views.mailbox_trash, name='mailbox_trash'),
    path('mailbox/sent/', views.mailbox_sent, name='mailbox_sent'),
    path('mailbox/compose/', views.mailbox_compose, name='mailbox_compose'),
    path('mailbox/read/<uuid:mail_id>/', views.mailbox_read,
         name='mailbox_read'),
    path('users/q.json', views.mailbox_user_query, name='mailbox_user_query'),

    # User handling URLs
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    # System related URLs
    path('sys/nat/', views.nat, name='nat'),
    path('sys/deploy-vm/', views.deploy_vm, name='deploy_vm'),
    path('upload/', views.file_upload, name='file_upload'),
]
