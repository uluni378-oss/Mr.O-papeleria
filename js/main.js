const menuButton = document.querySelector("[data-menu-button]");
const menuPanel = document.querySelector("[data-menu-panel]");
const menuOverlay = document.querySelector("[data-menu-overlay]");
const navLinks = document.querySelectorAll("[data-nav-link]");
const faqButtons = document.querySelectorAll(".faq-question");
const revealItems = document.querySelectorAll(".reveal");
const whatsappForm = document.querySelector("[data-whatsapp-form]");
const currentYearItems = document.querySelectorAll("[data-current-year]");

const setMenuState = (isOpen) => {
  if (!menuButton || !menuPanel || !menuOverlay) return;
  menuButton.classList.toggle("is-open", isOpen);
  menuPanel.classList.toggle("is-open", isOpen);
  menuOverlay.classList.toggle("is-open", isOpen);
  menuButton.setAttribute("aria-expanded", String(isOpen));
  menuButton.setAttribute("aria-label", isOpen ? "Cerrar menú de navegación" : "Abrir menú de navegación");
};

menuButton?.addEventListener("click", () => {
  const isOpen = !menuPanel?.classList.contains("is-open");
  setMenuState(isOpen);
});

menuOverlay?.addEventListener("click", () => setMenuState(false));

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    setMenuState(false);
  }
});

navLinks.forEach((link) => {
  link.addEventListener("click", () => setMenuState(false));
});

const currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
navLinks.forEach((link) => {
  const linkPath = new URL(link.getAttribute("href"), window.location.href).pathname.replace(/\/index\.html$/, "/");
  if (currentPath === linkPath || currentPath.endsWith(link.dataset.route || "no-match")) {
    link.classList.add("is-active");
    link.setAttribute("aria-current", "page");
  }
});

faqButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const item = button.closest(".faq-item");
    const answer = item?.querySelector(".faq-answer");
    const isOpen = item?.classList.toggle("is-open");
    button.setAttribute("aria-expanded", String(isOpen));
    if (answer) {
      answer.style.maxHeight = isOpen ? `${answer.scrollHeight}px` : "0px";
    }
  });
});

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries, entryObserver) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          entryObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -28px 0px" }
  );
  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

whatsappForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(whatsappForm);
  const nombre = String(formData.get("nombre") || "").trim();
  const telefono = String(formData.get("telefono") || "").trim();
  const servicio = String(formData.get("servicio") || "").trim();
  const mensaje = String(formData.get("mensaje") || "").trim();
  const text = `Hola, soy ${nombre}. Me interesa el servicio de ${servicio}. Mi teléfono es ${telefono}. Mensaje: ${mensaje}.`;
  window.open(`https://wa.me/527471013037?text=${encodeURIComponent(text)}`, "_blank", "noopener");
});

currentYearItems.forEach((item) => {
  item.textContent = new Date().getFullYear();
});
