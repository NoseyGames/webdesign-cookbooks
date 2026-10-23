(() => {
  'use strict';

  const controls = document.querySelector('#sample-controls');
  const finish = document.querySelector('#finish');
  const addButton = document.querySelector('#add-sample');
  const removeButton = document.querySelector('#remove-last');
  const clearButton = document.querySelector('#clear-bag');
  const actions = document.querySelector('#bag-actions');
  const art = document.querySelector('#hero-art');
  const finishLabel = document.querySelector('#finish-label');
  const price = document.querySelector('#hero-price');
  const title = document.querySelector('#vessel-title');
  const items = document.querySelector('#bag-items');
  const empty = document.querySelector('#bag-empty');
  const quantity = document.querySelector('#bag-quantity');
  const subtotal = document.querySelector('#bag-subtotal');
  const navCount = document.querySelector('#nav-count');
  const status = document.querySelector('#bag-status');
  const required = [controls, finish, addButton, removeButton, clearButton, actions, art, finishLabel, price, title, items, empty, quantity, subtotal, navCount, status];
  if (required.some((element) => !element)) return;

  const currency = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  // Source the product's visible labels and prices from baseline HTML.
  const finishes = new Map(Array.from(finish.options, (option) => [option.value, {
    name: option.dataset.label,
    price: Number(option.dataset.price)
  }]));
  if (Array.from(finishes.values()).some((item) => !item.name || !Number.isFinite(item.price) || item.price < 0)) return;
  const bag = [];

  function selectedFinish() { return finishes.get(finish.value); }

  function updatePreview(announce = false) {
    const selected = selectedFinish();
    if (!selected) return;
    art.dataset.finish = finish.value;
    finishLabel.textContent = selected.name;
    price.textContent = currency.format(selected.price);
    title.textContent = `Orbit vessel in ${selected.name}`;
    if (announce) status.textContent = `Previewing ${selected.name}, ${currency.format(selected.price)}. Existing bag items keep their selected finish.`;
  }

  function renderBag(message) {
    // Group repeated finishes for a readable summary; each addition is retained
    // in the underlying list so Remove last item has a predictable meaning.
    const groups = new Map();
    for (const item of bag) {
      const previous = groups.get(item.name);
      groups.set(item.name, { ...item, quantity: (previous?.quantity || 0) + 1 });
    }
    const rows = Array.from(groups.values(), (item) => {
      const row = document.createElement('li');
      const label = document.createElement('span');
      const amount = document.createElement('span');
      label.textContent = `Orbit · ${item.name} × ${item.quantity}`;
      amount.textContent = currency.format(item.price * item.quantity);
      row.append(label, amount);
      return row;
    });
    items.replaceChildren(...rows);
    empty.hidden = bag.length > 0;
    quantity.textContent = String(bag.length);
    navCount.textContent = String(bag.length);
    navCount.setAttribute('aria-label', `items: ${bag.length}`);
    const total = bag.reduce((sum, item) => sum + item.price, 0);
    subtotal.textContent = currency.format(total);
    // Keep keyboard focus in the bag when its controls become unavailable.
    const disablingFocusedButton = bag.length === 0 && [removeButton, clearButton].includes(document.activeElement);
    removeButton.disabled = bag.length === 0;
    clearButton.disabled = bag.length === 0;
    if (disablingFocusedButton) {
      document.querySelector('#bag-title').setAttribute('tabindex', '-1');
      document.querySelector('#bag-title').focus({ preventScroll: true });
    }
    status.textContent = `${message} ${bag.length} ${bag.length === 1 ? 'item' : 'items'} in the sample bag; subtotal ${currency.format(total)}. Demo only.`;
  }

  finish.addEventListener('change', () => updatePreview(true));
  addButton.addEventListener('click', () => {
    const selected = selectedFinish();
    if (!selected) return;
    bag.push({ ...selected });
    renderBag(`Added Orbit in ${selected.name}.`);
  });
  removeButton.addEventListener('click', () => {
    const removed = bag.pop();
    if (removed) renderBag(`Removed the last Orbit in ${removed.name}.`);
  });
  clearButton.addEventListener('click', () => {
    bag.length = 0;
    renderBag('Sample bag cleared.');
  });

  updatePreview();
  // Reveal enhancements only after their state and event handlers exist.
  controls.hidden = false;
  actions.hidden = false;
})();
