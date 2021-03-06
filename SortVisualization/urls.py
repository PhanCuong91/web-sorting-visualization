"""SortVisualization URL Configuration

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
from django.contrib import admin
from django.urls import path
from Sorting import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('SortingVisualization/', views.SortingVisualization.as_view(), name='sorting-vizualization'),
    path('admin/', admin.site.urls),
    #using for ajax in chart.html
    path('SortingVisualization/SelectionSort/', views.SelectionView.as_view(), name='selection-sort'),
    path('SortingVisualization/InsertionSort/', views.InsertionView.as_view(), name='insertion-sort'),
    path('SortingVisualization/MergeSort/', views.MergeView.as_view(), name='merge-sort'),
]
