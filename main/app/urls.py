from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),

    path('budgets/', BudgetList.as_view(), name='budgets'),
    path('budgets/<int:pk>/', BudgetDetail.as_view(), name='budget'),

    path('saving_goals/', SavingGoalList.as_view(), name='saving_goals'),
    path('saving_goals/<int:pk>/', SavingGoalDetail.as_view(), name='saving_goal'),

    path('expenses/', ExpenseList.as_view(), name='expenses'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense'),

    path('incomes/', IncomeList.as_view(), name='incomes'),
    path('incomes/<int:pk>/', IncomeDetail.as_view(), name='income'),
]
