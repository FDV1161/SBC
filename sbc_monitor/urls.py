from django.urls import path
from sbc_monitor import views

app_name="sbc_monitor"

urlpatterns = [    
    path('test/', views.test, name='test'),
    path('test/<int:id>', views.test2),
]


