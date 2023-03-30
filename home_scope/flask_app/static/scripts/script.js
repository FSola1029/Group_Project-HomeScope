// Get the file input element and the image preview element
const inputFile = document.getElementById('image-file');
const imagePreview = document.getElementById('image-preview');

// Add an event listener to the file input element
inputFile.addEventListener('change', function(event) {
    // Get the selected file
    const file = event.target.files[0];
    
    // Create a FileReader object
    const reader = new FileReader();
    
    // Set the onload event handler for the FileReader object
    reader.onload = function(event) {
        // Set the src attribute of the image preview element
        imagePreview.src = event.target.result;
    };
    
    // Read the selected file as a data URL
    reader.readAsDataURL(file);
});





