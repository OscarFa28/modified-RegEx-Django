import os
from huffman_logic import FileCompression
from PIL import Image
import base64
from django.http import HttpResponse

class CompressFile():
    
    def __init__(self, file, new_file_name, compress):
        # Inicialización de la clase con parámetros de entrada
        self.uploaded_file = file  # Archivo subido
        self.file_name = new_file_name  # Nuevo nombre de archivo
        self.compress_bool = compress  # Bandera para comprimir
        self.file_extension = self.get_file_extension()  # Obtiene la extensión del archivo
        self.fc = FileCompression()  # Instancia de la clase para la compresión de archivos
        
    def get_file_extension(self):
        # Obtiene la extensión del archivo
        return os.path.splitext(self.uploaded_file)[1]
        
    def main_logic(self):
        # Lógica principal para comprimir o descomprimir archivos
        compress = self.compress_bool
        file_extension = self.file_extension
        
        if compress:
            if file_extension == ".txt":  
                
                compressed_data = self.fc.compress(self.uploaded_file)
                if not new_file_name:
                    new_file_name = 'compressed_file'

                new_file_name += ".oyz"
                
                # Crear una respuesta HTTP para descargar el archivo comprimido
                response = HttpResponse(compressed_data, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
                return response
            
            elif file_extension == ".png":
                
                data_read = self.uploaded_file.read()
                
                file_data = base64.b64encode(data_read).decode('utf-8')
                
                compressed_data = self.fc.huffman_compress(file_data)
                if not new_file_name:
                    new_file_name = 'compressed_file'

                new_file_name += ".oyz"
                
                response = HttpResponse(compressed_data, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
                return response
            
            elif file_extension == ".mp3":
                data_read = self.uploaded_file.read()
                
                file_data = base64.b64encode(data_read).decode('utf-8')
                
                compressed_data = self.fc.huffman_compress(file_data)

                if not new_file_name:
                    new_file_name = 'compressed_file'

                new_file_name += ".oyz"
                
                response = HttpResponse(compressed_data, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
                return response
            
            elif file_extension == ".mp4":
                data_read = self.uploaded_file.read()
                
                file_data = base64.b64encode(data_read).decode('utf-8')
                
                compressed_data = self.fc.huffman_compress(file_data)

                if not new_file_name:
                    new_file_name = 'compressed_file'

                new_file_name += ".oyz"
                
                response = HttpResponse(compressed_data, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
                return response
            
            else:
                response = {
                    "error": None
                }
                return response
            
            
        else:
           # Si se necesita descomprimir el archivo
            file_extension_name = new_file_name
            if file_extension != ".oyz":
                # Validar si el archivo está en un formato comprimido válido
                response = {
                    "error": None
                }
                return response
            
            if "mp3" in file_extension_name:
                datos_descomprimidos = self.fc.decompress(self.uploaded_file)
                compressed_data = base64.b64decode(datos_descomprimidos)


                # Crear una respuesta HTTP para descargar el archivo comprimido
                response = HttpResponse(compressed_data, content_type='audio/mpeg')  
                response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
                return response
            
            elif "txt" in file_extension_name:
                datos_descomprimidos = self.fc.decompress(self.uploaded_file)
                compressed_data = base64.b64decode(datos_descomprimidos)

                
                response = HttpResponse(compressed_data, content_type='text/plain') 
                response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
                return response
            
            elif "png" in file_extension_name:
                datos_descomprimidos = self.fc.decompress(self.uploaded_file)
                compressed_data = base64.b64decode(datos_descomprimidos)
                
                response = HttpResponse(compressed_data, content_type='image/png') 
                response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
                return response
            
            elif "mp4" in file_extension_name:
                datos_descomprimidos = self.fc.decompress(self.uploaded_file)
                compressed_data = base64.b64decode(datos_descomprimidos)
                
                response = HttpResponse(compressed_data, content_type='video/mp4') 
                response['Content-Disposition'] = 'attachment; filename="datos_descomprimidos"'
                return response