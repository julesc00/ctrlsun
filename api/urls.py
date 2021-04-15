from rest_framework.routers import SimpleRouter

from .views import BranchLocationViewSet, UserViewSet, WorkingTimeViewSet, StaffViewSet

router = SimpleRouter()
router.register("branches", BranchLocationViewSet, basename="branches")
router.register("users", UserViewSet, basename="users")
router.register("staff", StaffViewSet, basename="staff")
router.register("working-time", WorkingTimeViewSet, basename="working-time")

urlpatterns = router.urls
