/* ===== ALERTA DE BEM-VINDO ===== */
document.addEventListener('DOMContentLoaded', function() {
  alert('Bem-vindo à nossa página!');
});
/* ===== ALERTA DE BEM-VINDO ===== */


/* ===== DARK MODE ===== */
const body = document.querySelector('body');
const modeToggle = document.querySelector('#moon');

modeToggle.addEventListener('click', () => {
    body.classList.toggle('dark')
})
/* ===== DARK MODE ===== */


/* ===== MENU ===== */
const menuButton = document.getElementById('openBtn');
const closeButton = document.getElementById('closeBtn');
const circle = document.getElementById('circle');
const menu = document.getElementById('menu');
const btns = document.getElementById('btns');

//abre o menu
menuButton.addEventListener('click', () => {
  circle.classList.add('show');
  menu.classList.add('show');
  btns.classList.add('hide');
  menuButton.disabled = true;
});

//fecha o menu
closeButton.addEventListener('click', () => {
  circle.classList.remove('show');
  menu.classList.remove('show');
  btns.classList.remove('hide');
  menuButton.disabled = false;
});
/* ===== MENU ===== */


/* ===== DATA E HORA ===== */
function displayDateTime() {
  var datetimeElement = document.getElementById("datetime");
  var currentDate = new Date();
  var dateOptions = { year: 'numeric', month: 'long', day: 'numeric' };
  var timeOptions = { hour: 'numeric', minute: 'numeric', second: 'numeric' };
  var formattedDate = currentDate.toLocaleDateString(undefined, dateOptions);
  var formattedTime = currentDate.toLocaleTimeString(undefined, timeOptions);
  datetimeElement.innerHTML = formattedTime + ", " + formattedDate;
}

// Atualiza a data e hora a cada segundo
setInterval(displayDateTime, 1000);

// Exibe a data e hora assim que a página é carregada
displayDateTime();
/* ===== FOOTER ===== */


/* ===== Login ===== */
const formOpenBtn = document.querySelector("#form-open"),
home = document.querySelector(".container");
    //faz o pop up aparecer quando aperta em login
formOpenBtn.addEventListener("click", () => home.classList.add("show"))
    //faz o pop up sumir quando aperta fora
document.addEventListener('click', function (event) {
    if (!home.contains(event.target) && event.target !== formOpenBtn) {
        home.classList.remove("show");
    }
});
  
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const sign_in_btn2 = document.querySelector("#sign-in-btn2");
const sign_up_btn2 = document.querySelector("#sign-up-btn2");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

sign_up_btn2.addEventListener("click", () => {
    container.classList.add("sign-up-mode2");
});
sign_in_btn2.addEventListener("click", () => {
    container.classList.remove("sign-up-mode2");
});
/* ===== Login ===== */


/* =====  Validação do login ===== */
document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Evita o envio do formulário

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Validação do usuário e senha
  if (username === 'Admin' && password === '123456') {
    // Redireciona para o site desejado
    window.location.href = 'https://www.unicef.org/brazil/comunicados-de-imprensa/relatorio-da-onu-numeros-globais-de-fome-subiram-para-cerca-de-828-milhoes-em-2021';
  } else {
    // Credenciais inválidas, exibe uma mensagem de erro
    alert('Usuário ou senha inválidos!');
  }
});
/* =====  Validação do login ===== */


/* ===== EFEITO NA PAGINA INICIAL ===== */
const arco = document.getElementById('arco');
const box1 = document.querySelector('.box1');

ScrollTrigger.create({
  trigger: '.section1',
  start: 'top top',
  end: 'bottom',
  pin: true,
  onUpdate: (self) => {
    const progress = self.progress.toFixed(2);

    // Atualiza a escala do arco
    const scale = 1.05 + progress * 2; // Ajuste o valor multiplicador conforme necessário
    gsap.set(arco, { scale: scale });

    // Atualiza as propriedades da box1
    const width = 30 + progress * 28; // Ajuste o valor multiplicador e o valor inicial da largura conforme necessário
    const fontSize = 38 + progress * 5; // Ajuste o valor multiplicador e o valor inicial do tamanho da fonte conforme necessário
    const lineHeight = 1.2 + progress * 0.4; // Ajuste o valor multiplicador e o valor inicial da line-height conforme necessário
    const top = 60 - progress * 10; // Ajuste o valor multiplicador e o valor inicial de top conforme necessário

    gsap.set(box1, {
      width: `${width}rem`,
      top: `${top}%`
    });

    gsap.set(box1.querySelector('h1'), {
      fontSize: `${fontSize}px`,
      lineHeight: lineHeight
    });
  }
});
/* ===== EFEITO NA PAGINA INICIAL ===== */


