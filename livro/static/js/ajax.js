

  $(document).ready(function() {
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