
function modalizeImage(img) {
  var modal             = document.getElementById('myModal');
  var modalImg          = document.getElementById('modalImg');
  var closeModal        = document.getElementById('closeModal');

  modal.style.display   = 'block';
  modalImg.src          = img.src;
  captionText.innerHTML = img.alt;
} // img.onclick


function closeModal() {
  var modal             = document.getElementById('myModal');
  modal.style.display   = 'none';
} // closeModal
