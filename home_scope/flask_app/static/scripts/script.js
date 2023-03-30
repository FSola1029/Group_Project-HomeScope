const fileInput = document.getElementById('file-input');
const fileName = document.getElementById('file-name');

fileInput.addEventListener('change', () => {
    fileName.textContent = fileInput.files[0].name;
});




