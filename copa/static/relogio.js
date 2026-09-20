$(document).ready(function(){

    //================================================ 
    // essa é a div onde os relógios serão adicionados
    // ===============================================

    const $conteinerRelogio = $(".conteiner-relogio")
    const $audio = $("#alarme");

    // ==============================================

    //================================================ 
    // essa é a div onde os relógios serão adicionados
    // ===============================================
    function vibrarRelogio(div){
        div.css('position', 'relative'); //deixa o conteiner livre para movimentar 
        div.css("animation", "pulse 1s infinite");


    }

  // ==============================================
  // nessa função terá a lógica para que o relógio funcione
  // ==============================================
  async function contator(nome,div){
    // variavel que irá percorrer pelo código 
    var valorIniciar = "00:10:00";

    // essa função irá pegar o valor inicial e transformar em segundos
    async function converterEmSegundos(valor){
      let stringSeparado = valor.split(":") //separando o texto para poder fazer o calculo
      let emSegundos = parseInt(stringSeparado[1]) *60 + parseInt(stringSeparado[2]) // transformando em segundos
      valorIniciar =  emSegundos; //agora o valor inicial será em segundos
    }
    
    // essa função transformará segundos em string para ser exibida na tela
    async function converterString(valor){
        let minuto = String(parseInt(valor/60)).padStart(2,0); //formatado para ter dois caracteres
        let segundo = String(valor % 60).padStart(2,0);
        
        valorIniciar = `00:${minuto}:${segundo}` //agora valorInicial será uma string
    }

    // esse processo assincro será utilizado para a contagem regressiva
    let converter = setInterval(()=>{
        // transformar em segundos
        converterEmSegundos(valorIniciar)
        // diminuir
        valorIniciar --
        if(valorIniciar <= -1){
          clearInterval(converter)
          div.css("background", "red");
          vibrarRelogio(div)
          fetch("/bipe",{
  
            method: "POST",
            headers:{
            "Content-Type": "application/json",
                    },
            body: JSON.stringify({"bipe":"bipe"})
        
          }).then(data => data)
        }else{
        
        // mostrar tempo atual
        converterString(valorIniciar)
        if(valorIniciar == "00:01:00"){
          div.css("background", "yellow");
        }
          // mostrar tempo atual
        div.find(".numeros").last().text(valorIniciar)
        
        }

    },1000)

  }

async function addPainel(cola){
  // criar div relogio
  let $relogio = $("<div>").addClass("relogio");

  let $h2Nome = $("<h2>").addClass("nome-Titulo").text(cola);
  let $h2Numeros = $("<h2>").addClass("numeros").text("00:10:00");

  $relogio.append($h2Nome, $h2Numeros);
  $conteinerRelogio.append($relogio);

  contator(cola, $relogio);
}


function reset(){
  fetch("/envio",{
  
    method: "POST",
    headers:{
    "Content-Type": "application/json",
            },
    body: JSON.stringify({"nome":""})

  }).then(data => data)
}

setInterval(() => {


  fetch("/recebendo").then(data => data.json()).then((d)=>{


  if(d['nome'] != ""){
      let $nome = $("h2.nome-Titulo")
      .filter(function() {
          return $(this).text().trim() === d['nome'].trim();
      })
      .closest(".relogio") 


      if ($nome.length > 0) {
        // Se encontrou, remove
        $nome.remove();
        reset()
      } else {
          // Se não encontrou, adiciona
          addPainel(d['nome']);
          reset()
      }


  }


  } );
  

}, 1000);

  

        


})       