from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Sudoku API",
        default_version='v1',
        description="Best sudoku game ever!",
    ),
    validators=['ssv'],
    public=True,
    permission_classes=(AllowAny,)
)
