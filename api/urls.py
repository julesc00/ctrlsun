from rest_framework.routers import SimpleRouter

from .views import BranchLocationViewSet, UserViewSet, WorkingTimeViewSet

router = SimpleRouter()
router.register("branches", BranchLocationViewSet, basename="branches")
router.register("users", UserViewSet, basename="users")
router.register("workingtimes", WorkingTimeViewSet, basename="workingtimes")

urlpatterns = router.urls
