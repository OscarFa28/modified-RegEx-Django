function compressFile(compress) {
    const fileInput = document.getElementById('fileInput');
    const fileNameInput = document.getElementById('file-name');
    
    if (fileInput.files.length === 0) {
        alert('Please select a file!');
        return;
    }

    if (!fileNameInput.value) {
        alert('Please select a name');
        return;
    }
    
    const file = fileInput.files[0];
    const fileName = fileNameInput.value || 'compressed_file';
    const compressB = compress;

    const formData = new FormData();
    formData.append('file', file);
    formData.append('file-name', fileName);
    formData.append('compress', compressB);

    var url = "/compress_file/";
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formData
    })
    .then(response => {
        if (response.ok) {
            // Handle successful response, initiate file download
            response.blob().then(blob => {
                const fileName = response.headers.get('Content-Disposition').split('filename=')[1];
                const downloadUrl = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = downloadUrl;
                a.download = fileName.trim().replace(/"/g, ''); // Eliminar comillas en el nombre de archivo
                document.body.appendChild(a);
                a.click();
                a.remove();
                window.URL.revokeObjectURL(downloadUrl);
                console.log('File compressed successfully!');
            });
        } else {
            alert(`Error: no se ingresó un archivo válido`);
            
            
        }
    })
    .catch(error => {
        console.error('Error:', error);
        
    });
}