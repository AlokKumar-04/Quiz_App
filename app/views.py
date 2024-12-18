from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question
import random

# Session keys
SESSION_KEY_TOTAL_QUESTIONS = "total_questions"
SESSION_KEY_CORRECT_ANSWERS = "correct_answers"
SESSION_KEY_QUESTION_IDS = "question_ids"


def start_quiz(request):
    request.session[SESSION_KEY_TOTAL_QUESTIONS] = 0
    request.session[SESSION_KEY_CORRECT_ANSWERS] = 0
    request.session[SESSION_KEY_QUESTION_IDS] = []
    return render(request, "start_quiz.html")


def get_question(request):
    answered_ids = request.session.get(SESSION_KEY_QUESTION_IDS, [])
    question = Question.objects.exclude(id__in=answered_ids).order_by('?').first()

    if not question:
        return JsonResponse({"message": "No more questions available."})

    request.session[SESSION_KEY_QUESTION_IDS].append(question.id)
    return JsonResponse({
        "id": question.id,
        "question": question.question_text,
        "options": [
            question.option_1,
            question.option_2,
            question.option_3,
            question.option_4,
        ],
    })


def submit_answer(request):
    if request.method == "POST":
        question_id = int(request.POST.get("question_id"))
        selected_option = int(request.POST.get("selected_option"))

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return JsonResponse({"error": "Invalid question."}, status=400)

        total_questions = request.session.get(SESSION_KEY_TOTAL_QUESTIONS, 0) + 1
        correct_answers = request.session.get(SESSION_KEY_CORRECT_ANSWERS, 0)

        if question.correct_option == selected_option:
            correct_answers += 1

        request.session[SESSION_KEY_TOTAL_QUESTIONS] = total_questions
        request.session[SESSION_KEY_CORRECT_ANSWERS] = correct_answers

        return JsonResponse({
            "correct": question.correct_option == selected_option,
            "correct_answers": correct_answers,
            "total_questions": total_questions,
        })


# Create your views here.
