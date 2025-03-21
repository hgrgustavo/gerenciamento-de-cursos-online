class Ajax {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  getCSRFToken() {
    const token = document.querySelector("[name=csrfmiddlewaretoken]") ||
      document.querySelector('meta[name="csrf-token"]');
    return token ? token.getAttribute('content') || token.value : '';
  }

  deleteItem(itemId, itemName) {
    if (confirm("Tem certeza que deseja excluir este item?")) {
      fetch(`${this.baseUrl}/${itemId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": this.getCSRFToken(),
        }
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            document.getElementById(`${itemName}-${itemId}`).remove();
            alert("Item excluído com sucesso!");
          } else {
            alert("Erro ao excluir o item!");
          }
        })
        .catch(error => {
          console.error("Erro na requisição: ", error);
          alert("Ocorreu um erro ao tentar excluir o item.");
        });
    }
  }
}

// Exemplo de uso:
const ajax = new Ajax("excluir");

