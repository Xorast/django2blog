from django.urls    import path
from .views         import login, register, logout, profile


urlpatterns = [
    path('login',    login,    name='Login'),
    path('register', register, name='Register'),
    path('logout',   logout,   name='Logout'),
    path('profile',  profile,  name='Profile'),
]
