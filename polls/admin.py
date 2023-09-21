from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)

    list_display = ('question_text', 'pub_date')
    fieldsets = [
        (
            None,
            {
                "fields": ["question_text",],
            },
        ),
        (
            "Advanced options",
            {
                "fields": ["pub_date",],
            },
        ),
    ]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        return [
            path(
                "custom_page/",
                self.admin_view(self.custom_page),
                name="custom_page"
            )
        ] + super().get_urls()

    def custom_page(self, request):
        context = {
            "text": "Hello Admin",
            "page_name": "Custom Page",
            "app_list": self.get_app_list(request), **self.each_context(request)
        }
        return render(request, "admin/custom_page.html", context)

admin.site.__class__ = CustomAdminSite
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
