document.addEventListener("DOMContentLoaded", function() {
    var editButtons = document.querySelectorAll(".editButton");
    editButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var row = this.parentElement.parentElement; // Obtém a linha da tabela
            var cells = row.querySelectorAll("td"); // Obtém todas as células da linha

            // Extrai os detalhes do livro das células
            var title = cells[0].textContent;
            var author = cells[1].textContent;
            var gender = cells[2].textContent;

            // Atualiza os campos do formulário com os detalhes do livro
            document.getElementById("titulo").value = title;
            document.getElementById("autor").value = author;
            document.getElementById("genero").value = gender;

            // Mostra os botões "enviar edição" e "cancelar edição"
            document.getElementById("submitEdit").style.display = "block";
            document.getElementById("cancelEdit").style.display = "block";
        });
    });

    // Adiciona um ouvinte de evento para o botão "cancelar edição"
    document.getElementById("cancelEdit").addEventListener("click", function() {
        // Limpa os campos do formulário
        document.getElementById("titulo").value = "";
        document.getElementById("autor").value = "";
        document.getElementById("genero").value = "";

        // Esconde os botões "enviar edição" e "cancelar edição"
        document.getElementById("submitEdit").style.display = "none";
        document.getElementById("cancelEdit").style.display = "none";
    });
});