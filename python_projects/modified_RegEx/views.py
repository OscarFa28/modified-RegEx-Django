from django.shortcuts import render
from .modified_RegEx_logic import modified_RegEx
from django.utils.html import escapejs

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

