'use strict';

// The page starts as complete HTML. This script only enhances the optional scene.
(() => {
  const scene = document.querySelector('.scene');
  const controls = document.querySelector('.scene-controls');
  const buttons = [...document.querySelectorAll('[data-room][aria-pressed]')];
  const motionButton = document.querySelector('.motion-toggle');
  const status = document.querySelector('#scene-status');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const rooms = {
    observatory: { index: '01', title: 'The Observatory', description: 'Look a little longer. Patterns emerge when you let your eyes settle.' },
    archive: { index: '02', title: 'The Archive', description: 'Collect the overlooked. A different arrangement can tell a different story.' },
    garden: { index: '03', title: 'The Garden', description: 'Repeat, then vary. Small changes create a landscape of possibilities.' }
  };
  let motionEnabled = false;
  let sceneVisible = true;

  function selectRoom(id) {
    const room = rooms[id];
    if (!room) return;
    scene.dataset.room = id;
    document.querySelector('#room-index').textContent = `Room ${room.index}`;
    document.querySelector('#room-title').textContent = room.title;
    document.querySelector('#room-description').textContent = room.description;
    const link = document.querySelector('#room-link');
    link.href = `#${id}`;
    link.setAttribute('aria-label', `Read ${room.title.toLowerCase()} field note`);
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.room === id)));
    // Keep focus on the selected button, announce only the new destination.
    status.textContent = `${room.title} selected. Its field note is available below.`;
  }

  function updateMotion() {
    const allowed = motionEnabled && !reducedMotion.matches;
    scene.classList.toggle('is-moving', allowed);
    scene.classList.toggle('is-paused', document.hidden || !sceneVisible);
    motionButton.setAttribute('aria-pressed', String(allowed));
    motionButton.disabled = reducedMotion.matches;
    motionButton.textContent = reducedMotion.matches ? 'Motion off: reduced-motion preference' : allowed ? 'Turn motion off' : 'Turn motion on';
  }

  buttons.forEach(button => button.addEventListener('click', () => selectRoom(button.dataset.room)));
  motionButton.addEventListener('click', () => { motionEnabled = !motionEnabled; updateMotion(); });
  reducedMotion.addEventListener('change', () => {
    // Turning the preference back off does not silently restart a previous animation.
    motionEnabled = false;
    updateMotion();
  });
  document.addEventListener('visibilitychange', updateMotion);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      sceneVisible = entries[0].isIntersecting;
      updateMotion();
    }).observe(scene);
  }
  updateMotion();
  controls.hidden = false;
})();
