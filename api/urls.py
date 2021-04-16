from rest_framework.routers import SimpleRouter

from .views import BranchLocationViewSet, UserViewSet, WorkingTimeViewSet, StaffViewSet

router = SimpleRouter()
router.register(r"branches", BranchLocationViewSet, basename="branches")
router.register(r"users", UserViewSet, basename="users")
router.register(r"staff", StaffViewSet, basename="staff")
router.register(r"working-time", WorkingTimeViewSet, basename="working-time")

urlpatterns = router.urls
