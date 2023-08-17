from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question, Subject


# Create your views here.
class StartQuizView(TemplateView):
    template_name = "cards/start_quiz.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.order_by("name")
        return context

    def post(self, request):
        years = request.POST.getlist("year")
        if years == []:
            messages.add_message(request, messages.ERROR, "year_empty")
            return self.get(request)

        years = list(map(lambda y: "1" if y == "mp2i" else "2", years))

        subject_ids = request.POST.getlist("subjects")
        if subject_ids == []:
            messages.add_message(request, messages.ERROR, "subject_empty")
            return self.get(request)

        chapters_ids = []
        for subject_id in subject_ids:
            subject_chapters_ids = request.POST.getlist(f"chapters-{subject_id}")
            if subject_chapters_ids == []:
                messages.add_message(request, messages.ERROR, f"chapters_{subject_id}_empty")
                return self.get(request)

            chapters_ids += [
                int(subject_chapters_id)
                for subject_chapters_id in subject_chapters_ids
            ]

        number_of_questions = int(request.POST.get("nb-questions"))
        if number_of_questions < 1:
            messages.add_message(request, messages.ERROR, "nb_too_shorts")
            return self.get(request)

        # Get question ids
        questions = Question.objects.filter(chapter__pk__in=chapters_ids)

        if len(years) == 1:
            questions = questions.filter(chapter__year=years[0])

        questions = questions.order_by("?")[:number_of_questions]

        request.session["question_ids"] = [
            q.id for q in questions
        ]

        return redirect("cards:card")

class CardView(TemplateView):
    template_name = "cards/card.html"

    def get(self, request):
        question_ids = self.request.session.get("question_ids")
        if question_ids is None:
            messages.add_message(self.request, messages.ERROR, "invalid_session")
            return redirect("cards:start_quiz")

        if question_ids == []:
            messages.add_message(self.request, messages.INFO, "quiz_done")
            return redirect("cards:start_quiz")

        question_id = question_ids.pop(0)
        self.request.session["question_ids"] = question_ids
        context = {
            "question": Question.objects.get(pk=question_id)
        }

        return render(request, self.template_name, context)

class AddQuestion(LoginRequiredMixin, CreateView):
    model = Question
    template_name_suffix = "_add"
    fields = [
        "chapter",
        "question",
        "answer",
    ]
    success_url = reverse_lazy("cards:add")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.order_by("name")
        return context

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, "success")
        return super().form_valid(form)
