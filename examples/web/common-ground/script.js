"use strict";

(() => {
  const controls = document.querySelector("#work-filters");
  const list = document.querySelector("#work-list");
  const status = document.querySelector("#result-count");
  if (!controls || !list || !status) return;

  const buttons = [...controls.querySelectorAll("button[data-filter]")];
  const projects = [...list.querySelectorAll("[data-disciplines]")].map(element => ({
    element,
    // Token matching supports overlapping categories without substring collisions.
    disciplines: new Set(element.dataset.disciplines.split(/\s+/).filter(Boolean))
  }));
  if (!buttons.length || !projects.length) return;

  const matches = (project, discipline) => discipline === "all" || project.disciplines.has(discipline);

  function selectFilter(selected) {
    const discipline = selected.dataset.filter;
    let count = 0;
    for (const project of projects) {
      const visible = matches(project, discipline);
      project.element.hidden = !visible;
      if (visible) count += 1;
    }
    for (const button of buttons) button.setAttribute("aria-pressed", String(button === selected));
    list.classList.toggle("is-filtered", discipline !== "all");

    // A concise live announcement reports results without moving keyboard focus.
    status.textContent = discipline === "all"
      ? `Showing all ${count} projects.`
      : `Showing ${count} ${discipline} ${count === 1 ? "project" : "projects"}.`;
  }

  for (const button of buttons) {
    const count = button.querySelector("[data-count]");
    if (count) count.textContent = String(projects.filter(project => matches(project, button.dataset.filter)).length);
    button.addEventListener("click", () => selectFilter(button));
  }
  // Native details need no JS, so their open state survives filtering naturally.
  // Reveal only after handlers and count labels are installed; all work stays visible if JS fails.
  selectFilter(buttons.find(button => button.dataset.filter === "all") || buttons[0]);
  controls.hidden = false;
})();
