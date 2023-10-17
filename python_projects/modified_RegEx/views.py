from django.shortcuts import render
from .modified_RegEx_logic import modified_RegEx
from django.http import HttpResponse, FileResponse
from django.template import loader

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

        try:
            with open(file.name, 'w') as archivo:
                archivo.write(modified_text)
        except Exception as e:
            return render(request, "error.html", {'error': str(e)})

        context = {
            'positions': positions,
            'modified_text': modified_text
        }

        return render(request, "index.html", context)
    else:
       
        return render(request, "error.html")

def download_file(request, file_name):
    with open(file_name + '.txt', 'r') as file:
        response = HttpResponse(file.read(), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="modified_file.txt"'
        return response