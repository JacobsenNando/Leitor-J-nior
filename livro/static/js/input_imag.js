const imageInput = document.getElementById('imageInput');
    const preview = document.getElementById('preview');

    imageInput.addEventListener('change', function() {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          const img = new Image();
          img.src = e.target.result;
          img.onload = function() {
            preview.innerHTML = '';
            preview.appendChild(img);
          }
        }
       console.log(file);
        reader.readAsDataURL(file);
      } else {
        preview.innerHTML = 'Nenhuma imagem selecionada';
      }
    });