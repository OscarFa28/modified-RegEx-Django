from django.shortcuts import render
from .modified_RegEx_logic import modified_RegEx
from django.utils.html import escapejs
from .huffman_logic import FileCompression
import os
import heapq
import io
from io import BytesIO
import lzma
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
# Create your views here.
def index(request):
    
    return render(request, "index.html")

def regEx_process(request):
    if request.method == 'POST' and request.FILES['txt_file']:
        
        logic = modified_RegEx()
        
        file = request.FILES['txt_file']
        query = request.POST.get('query') 
        new = request.POST.get('new') 
        
        text = file.read().decode('utf-8')  
        try:
            positions = logic.read_first_function(query, new, text)
        except Exception as e:
            return render(request, "error.html", {'error': str(e)})
        
        modified_text = logic.return_text()
        modified_text = escapejs(modified_text)
        
        context = {
            'positions': positions,
            'modified_text': modified_text
        }

        return render(request, "index.html", context)
    else:
       
        return render(request, "error.html")

def file_compressor(request):
    
    return render(request, "file_compressor.html")

def compress_file(request):
    uploaded_file = request.FILES['file']
    new_file_name = request.POST.get('file-name', '')  # Obtener el nombre del archivo del cliente
    compress = request.POST.get('compress', '').lower() == 'true'

    file_name = uploaded_file.name
    file_extension = os.path.splitext(file_name)[1]

    if compress:
        if file_extension == ".txt":  
            compressed_data = lzma.compress(uploaded_file.read())

            if not new_file_name:
                new_file_name = 'compressed_file'

            new_file_name += ".oyz"
            response = HttpResponse(compressed_data, content_type='application/x-xz')
            response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
            return response
        
        elif file_extension == ".png":
            compressed_data = lzma.compress(uploaded_file.read())

            if not new_file_name:
                new_file_name = 'compressed_file'

            new_file_name += ".oyz"
            response = HttpResponse(compressed_data, content_type='application/x-xz')
            response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
            return response
        
        elif file_extension == ".mp3":
            compressed_data = lzma.compress(uploaded_file.read())

            if not new_file_name:
                new_file_name = 'compressed_file'

            new_file_name += ".oyz"
            response = HttpResponse(compressed_data, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
            return response
        
        elif file_extension == ".mp4":
            compressed_data = lzma.compress(uploaded_file.read())

            if not new_file_name:
                new_file_name = 'compressed_file'

            new_file_name += ".oyz"
            response = HttpResponse(compressed_data, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
            return response
        
        else:
            return HttpResponseBadRequest("Error: No se ingresó un archivo válido")
        
        
    else:
        file_decompressor = FileCompression()
        file_extension_name = new_file_name
        if file_extension != ".oyz":
            return HttpResponseBadRequest("Error: No se ingresó un archivo válido")
        
        if "mp3" in file_extension_name:
            datos_descomprimidos = lzma.decompress(uploaded_file.read())

            response = HttpResponse(datos_descomprimidos, content_type='audio/mpeg')  
            response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
            return response
        elif "txt" in file_extension_name:
            datos_descomprimidos = lzma.decompress(uploaded_file.read())

            response = HttpResponse(datos_descomprimidos, content_type='text/plain') 
            response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
            return response
        
        elif "png" in file_extension_name:
            datos_descomprimidos = lzma.decompress(uploaded_file.read())

            response = HttpResponse(datos_descomprimidos, content_type='image/png') 
            response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
            return response
        
        elif "mp4" in file_extension_name:
            datos_descomprimidos = lzma.decompress(uploaded_file.read())

            response = HttpResponse(datos_descomprimidos, content_type='video/mp4') 
            response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
            return response


    return HttpResponse("File type not handled for compression")
        
            

    
