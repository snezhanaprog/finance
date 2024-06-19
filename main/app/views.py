from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Все поля обязательны для заполнения'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Пользователь с таким именем уже существует'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token = Token.objects.create(user=user)
        return Response({'token': str(token)}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Имя пользователя и пароль обязательны для ввода'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Неверное имя пользователя или пароль'}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)


class BudgetList(APIView):
    def get(self):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BudgetDetail(APIView):

    def get_object(self, pk):
        return Budget.objects.get(user=self.request.user, pk=pk)

    def get(self, request, pk):
        budget = self.get_object(pk)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, pk):
        budget = self.get_object(pk)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        budget = self.get_object(pk)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SavingGoalList(APIView):

    def get(self, request):
        saving_goals = SavingGoal.objects.all()
        serializer = SavingGoalSerializer(saving_goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SavingGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavingGoalDetail(APIView):

    def get_object(self, pk):
        return SavingGoal.objects.get(pk=pk, user=self.request.user)

    def get(self, request, pk):
        saving_goal = self.get_object(pk)
        serializer = SavingGoalSerializer(saving_goal)
        return Response(serializer.data)

    def put(self, request, pk):
        saving_goal = self. get_object(pk)
        serializer = SavingGoalSerializer(saving_goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        saving_goal = self.get_object(pk)
        saving_goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenseList(APIView):

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):

    def get_object(self, pk):
        return Expense.objects.get(pk=pk, user=self.request.user)

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncomeList(APIView):

    def get(self, request):
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetail(APIView):

    def get_object(self, pk):
        return Income.objects.get(pk=pk, user=self.request.user)

    def get(self, request, pk):
        income = self.get_object(pk)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    def put(self, request, pk):
        income = self.get_object(pk)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        income = self.get_object(pk)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









