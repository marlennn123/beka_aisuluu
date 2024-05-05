from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieViewSets.as_view({'get':'list',
                                  'post':'create'}), name='movie_list'),
    path('<int:pk>/', MovieViewSets.as_view({'get':'retrieve', 'put':'update',
                                           'delete':'destroy'}), name='movie_detail'),

    path('marka/', CategoryViewSets.as_view({'get':'list',
                                  'post':'create'}), name='category_list'),
    path('marka/<int:pk>/', CategoryViewSets.as_view({'get':'retrieve',  'put':'update',
                                                    'delete':'destroy'}), name='category_detail')
]
