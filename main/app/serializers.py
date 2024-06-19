from rest_framework import serializers
from .models import *


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['name', 'total_amount', 'user']


class SavingGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavingGoal
        fields = ['user', 'title', 'description', 'amount', 'saved_amount',
                  'date_created', 'date_updated', 'target_date']


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ['title', 'user', 'description', 'date_created', 'amount']


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        models = Income
        fields = ['user', 'title', 'description', ' amount', ' date_created']
