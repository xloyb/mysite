from django.urls import path,include
from .views import home,CreerPost, ModifierPost, ModifierPost, SupprimerPost, ListePosts, DetailPost
urlpatterns = [
    
    # path('', home, name="home"),
    path('', ListePosts.as_view(), name='liste_posts'), 
    path('<int:pk>/', DetailPost.as_view(), name='detail_post'), 
    path('ajouter/', CreerPost.as_view(), name='creer_post'), 
    path('<int:pk>/modifier/', ModifierPost.as_view(), name='modifier_post'), 
    path('<int:pk>/supprimer/', SupprimerPost.as_view(), name='supprimer_post'), 

]
