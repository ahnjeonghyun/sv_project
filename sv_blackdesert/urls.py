"""sv_blackdesert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls    import path
from admins.views   import AdminSigninView, AdminChartView
from users.views    import SignupView, UserMovieView
from quizes.views   import RewardLoadView, QuizLoadView, AnswerCheckView, ResultCheckView

urlpatterns = [
    path('admin-login', AdminSigninView.as_view()),
    path('users', SignupView.as_view()),
    path('reward/<int:quiz_num>',RewardLoadView.as_view()),
    path('quiz/<int:quiz_num>',QuizLoadView.as_view()),
    path('quiz',AnswerCheckView.as_view()),
    path('result',ResultCheckView.as_view()),
    path('chart',AdminChartView.as_view()),
    path('movie-url',UserMovieView.as_view())
]
