const menuToggle = document.querySelector("[data-menu-toggle]");
const mobilePanel = document.querySelector("[data-mobile-panel]");
const navLinks = document.querySelectorAll("[data-nav-link]");
const revealItems = document.querySelectorAll(".reveal");
const currentYearItems = document.querySelectorAll("[data-current-year]");
const images = document.querySelectorAll("img");
const sections = Array.from(document.querySelectorAll("main section[id]"));

const setMenu = (isOpen) => {
  if (!menuToggle || !mobilePanel) return;
  menuToggle.classList.toggle("is-open", isOpen);
  mobilePanel.classList.toggle("is-open", isOpen);
  document.body.classList.toggle("menu-open", isOpen);
  menuToggle.setAttribute("aria-expanded", String(isOpen));
  menuToggle.setAttribute("aria-label", isOpen ? "Cerrar menú" : "Abrir menú");
};

menuToggle?.addEventListener("click", () => {
  setMenu(!mobilePanel?.classList.contains("is-open"));
});

navLinks.forEach((link) => {
  link.addEventListener("click", () => setMenu(false));
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") setMenu(false);
});

images.forEach((image) => {
  image.addEventListener("error", () => {
    const fallback = image.dataset.fallback;
    if (fallback && !image.src.endsWith(fallback)) {
      image.src = fallback;
      image.removeAttribute("srcset");
      return;
    }
    image.style.visibility = "hidden";
  });
});

if ("IntersectionObserver" in window) {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -24px 0px" }
  );

  revealItems.forEach((item, index) => {
    item.style.setProperty("--reveal-delay", `${Math.min(index % 3, 2) * 30}ms`);
    revealObserver.observe(item);
  });

  const navObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.getAttribute("id");
        navLinks.forEach((link) => {
          const isActive = link.getAttribute("href") === `#${id}`;
          link.classList.toggle("is-active", isActive);
          if (isActive) {
            link.setAttribute("aria-current", "page");
          } else {
            link.removeAttribute("aria-current");
          }
        });
      });
    },
    { threshold: 0.42 }
  );

  sections.forEach((section) => navObserver.observe(section));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

currentYearItems.forEach((item) => {
  item.textContent = new Date().getFullYear();
});
