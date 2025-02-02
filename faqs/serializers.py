# faqs/serializers.py

from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at']

    def to_representation(self, instance):
        lang = self.context.get('request').query_params.get('lang', 'en')
        data = super().to_representation(instance)
        
        translated_content = instance.get_translated_content(lang)
        data['question'] = translated_content['question']
        data['answer'] = translated_content['answer']
        
        return data