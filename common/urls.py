from django.urls import path

from app_comment import views as comment_views
from app_product import views as product_views
from app_user import views as user_views

urlpatterns = [
    path('register/', user_views.RegisterView.as_view()),
    path('login/', user_views.LoginView.as_view()),
    path('product/', product_views.ProductViewForUser.as_view()),
    path('product-for-admin/', product_views.ProductViewForAdmin.as_view()),
    path('comment/', comment_views.CommentView.as_view())
]
