const form = document.querySelector("form");
const email = document.querySelector("#email");
const senha = document.querySelector("#senha");
const button = document.querySelector(".btn2");
const alertContent = document.querySelector(".alert-content");

form.addEventListener("submit", (e) => {
  if (!checkInputs()) {
    e.preventDefault();
  }
});

function checkInputs() {
  const emailValue = email.value;
  const senhaValue = senha.value;

  

  if (emailValue === "") {
    setErrorFor(email, "O email é obrigatório.");
  } else if (!checkEmail(emailValue)) {
    setErrorFor(email, "Por favor, insira um email válido.");
  } else {
    setSuccessFor(email);
  }

  if (senhaValue === "") {
    setErrorFor(senha, "A senha é obrigatória.");
  } else if (senhaValue.length < 8) {
    setErrorFor(senha, "A senha deve ter no mínimo 8 caracteres.");
  } else {
    setSuccessFor(senha);
  }

  const formControls = form.querySelectorAll(".form-control");

  const formIsValid = [...formControls].every((formControl) => {
    return formControl.className === "form-control success";
  });

  if (formIsValid) {
    console.log("O formulário está 100% válido!");

    //resetForm();
    showSuccessMessage();
    setTimeout(() => {
      form.submit()
    }, 2000);
  }
}
function resetForm() {
 
  email.value = "";
  senha.value = "";

  form.querySelectorAll(".form-control.success").forEach((formControl) => {
    formControl.classList.remove("success");
  });
}

function showSuccessMessage() {
  alertContent.style.display = "block";

  // Esconde o alerta após 4 segundos
  setTimeout(() => {
    alertContent.style.display = "none";
  }, 2000);
}
function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const small = formControl.querySelector("small");

  small.innerText = message;

  formControl.className = "form-control error";
}

function setSuccessFor(input) {
  const formControl = input.parentElement;

  formControl.className = "form-control success";
}

function checkEmail(email) {
  return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
    email
  );
}
