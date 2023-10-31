from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class QuestionView(APIView):
    def get(self, request):
        try:
            questions = Question.objects.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        req_data = request.data
        try:
            serializer = QuestionSerializer(data=req_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class QuestionDetailView(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(
                {"error": "question not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):
        try:
            question = self.get_object(pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk):
        req_data = request.data
        try:
            question = self.get_object(pk)
            serializer = QuestionSerializer(question, data=req_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            question = self.get_object(pk)
            question.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ChoiceView(APIView):
    def get(self, request):
        try:
            choices = Question.objects.all()
            serializer = QuestionSerializer(choices, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, format=None):
        req_data = request.data
        try:
            serializer = QuestionSerializer(data=req_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ChoiceByQuestionView(APIView):
    def get(self, request, question_id):
        try:
            choices = Choice.objects.filter(question=question_id)
            serializer = ChoiceSerializer(choices, many=True)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response(
                {"error": "question not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ChoiceDetailView(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(
                {"error": "question not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):
        try:
            question = self.get_object(pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response(
                {"error": "question not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk):
        req_data = request.data
        try:
            question = self.get_object(pk)
            serializer = QuestionSerializer(question, data=req_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "e"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            question = self.get_object(pk)
            question.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "e"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
