  // Manipulador de evento para o botão "Cadastrar"
  $("#cadastrar").click(function() {
    var url = window.location.origin + "/livro/valida_cadastro_livro/";
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    enviarRequisicao(url, "POST", csrftoken);
});

// Manipulador de evento para o botão "Editar"
$("#submitEdit").click(function() {
    var url = window.location.origin + "/livro/valida_edicao_livro/";
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    enviarRequisicao(url, "POST", csrftoken);
});

// Manipulador de evento para o botão "Deletar"
$("#botaoDeletar").click(function() {
    var url = window.location.origin + "/livro/valida_exclusao_livro/";
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    enviarRequisicao(url, "POST", csrftoken);
    // Limpa os campos do formulário
    document.getElementById("id").value = id;
    document.getElementById("titulo").value = "";
    document.getElementById("autor").value = "";
    document.getElementById("genero").value = "";

    // Esconde os botões "enviar edição" e "cancelar edição"
    document.getElementById("id").style.display = "none";
    document.getElementById("cadastrar").style.display = "block";
    document.getElementById("submitEdit").style.display = "none";
    document.getElementById("cancelEdit").style.display = "none";
    document.getElementById("botaoDeletar").style.display = "none";
});

// Função para enviar a requisição Ajax com um método específico
function enviarRequisicao(url, metodo, csrftoken) {
    $.ajax({
        url: url,
        type: metodo,
        data: $("#crudForm").serialize(), // Serializa os dados do formulário
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin', // Do not send CSRF token to another domain.
        success: function(response) {
            // Manipule a resposta, se necessário
            console.log(response);
        },
        error: function(xhr, status, error) {
            // Trate erros, se houver
            console.error(xhr.responseText);
        }
    });
}









/*document.addEventListener("DOMContentLoaded", function() {
    // Manipulador de evento para o botão "Cadastrar"
    document.getElementById("cadastrar").addEventListener("click", function() {
        enviarFormulario("valida_cadastro_livro", "POST");
    });

    // Manipulador de evento para o botão "Editar"
    document.getElementById("submitEdit").addEventListener("click", function() {
        enviarFormulario("valida_edicao_livro/", "PUT");
    });

    // Manipulador de evento para o botão "Deletar"
    document.getElementById("botaoDeletar").addEventListener("click", function() {
        enviarFormulario("valida_exclusao_livro/", "DELETE");
    });
});

// Função para enviar o formulário para uma URL com um método específico
function enviarFormulario(url, metodo) {
    var form = document.getElementById("crudForm");
    form.action = url; // Define a ação do formulário
    form.method = metodo; // Define o método do formulário
    form.submit(); // Submete o formulário
}
*/