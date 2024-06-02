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

import logging
logger = logging.getLogger(__name__)


def home(request):
    logger.info("Home page accessed")
    context = {
        "page_name": "home",
    }
    return render(request, "firstapp/home.html", context)


def contact(request):
    logger.info("Contact page accessed")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            logger.info(f"Sending email from {name}")
            try:
                send_mail(
                    f"Message from {name}",
                    message,
                    email,
                    ["websitesfromplanetx@gmail.com"],
                    fail_silently=False,  # raises an exception, which can then be caught
                )
                logger.info("Email sent successfully")
            except Exception as e:
                logger.error(f"Failed to send email: {e}")
                return HttpResponse("Internal Server Error", status=500)
            return redirect("thank_you")
        else:
            logger.warning("Invalid form submission attempted")
    else:
        form = ContactForm()
    return render(request, "firstapp/contact.html", {"form": form})


def thank_you(request):
    logger.info("Statement page accessed")
    return render(request, "firstapp/thank_you.html")


def statement(request):
    logger.info("Statement page accessed")
    context = {
        "page_name": "statement",
    }
    return render(request, "firstapp/statement.html", context)


# The CategoryListView is a generic ListView for the Category model.
# It uses the category_list.html template.
class CategoryListView(ListView):
    model = Category
    template_name = "firstapp/category_list.html"

    # Add logging to the get_queryset method to log when the categories are fetched.
    def get_queryset(self):
        logger.info("Fetching all categories")
        return Category.objects.all()

    # Add logging to the get_context_data method to log when the context is loaded.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug(f"Loaded context for category list with {len(context['category_list'])} items")
        return context


# The PaintingListView is a generic ListView for the Painting model.
# It uses the painting_list.html template and filters the paintings by category name.
class PaintingListView(ListView):
    template_name = "firstapp/painting_list.html"
    context_object_name = "paintings"

    # The get_queryset method is overridden to filter the paintings by category name.
    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        logger.info(f"Fetching paintings for category: {category_name}")
        return Painting.objects.filter(category__name=category_name)

    # The get_context_data method is overridden to add the category name to the context.
    # This allows the category name to be used as the page name in the template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = self.kwargs["category_name"]
        logger.debug(f"Loaded context for painting list in category {self.kwargs['category_name']} with {len(context['paintings'])} items")
        return context
