// Мобильное меню: после клика по пункту сворачиваем его, а уже потом переходим.
// Если перейти сразу, меню сворачивается после прокрутки, шапка становится ниже,
// и секция уезжает вверх под край экрана.
const menu = document.querySelector(".navbar-collapse");

document.querySelectorAll(".navbar-collapse .nav-link").forEach((link) => {
  link.addEventListener("click", (event) => {
    if (!menu.classList.contains("show")) {
      return;
    }
    event.preventDefault();
    menu.addEventListener(
      "hidden.bs.collapse",
      () => {
        window.location.href = link.href;
      },
      { once: true },
    );
    bootstrap.Collapse.getOrCreateInstance(menu).hide();
  });
});
