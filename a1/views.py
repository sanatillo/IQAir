from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import os
from django.conf import settings

class HtmlFileSendView(APIView):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'static', 'index.html')

        if not os.path.exists(file_path):
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Return HTML content with proper content type
        return HttpResponse(html_content, content_type='text/html')
