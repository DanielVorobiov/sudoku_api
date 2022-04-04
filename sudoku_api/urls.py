from django.urls import path, include

from sudoku_api.helper import schema_view

urlpatterns = [
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('user/', include('users.urls')),
    path('statistics/', include('stats.urls')),
    path('sudoku/', include('sudoku.urls'))
]
