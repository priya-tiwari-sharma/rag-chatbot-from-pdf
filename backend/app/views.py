# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .serializers import FileUploadSerializer, AskQuerySerializer
from rest_framework import status
import time
import pickle
import os
from utils.utils import Validate_openAI_key, gen_pkl, get_response

class OpenAIKeyView(APIView):
    def post(self, request, *args, **kwargs):
        global api_key
        try:
            api_key=request.data.get("openai_key")
            response = Validate_openAI_key(api_key)
            return Response({'message': 'OpenAI API Key is valid'})
        except Exception as e:
            return Response({"error": 'OpenAI API Key is not valid'}, status=400)
        
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

        global vectorstore

        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            file = serializer.validated_data['file'] 
            for item in os.listdir('uploads'):
                os.remove(f'uploads/{item}')
            pdf_path = f"uploads/{file.name}"
            # saving pdf file
            open(pdf_path, "wb").write(file.read())

            # generating pickle from pdf file
            vectorstore = gen_pkl(pdf_path,api_key)

            return Response({'message': 'File uploaded successfully.'})
        else:
            return Response(serializer.errors, status=400)


class AskQueryView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            serializer = AskQuerySerializer(data=request.data)

            if serializer.is_valid():
                query = serializer.validated_data['query']        
                
                # get query response
                response = get_response(query, vectorstore,api_key)

                return Response({'response': response})
            
        except Exception as e:
            if e.args[0] == "name 'vectorstore' is not defined":
                error = "Upload a PDF file before asking a question."
            else:
                error = e.args[0]
            print(error)
            print(type(error))
            return Response({"error": error}, status=500)
        else:
            return Response(serializer.errors, status=400)