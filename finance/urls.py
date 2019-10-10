from django.urls import path
from finance import views
from .views import home_view, Blog_Page, Blog_post


urlpatterns = [
    path('', home_view.as_view(), name="Home"),
    path('blog_post/<int:pk>/', Blog_post.as_view(), name="Blog-Post"), #this route takes us to a specific post.
    path('Blog/', Blog_Page.as_view(), name="Blog"),
    path('about/', views.about_page_view, name="About"),
    path('contact/', views.contact_page_view, name="Contact"),
    
]