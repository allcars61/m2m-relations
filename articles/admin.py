# from django.contrib import admin
#
# from .models import Article
#
#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass


from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_tags_count = 0
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main', False)
            if is_main:
                main_tags_count += 1
            if main_tags_count > 1:
                raise ValidationError('Может быть только один основной раздел')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]