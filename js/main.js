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


// Intersection Observer for Animations
document.addEventListener('DOMContentLoaded', () => {
  const animatedElements = document.querySelectorAll('.quick-service-card, .category-card, .school-season-copy, .school-season-list, .identity-card, .web-gallery-card, .location-inner > div');

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        });
      },
      { threshold: 0.1 }
    );

    animatedElements.forEach((el) => {
      observer.observe(el);
    });
  } else {
    animatedElements.forEach((el) => {
      el.classList.add("is-visible");
    });
  }
});


// Fallback for missing images
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('img[data-fallback]').forEach(img => {
    img.addEventListener('error', function() {
      const fallbackSrc = this.getAttribute('data-fallback');
      if (fallbackSrc && this.src !== fallbackSrc && !this.src.includes(fallbackSrc)) {
        this.src = fallbackSrc;
      }
    });
  });
});


// QUICK SERVICES REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const quickServiceElements = document.querySelectorAll(".quick-reveal");
  if(quickServiceElements.length > 0) {
    const quickServiceObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.15 }
    );

    quickServiceElements.forEach((element, index) => {
      element.style.transitionDelay = `${index * 70}ms`;
      quickServiceObserver.observe(element);
    });
  }
});

// WEB SECTION REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const webRevealElements = document.querySelectorAll(".web-reveal-left, .web-reveal-stagger, .web-reveal-right");
  if(webRevealElements.length > 0) {
    const webRevealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    webRevealElements.forEach(el => webRevealObserver.observe(el));
  }
});


// --- LIGHTBOX OBSERVER AND LOGIC ---
document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("image-lightbox");
  const lightboxImage = document.getElementById("image-lightbox-img");
  const lightboxTitle = document.getElementById("image-lightbox-title");
  const lightboxTriggers = document.querySelectorAll(".web-preview, .business-design-preview");
  const lightboxCloseButtons = document.querySelectorAll("[data-lightbox-close]");

  let lastFocusedElement = null;

  const openLightbox = (trigger) => {
  if (!lightbox || !lightboxImage || !lightboxTitle) return;

  const previewImage = trigger.querySelector("img");

  if (!previewImage) return;

  const imageSource =
    previewImage.currentSrc ||
    previewImage.getAttribute("src");

  const imageAlt =
    previewImage.getAttribute("alt") || "";

  const imageTitle =
    trigger.dataset.lightboxTitle ||
    trigger.querySelector(".web-preview__label")?.textContent?.trim() ||
    "";

  if (!imageSource) return;

  lastFocusedElement = document.activeElement;

  lightboxImage.onload = () => {
    lightbox.classList.remove("has-error");
  };

  lightboxImage.onerror = () => {
    lightbox.classList.add("has-error");
  };

  lightboxImage.src = imageSource;
  lightboxImage.alt = imageAlt;
  lightboxTitle.textContent = imageTitle;

  lightbox.classList.add("is-open");
  lightbox.setAttribute("aria-hidden", "false");
  document.body.classList.add("lightbox-open");

  const closeButton =
    lightbox.querySelector(".image-lightbox__close");

  closeButton?.focus();
};

  const closeLightbox = () => {
  if (!lightbox || !lightboxImage || !lightboxTitle) return;

  lightbox.classList.remove("is-open", "has-error");
  lightbox.setAttribute("aria-hidden", "true");
  document.body.classList.remove("lightbox-open");

  lightboxImage.removeAttribute("src");
  lightboxImage.alt = "";
  lightboxTitle.textContent = "";

  lastFocusedElement?.focus();
};

  lightboxTriggers.forEach((trigger) => {
    trigger.addEventListener("click", () => openLightbox(trigger));
  });

  lightboxCloseButtons.forEach((button) => {
    button.addEventListener("click", closeLightbox);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && lightbox?.classList.contains("is-open")) {
      closeLightbox();
    }
  });
});

// BUSINESS DESIGN REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const businessRevealElements = document.querySelectorAll(".business-design-reveal");
  if(businessRevealElements.length > 0) {
    const businessRevealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    
    businessRevealElements.forEach((el, index) => {
      el.style.transitionDelay = `${index * 80}ms`;
      businessRevealObserver.observe(el);
    });
  }
});

// BUSINESS DESIGN REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const businessRevealElements = document.querySelectorAll(".business-design-reveal");
  if(businessRevealElements.length > 0) {
    const businessRevealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    
    businessRevealElements.forEach((el, index) => {
      el.style.transitionDelay = `${index * 80}ms`;
      businessRevealObserver.observe(el);
    });
  }
});

// CATEGORY CARDS REVEAL OBSERVER
document.addEventListener("DOMContentLoaded", () => {
  const categoryCards = document.querySelectorAll(".category-card-reveal");
  if(categoryCards.length > 0) {
    const categoryObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });

    categoryCards.forEach((card, index) => {
      card.style.transitionDelay = `${index * 65}ms`;
      categoryObserver.observe(card);
    });
  }
});
