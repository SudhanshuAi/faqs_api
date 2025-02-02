# faqs/models.py

from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    answer_bn = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_cached_translation(self, field, lang):
        cache_key = f"faq_{self.id}_{field}_{lang}"
        cached = cache.get(cache_key)
        
        if cached:
            return cached
            
        original = getattr(self, field)
        translated_field = f"{field}_{lang}"
        
        if hasattr(self, translated_field) and getattr(self, translated_field):
            translation = getattr(self, translated_field)
        else:
            translator = Translator()
            translation = translator.translate(original, dest=lang).text
            
        cache.set(cache_key, translation, timeout=86400)
        return translation

    def get_translated_content(self, lang='en'):
        if lang == 'en':
            return {
                'question': self.question,
                'answer': self.answer
            }
        
        return {
            'question': self.get_cached_translation('question', lang),
            'answer': self.get_cached_translation('answer', lang)
        }