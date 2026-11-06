const KEY = "es-saved";

function readSaved() {
  try {
    const value = JSON.parse(localStorage.getItem(KEY) || "[]");
    return Array.isArray(value) ? value : [];
  } catch {
    return [];
  }
}

function writeSaved(ids) {
  localStorage.setItem(KEY, JSON.stringify(ids));
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&",
    "<": "<",
    ">": ">",
    '"': """,
    "'": "&#39;",
  }[char]));
}

function paintSaved() {
  const ids = readSaved();
  const set = new Set(ids);
  document.querySelectorAll(".save-btn").forEach((button) => {
    const on = set.has(button.dataset.id);
    button.setAttribute("aria-pressed", on ? "true" : "false");
    button.classList.toggle("is-on", on);
    button.setAttribute("aria-label", on ? "Remove from saved" : "Save home");
    if (button.classList.contains("btn")) button.textContent = on ? "Saved" : "Save";
  });
  const count = document.querySelector(".saved-count");
  if (count) {
    count.hidden = ids.length === 0;
    count.textContent = String(ids.length);
  }
}

function renderSavedPage() {
  const catalogNode = document.getElementById("catalog");
  const grid = document.getElementById("saved-grid");
  const empty = document.getElementById("saved-empty");
  if (!catalogNode || !grid || !empty) return;
  const ids = new Set(readSaved());
  const homes = JSON.parse(catalogNode.textContent).filter((home) => ids.has(home.id));
  const heart = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20s-7-4.4-7-9a4 4 0 0 1 7-2 4 4 0 0 1 7 2c0 4.6-7 9-7 9z"/></svg>';
  grid.innerHTML = homes
    .map(
      (home) => `<article class="card">
        <a href="${escapeHtml(home.url)}">
          <div class="photo-frame"><img src="${escapeHtml(home.photo)}" alt="" /></div>
          <p class="kicker">${escapeHtml(home.intent)}</p>
          <p class="price">${escapeHtml(home.price)}</p>
          <p class="muted">${escapeHtml(home.meta)}</p>
          <p>${escapeHtml(home.street)}</p>
        </a>
        <button class="icon-btn save-btn is-on" type="button" data-id="${escapeHtml(home.id)}" aria-pressed="true" aria-label="Remove from saved">${heart}</button>
      </article>`,
    )
    .join("");
  empty.hidden = homes.length > 0;
  grid.hidden = homes.length === 0;
}

document.addEventListener("click", (event) => {
  const button = event.target.closest(".save-btn");
  if (!button) return;
  const id = button.dataset.id;
  const ids = readSaved();
  const next = ids.includes(id) ? ids.filter((item) => item !== id) : ids.concat(id);
  writeSaved(next);
  if (document.getElementById("catalog")) renderSavedPage();
  paintSaved();
});

renderSavedPage();
paintSaved();