/* ===== MUDAR O CONTEUDO DOS BENEFICIOS ===== */
const inputs = document.querySelectorAll('input[name="opcao"]');
const labels = document.querySelectorAll('.box5 label');
const box = document.querySelector('.box5');
const img = box.querySelector('img');
const title = box.querySelector('.text h1');
const description = box.querySelector('.text p');

// Adicionar evento de mudança para os inputs
inputs.forEach(input => {
  input.addEventListener('change', () => {
    // Verificar qual input está selecionado
    if (input.checked) {
        labels.forEach(label => {
          if (label.getAttribute('for') === input.id) {
            label.classList.add('selected');
          } else {
            label.classList.remove('selected');
          }
        });
      // Limpar classes ou estilos existentes
      box.className = 'box5';

      // Adicionar classes ou estilos com base na seleção
      switch (input.id) {
        case 'op1':
          img.src = 'img/ben1.jpg';
          title.textContent = 'Redução do desperdício de alimentos';
          description.textContent = 'Ao implementar sistemas de rastreamento inteligente e compartilhamento de informações, podemos identificar pontos de desperdício ao longo da cadeia de suprimentos e tomar medidas para reduzi-lo, evitando perdas desnecessárias.';
          break;
        case 'op2':
          img.src = 'img/ben2.jpg';
          title.textContent = 'Fortalecimento da agricultura';
          description.textContent = 'Ao promover o uso de tecnologias avançadas, como o rastreamento inteligente e as práticas de conservação de alimentos, podemos fortalecer a agricultura, melhorando a eficiência da produção e minimizando as perdas.';
          break;
        case 'op3':
          img.src = 'img/ben3.jpg';
          title.textContent = 'Distribuição equitativa de alimentos';
          description.textContent = 'A plataforma de compartilhamento de informações permite que alimentos excedentes sejam doados ou redistribuídos para áreas onde há escassez, garantindo uma distribuição mais equitativa e ajudando a combater a fome e a insegurança alimentar.';
          break;
        case 'op4':
          img.src = 'img/ben4.jpg';
          title.textContent = 'Sustentabilidade ambiental';
          description.textContent = 'Ao reduzir o desperdício de alimentos, também reduzimos o impacto ambiental associado à produção, transporte e descarte desses alimentos, contribuindo para a sustentabilidade ambiental e a mitigação das mudanças climáticas.';
          break;
        case 'op5':
          img.src = 'img/ben5.jpg';
          title.textContent = 'Otimização da cadeia de suprimentos';
          description.textContent = 'Ao reduzir o desperdício de alimentos, também reduzimos o impacto ambiental associado à produção, transporte e descarte desses alimentos, contribuindo para a sustentabilidade ambiental e a mitigação das mudanças climáticas.';
          break;
        // Adicionar outros cases para cada opção
      }
    }
  });
});
document.addEventListener('DOMContentLoaded', function() {
    const op1 = document.getElementById('op1');
    const labelOp1 = document.querySelector('label[for="op1"]');
    
    op1.checked = true;
    labelOp1.classList.add('selected');
  });
/* ===== MUDAR O CONTEUDO DOS BENEFICIOS ===== */


/* ===== GALERIA ===== */
document.addEventListener("DOMContentLoaded", function() {
  const carrossel = document.querySelector(".carrossel");
  const prevButton = document.querySelector("#prev");
  const nextButton = document.querySelector("#next");
  const images = Array.from(carrossel.children);
  let currentImageIndex = 0;

  // Exibe a imagem atual
  images[currentImageIndex].style.opacity = 1;

  // Função para exibir a próxima imagem
  function showNextImage() {
    images[currentImageIndex].style.opacity = 0;
    currentImageIndex = (currentImageIndex + 1) % images.length;
    images[currentImageIndex].style.opacity = 1;
  }

  // Função para exibir a imagem anterior
  function showPrevImage() {
    images[currentImageIndex].style.opacity = 0;
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    images[currentImageIndex].style.opacity = 1;
  }

  // Evento de clique para o botão "Next"
  nextButton.addEventListener("click", showNextImage);

  // Evento de clique para o botão "Prev"
  prevButton.addEventListener("click", showPrevImage);
});
/* ===== GALERIA ===== */


/* ===== CONTATO ===== */
/* Form contato animação */
const input = document.querySelectorAll('.contact-input')

input.forEach(ipt => {
    ipt.addEventListener('focus', () => {
        ipt.parentNode.classList.add('focus');
        ipt.parentNode.classList.add('not-empty');
    })
    ipt.addEventListener('blur', () => {
        if(ipt.value == ''){
            ipt.parentNode.classList.remove('not-empty');
        }
        ipt.parentNode.classList.remove('focus');
    })
})
/* Form contato animação */

/* ===== CONTATO ===== */