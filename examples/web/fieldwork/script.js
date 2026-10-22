'use strict';

// Navigation remains visible until this enhancement has successfully initialized.
const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const narrow = window.matchMedia('(max-width: 42rem)');

function setMenu(open, returnFocus = false) {
  navigation.hidden = narrow.matches && !open;
  toggle.setAttribute('aria-expanded', String(narrow.matches && open));
  toggle.querySelector('span').textContent = open ? '−' : '+';
  if (returnFocus) toggle.focus();
}

function syncNavigation() {
  // Avoid leaving keyboard focus inside navigation that becomes hidden on resize.
  const focusWasInNav = navigation.contains(document.activeElement);
  const focusWasOnToggle = document.activeElement === toggle;
  toggle.hidden = !narrow.matches;
  setMenu(false, narrow.matches && focusWasInNav);
  if (!narrow.matches && focusWasOnToggle) navigation.querySelector('a').focus();
}

toggle.addEventListener('click', () => {
  setMenu(toggle.getAttribute('aria-expanded') !== 'true');
});
navigation.addEventListener('click', (event) => {
  if (narrow.matches && event.target.closest('a')) {
    // Let the anchor move to its destination; do not leave focus in a hidden nav.
    const anchor = event.target.closest('a');
    const target = document.querySelector(anchor.getAttribute('href'));
    setMenu(false);
    if (target) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
      target.addEventListener('blur', () => target.removeAttribute('tabindex'), { once: true });
    }
  }
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && narrow.matches && toggle.getAttribute('aria-expanded') === 'true') {
    setMenu(false, true);
  }
});
narrow.addEventListener('change', syncNavigation);
syncNavigation();

// With no JavaScript, all projects remain visible and native details still work.
const workTools = document.querySelector('.work-tools');
const filters = [...document.querySelectorAll('[data-filter]')];
const projects = [...document.querySelectorAll('[data-category]')];
const resultCount = document.querySelector('.result-count');
const projectGrid = document.querySelector('.project-grid');

filters.forEach((button) => {
  button.addEventListener('click', () => {
    const category = button.dataset.filter;
    projectGrid.dataset.filtered = String(category !== 'all');
    filters.forEach((filter) => filter.setAttribute('aria-pressed', String(filter === button)));
    let visible = 0;
    projects.forEach((project) => {
      const matches = category === 'all' || project.dataset.category.split(' ').includes(category);
      project.hidden = !matches;
      if (matches) visible += 1;
    });
    resultCount.textContent = category === 'all'
      ? `Showing all ${visible} projects`
      : `Showing ${visible} ${category} project${visible === 1 ? '' : 's'}`;
  });
});
workTools.hidden = false;
