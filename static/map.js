const dataNode = document.getElementById("map-data");
const host = document.getElementById("map");
if (dataNode && host && window.L) {
  const homes = JSON.parse(dataNode.textContent);
  const frame = host.dataset.frame || "";
  const map = L.map(host, { scrollWheelZoom: true }).setView([6.47, 3.45], 11);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap",
    maxZoom: 19,
  }).addTo(map);

  const preview = document.getElementById("map-preview");
  let hideTimer = 0;
  let quiet = true;

  function placePreview(home) {
    if (!preview) return;
    const point = map.latLngToContainerPoint([home.lat, home.lng]);
    const below = point.y < 180;
    preview.hidden = false;
    preview.href = home.url;
    preview.classList.toggle("is-below", below);
    preview.style.left = `${point.x}px`;
    preview.style.top = `${point.y}px`;
    preview.innerHTML = `<span class="map-preview-card"><img src="${home.photo}" alt="" /><span class="map-preview-copy"><span class="serif">${home.label}</span><span class="muted">${home.type} · ${home.beds} bd · ${home.baths} ba</span><span>${home.street}</span></span></span>`;
  }

  function showPreview(home) {
    window.clearTimeout(hideTimer);
    placePreview(home);
  }

  function scheduleHide() {
    window.clearTimeout(hideTimer);
    hideTimer = window.setTimeout(() => {
      if (preview) preview.hidden = true;
    }, 220);
  }

  homes.forEach((home) => {
    const icon = L.divIcon({
      className: "pin",
      html: `<span class="pill">${home.pill}</span>`,
      iconSize: [104, 36],
      iconAnchor: [52, 18],
    });
    const marker = L.marker([home.lat, home.lng], { icon, keyboard: true });
    marker.on("mouseover", () => {
      marker.setZIndexOffset(1000);
      showPreview(home);
    });
    marker.on("mouseout", () => {
      marker.setZIndexOffset(0);
      scheduleHide();
    });
    marker.on("click", () => {
      window.location.href = home.url;
    });
    marker.addTo(map);
  });

  if (preview) {
    preview.addEventListener("mouseenter", () => window.clearTimeout(hideTimer));
    preview.addEventListener("mouseleave", scheduleHide);
    map.on("move", () => {
      if (preview.hidden) return;
      const current = homes.find((home) => home.url === preview.getAttribute("href"));
      if (current) placePreview(current);
    });
  }

  function fit() {
    quiet = true;
    window.setTimeout(() => {
      quiet = false;
    }, 800);
    if (frame) {
      const [south, west, north, east] = frame.split(",").map(Number);
      map.fitBounds([[south, west], [north, east]], { padding: [36, 36], maxZoom: 15 });
    } else if (homes.length === 1) {
      map.setView([homes[0].lat, homes[0].lng], 14);
    } else if (homes.length > 1) {
      map.fitBounds(homes.map((home) => [home.lat, home.lng]), { padding: [40, 40], maxZoom: 13 });
    }
  }
  fit();

  const areaButton = document.getElementById("search-area");
  if (areaButton) {
    map.on("dragend zoomend", () => {
      if (!quiet) areaButton.hidden = false;
    });
    areaButton.addEventListener("click", () => {
      const bounds = map.getBounds();
      const box = [bounds.getSouth(), bounds.getWest(), bounds.getNorth(), bounds.getEast()]
        .map((part) => part.toFixed(5))
        .join(",");
      const url = new URL(window.location.href);
      url.searchParams.set("box", box);
      url.searchParams.set("area", "all");
      url.searchParams.delete("place");
      url.searchParams.delete("find");
      window.location.href = url.toString();
    });
  }

  const split = document.getElementById("split");
  const showList = document.getElementById("show-list");
  const showMap = document.getElementById("show-map");
  if (split && showList && showMap) {
    function setView(mode) {
      split.classList.toggle("is-list", mode === "list");
      split.classList.toggle("is-map", mode === "map");
      showList.classList.toggle("is-on", mode === "list");
      showMap.classList.toggle("is-on", mode === "map");
      window.setTimeout(() => map.invalidateSize(), 60);
    }
    showList.addEventListener("click", () => setView("list"));
    showMap.addEventListener("click", () => setView("map"));
  }
}
