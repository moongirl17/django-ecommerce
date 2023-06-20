const userMenuButton = document.getElementById("user-menu-button");
const userMenu = document.getElementById("user-menu");

userMenuButton.addEventListener("click", function() {
  const expanded = userMenuButton.getAttribute("aria-expanded");
  if (expanded === "false") {
    userMenuButton.setAttribute("aria-expanded", "true");
    userMenu.classList.remove("scale-0", "opacity-0");
    userMenu.classList.add("scale-100", "opacity-100");
  } else {
    userMenuButton.setAttribute("aria-expanded", "false");
    userMenu.classList.remove("scale-100", "opacity-100");
    userMenu.classList.add("scale-0", "opacity-0");
  }
});

$(document).ready(function() {
  $('.dropdown-toggle').click(function() {
    var dropdownMenu = $(this).next('.dropdown-menu');
    if (dropdownMenu.hasClass('open')) {
      dropdownMenu.removeClass('open');
      dropdownMenu.addClass('close');
    } else {
      dropdownMenu.removeClass('close');
      dropdownMenu.addClass('open');
    }
  });
});