

$(document).ready(function() {
  // Função para fazer uma requisição AJAX para a página especificada
  function carregarPagina(url) {
      $.ajax({
          url: url,
          method: "GET",
          success: function(response) {
              $("#bookList").html(response); // Atualiza a lista de livros com os resultados da página
          },
          error: function(xhr, status, error) {
              console.error(xhr.responseText); // Trata erros, se houver
          }
      });
  }

  // Manipulador de eventos para os links de paginação
  $("#bookList").on("click", "a", function(event) {
      event.preventDefault(); // Evita o comportamento padrão de clique no link
      var path = "/livro/search/"; // Obtém o caminho da URL atual
      var href = $(this).attr("href"); // Obtém a URL do link clicado
      var url = window.location.origin + path + href; // Monta a URL completa
      carregarPagina(url); // Carrega a página via AJAX
  });

  // Manipulador de eventos para o formulário de busca
  $("#searchForm").submit(function(event) {
      event.preventDefault(); // Evita o comportamento padrão de envio do formulário

      var formData = $(this).serialize(); // Serializa os dados do formulário

      // Faz uma requisição AJAX para buscar os livros
      $.ajax({
          url: $(this).attr("action"), // Obtém a URL do atributo "action" do formulário
          method: "GET",
          data: formData,
          success: function(response) {
              $("#bookList").html(response); // Atualiza a lista de livros com os resultados da busca
          },
          error: function(xhr, status, error) {
              console.error(xhr.responseText); // Trata erros, se houver
          }
      });
  });
});

/*  $(document).ready(function() {
    $("#searchForm").submit(function(event) {
      event.preventDefault(); // Evita o comportamento padrão de envio do formulário

      var formData = $(this).serialize(); // Serializa os dados do formulário

      // Faz uma requisição AJAX para buscar os livros
      $.ajax({
        url: $(this).attr("action"), // Obtém a URL do atributo "action" do formulário
        method: "GET",
        data: formData,
        success: function(response) {
          $("#bookList").html(response); // Atualiza a lista de livros com os resultados da busca
        },
        error: function(xhr, status, error) {
          console.error(xhr.responseText); // Trata erros, se houver
        }
      });
    });
  });
*/