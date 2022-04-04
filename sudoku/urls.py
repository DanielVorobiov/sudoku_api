from rest_framework.routers import DefaultRouter

from .views import SudokuViewSet

router = DefaultRouter()
router.register('', SudokuViewSet, basename='sudoku')

urlpatterns = router.urls
