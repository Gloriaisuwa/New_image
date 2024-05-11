document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('uploadForm');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const resultSection = document.getElementById('result');
    const compressedImage = document.getElementById('compressedImage');
    const downloadLink = document.getElementById('downloadLink');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);
        loadingIndicator.style.display = 'block';
        fetch('/compress', {
            method: 'POST',
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {
            loadingIndicator.style.display = 'none';
            resultSection.style.display = 'block';
            compressedImage.src = URL.createObjectURL(blob);
            downloadLink.href = URL.createObjectURL(blob);
        })
        .catch(error => {
            console.error('Error:', error);
            loadingIndicator.style.display = 'none';
        });
    });
});
