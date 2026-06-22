js_path = r'C:\Users\repre\Documents\Mro papeleria\js\main.js'
with open(js_path, 'a', encoding='utf-8') as f:
    f.write('''

// --- LIGHTBOX OBSERVER AND LOGIC ---
document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("image-lightbox");
  const lightboxImage = document.getElementById("image-lightbox-img");
  const lightboxTitle = document.getElementById("image-lightbox-title");
  const lightboxTriggers = document.querySelectorAll(".web-preview");
  const lightboxCloseButtons = document.querySelectorAll("[data-lightbox-close]");

  let lastFocusedElement = null;

  const openLightbox = (trigger) => {
    if (!lightbox || !lightboxImage || !lightboxTitle) return;

    const imageSource = trigger.dataset.lightboxSrc;
    const imageAlt = trigger.dataset.lightboxAlt || "";
    const imageTitle = trigger.dataset.lightboxTitle || "";

    if (!imageSource) return;

    lastFocusedElement = document.activeElement;

    lightboxImage.src = imageSource;
    lightboxImage.alt = imageAlt;
    lightboxTitle.textContent = imageTitle;

    lightbox.classList.add("is-open");
    lightbox.setAttribute("aria-hidden", "false");
    document.body.classList.add("lightbox-open");

    const closeButton = lightbox.querySelector(".image-lightbox__close");
    closeButton?.focus();
  };

  const closeLightbox = () => {
    if (!lightbox) return;

    lightbox.classList.remove("is-open");
    lightbox.setAttribute("aria-hidden", "true");
    document.body.classList.remove("lightbox-open");

    lightboxImage.src = "";
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
''')
print("JS updated successfully.")
