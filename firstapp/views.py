from django.shortcuts import render
from django.http import HttpResponse

# content management
from django.views.generic import ListView
from .models import Category, Painting

# contact form
from django.shortcuts import redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    context = {
        "page_name": "home",
        # "message": "Hello, user!",
    }
    return render(request, "firstapp/home.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_config["name"]
            send_mail(
                f"Message from {name}",
                message,
                email,
                ["mortensengarth@hotmail.com"],  # Adjust to where you want to receive messages
                fail_silently=False,
            )
            return redirect("thank_you")
    else:
        form = ContactForm()
    return render(request, "firstapp/contact.html", {"form": form})


def thank_you(request):
    return render(request, "firstapp/thank_you.html")


def statement(request):
    context = {
        "page_name": "statement",
    }
    return render(request, "firstapp/statement.html", context)


# The CategoryListView is a generic ListView for the Category model.
# It uses the category_list.html template.
class CategoryListView(ListView):
    model = Category
    template_name = "firstapp/category_list.html"


# The PaintingListView is a generic ListView for the Painting model.
# It uses the painting_list.html template and filters the paintings by category name.
class PaintingListView(ListView):
    template_name = "firstapp/painting_list.html"
    context_object_name = "paintings"

    # The get_queryset method is overridden to filter the paintings by category name.
    def get_queryset(self):
        return Painting.objects.filter(category__name=self.kwargs["category_name"])

    # The get_context_data method is overridden to add the category name to the context.
    # This allows the category name to be used as the page name in the template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = self.kwargs["category_name"]
        return context
