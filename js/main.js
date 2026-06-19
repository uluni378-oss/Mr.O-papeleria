const WHATSAPP_NUMBER = "527471013037";
document.documentElement.classList.add("js");
const WHATSAPP_MESSAGE = "Hola, quiero información sobre los servicios de Mr.O Papelería.";

const menuToggle = document.querySelector("[data-menu-toggle]");
const mobilePanel = document.querySelector("[data-mobile-panel]");
const navLinks = document.querySelectorAll("[data-nav-link]");
const revealItems = document.querySelectorAll(".reveal");
const currentYearItems = document.querySelectorAll("[data-current-year]");
const whatsappLinks = document.querySelectorAll("[data-whatsapp]");
const quoteLinks = document.querySelectorAll("[data-whatsapp-quote]");
const images = document.querySelectorAll("img");
const sections = Array.from(document.querySelectorAll("main section[id], footer[id]"));
const webCards = document.querySelectorAll(".web-gallery-card");

const whatsappUrl = (message = WHATSAPP_MESSAGE) =>
  `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;

whatsappLinks.forEach((link) => {
  link.href = whatsappUrl(link.dataset.message || WHATSAPP_MESSAGE);
});

quoteLinks.forEach((link) => {
  const message = link.href.includes("p%C3%A1ginas") || link.textContent.toLowerCase().includes("planes")
    ? "Hola, quiero cotizar una página web"
    : "Hola, quiero cotizar diseño para mi negocio";
  link.href = whatsappUrl(message);
});

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
    { threshold: 0.12, rootMargin: "0px 0px -28px 0px" }
  );

  revealItems.forEach((item, index) => {
    item.style.setProperty("--reveal-delay", `${Math.min(index % 4, 3) * 35}ms`);
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
    { threshold: 0.35 }
  );

  sections.forEach((section) => navObserver.observe(section));

  const webCardsObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.18 }
  );

  webCards.forEach((card) => {
    webCardsObserver.observe(card);
  });
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
  webCards.forEach((card) => card.classList.add("is-visible"));
}

currentYearItems.forEach((item) => {
  item.textContent = new Date().getFullYear();
});

// Sticky Header Logic
const siteHeader = document.querySelector(".site-header");
window.addEventListener("scroll", () => {
  if (window.scrollY > 10) {
    siteHeader?.classList.add("is-scrolled");
  } else {
    siteHeader?.classList.remove("is-scrolled");
  }
}, { passive: true });

// Lgica de filtrado de productos
document.addEventListener('DOMContentLoaded', () => {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.product-card');

  if (filterBtns.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Remover clase activa de todos
        filterBtns.forEach(b => b.classList.remove('active'));
        // Aadir clase activa al presionado
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-filter');

        productCards.forEach(card => {
          if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
            card.classList.remove('is-hidden');
          } else {
            card.classList.add('is-hidden');
          }
        });
      });
    });
  }
});
