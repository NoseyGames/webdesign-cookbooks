"use strict";

(() => {
  const controls = document.querySelector("[data-code-controls]");
  const buttons = [...document.querySelectorAll("[data-language]")];
  const samples = [...document.querySelectorAll("[data-sample]")];
  const copyButton = document.querySelector("[data-copy]");
  const status = document.querySelector("[data-copy-status]");
  if (!controls || buttons.length !== 2 || samples.length !== 2 || !copyButton || !status) return;

  let currentLanguage = "python";
  let copying = false;
  const names = { python: "Python", javascript: "JavaScript" };

  function selectLanguage(language, announce = true) {
    if (copying || !Object.hasOwn(names, language)) return;
    currentLanguage = language;
    buttons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.language === language));
    });
    samples.forEach((sample) => {
      sample.hidden = sample.dataset.sample !== language;
    });
    status.textContent = announce ? `${names[language]} example selected.` : "";
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => selectLanguage(button.dataset.language));
  });

  copyButton.addEventListener("click", async () => {
    if (copying) return;
    const sample = samples.find((item) => item.dataset.sample === currentLanguage);
    const code = sample?.querySelector("code");
    if (!code) return;

    // Insecure contexts and browser permissions may prevent clipboard access.
    // Keep text selectable rather than silently claiming a copy succeeded.
    if (!navigator.clipboard?.writeText) {
      status.textContent = "Clipboard unavailable. Select the code and copy it manually.";
      return;
    }

    copying = true;
    // Keep the invoking button focusable while the promise is pending.
    copyButton.setAttribute("aria-disabled", "true");
    buttons.forEach((button) => { button.disabled = true; });
    copyButton.textContent = "Copying…";
    status.textContent = "Copying the selected example…";
    try {
      await navigator.clipboard.writeText(code.textContent);
      status.textContent = `${names[currentLanguage]} code copied.`;
    } catch {
      status.textContent = "Copy was blocked. Select the code and copy it manually.";
    } finally {
      copying = false;
      copyButton.removeAttribute("aria-disabled");
      buttons.forEach((button) => { button.disabled = false; });
      copyButton.textContent = "Copy code";
    }
  });

  // Reveal only after handlers exist; baseline HTML includes both samples.
  selectLanguage(currentLanguage, false);
  controls.hidden = false;
})();
