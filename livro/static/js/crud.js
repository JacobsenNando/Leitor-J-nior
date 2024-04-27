document.addEventListener("DOMContentLoaded", function() {
    // Manipulador de evento para o botão "Cadastrar"
    document.getElementById("cadastrar").addEventListener("click", function() {
        enviarRequisicao("/valida_cadastro_livro/", "POST");
    });

    // Manipulador de evento para o botão "Editar"
    document.getElementById("submitEdit").addEventListener("click", function() {
        enviarRequisicao("URL_para_Editar", "PUT");
    });

    // Manipulador de evento para o botão "Deletar"
    document.getElementById("botaoDeletar").addEventListener("click", function() {
        enviarRequisicao("URL_para_Deletar", "DELETE");
    });
});

// Função para enviar uma requisição Ajax com um método específico
function enviarRequisicao(url, metodo) {
    var xhr = new XMLHttpRequest(); // Cria um objeto XMLHttpRequest

    // Configura a requisição Ajax
    xhr.open(metodo, url);

    // Obtém o token CSRF do cookie
    var csrftoken = getCookie('csrftoken');

    // Define o cabeçalho da requisição com o token CSRF
    xhr.setRequestHeader('X-CSRFToken', csrftoken);

    // Define o manipulador de eventos para quando a requisição for concluída
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            // Requisição bem-sucedida
            // Faça algo com a resposta, se necessário
            console.log(xhr.responseText);
        } else {
            // Requisição falhou
            console.error('Erro ao enviar requisição:', xhr.statusText);
        }
    };

    // Define o manipulador de eventos para quando houver um erro na requisição
    xhr.onerror = function() {
        console.error('Erro de conexão');
    };

    // Envia a requisição Ajax
    xhr.send();
}

// Função auxiliar para obter o valor do token CSRF do cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Verifica se o cookie corresponde ao nome do token CSRF
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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