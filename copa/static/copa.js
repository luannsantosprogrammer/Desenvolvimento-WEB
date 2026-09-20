$(document).ready(function(){
    $('input').focus();
    $(".conteiner-alert").hide('slow');
    
    // ============================
    // Função que envia mensagem para qualquer evento do formulário de login
    // ============================
    var respostaDados = (mensagem) => {
      $(".conteiner-alert").show('slow');
      $(".conteiner-alert>h2").eq(1).slideDown("slow").text(mensagem);
      $(".conteiner-alert>h2").eq(0).slideUp("slow");
    };
  
    // aqui cancelará a função de de messagem
    var cancelar = () => {
      $(".conteiner-alert").hide();
    };
    // ================================
  
  
    // ============================
    // carrega o banco de dados de login dos colaboradores
    // ============================
  
  
    const todasSenhas = () => {
      let passwords = []
      let link = "https://script.google.com/macros/s/AKfycbwfENfM6Q60P0JPM3o4saMNu9ddSh9LXIJf7ESVLyzi61Kz7JjCyLxgcrQ_uebvuo-M/exec"
      let retornPasswords = fetch(link)
      .then(resposta => resposta.json())
      .then((data)=>{
        passwords = data
      }).then(aviso => alert("Cadastros atualizados"))
      let nome = null; // variável acessível fora do keyup

      // --- Evento de digitação ---
      $(".input").off("keyup").on("keyup", (e) => {

        if (e.key === "Enter") return; // deixa o outro handler cuidar disso

        try {
          const filtrandoNome = passwords.filter(valores =>
          valores[2] == $(".input").val()
          );

          nome = filtrandoNome[0][1]; 
          respostaDados(nome);
        } catch {
          nome = null;
          cancelar();
        }
        });
  
  
        $(document).off("keyup").on("keyup", (e) => {
          if (e.key !== "Enter") return;
  
          if (!$(".input").val() || !nome) {
            respostaDados("Essa senha não existe. Tente novamente");
            return;
          }
  
  
          $(".conteiner-alert>h2").eq(1).text("Aguarde...");
  

            fetch("/envio",{

              method: "POST",
              headers:{
               "Content-Type": "application/json",
                      },
              body: JSON.stringify({"nome":nome})

            }).then((data)=>{
              $(".conteiner-alert>h2").eq(1).text("Enviado com sucesso");
              $(".input").val("");
              setTimeout(cancelar, 2000);
            }).catch((data)=>{
              $(".conteiner-alert>h2").eq(1).text("Ocorreu um erro, clique em cancelar e tente novamente");
              setTimeout(cancelar, 2000);
          
            })


        });
  
 
  };
  
  
    todasSenhas();
  
  

  
  }); 
  