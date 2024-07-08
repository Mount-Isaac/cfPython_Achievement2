from django.urls import path, include
from .views import recipes_home
from .views import RecipesListView, RecipesDetailView
from django.conf.urls.static import static
from django.conf import settings

app_name = "recipes"

urlpatterns = [
    path("", recipes_home, name="recipes_home"),
    path("recipes/", RecipesListView.as_view(), name="recipes_list"),
    path("list/<pk>", RecipesDetailView.as_view(), name="detail")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)