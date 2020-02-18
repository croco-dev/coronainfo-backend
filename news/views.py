from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .serializers import NewsSerializer
import urllib.request
import os
import json


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewsSerializer

    def list(self, request):
        data = {"news": []}
        client_id = os.environ.get("NAVER_SEARCH_CLIENT_ID")
        client_secret = os.environ.get("NAVER_SEARCH_CLIENT_SECRET")
        encText = urllib.parse.quote("코로나19")
        url = "https://openapi.naver.com/v1/search/news.json?query=" + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            json_body = json.loads(response_body.decode("utf-8"))
            data["news"] = json_body["items"]
        else:
            return Response(rescode, status=rescode)
        data["total"] = len(data["news"])
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

