document.querySelectorAll(".thumb").forEach((button) => {
  button.addEventListener("click", () => {
    const hero = document.getElementById("hero");
    if (!hero) return;
    hero.src = button.dataset.src;
    document.querySelectorAll(".thumb").forEach((item) => item.classList.remove("is-on"));
    button.classList.add("is-on");
  });
});

const sketch = document.getElementById("sketch");
if (sketch) {
  const price = Number(sketch.dataset.price);
  const down = document.getElementById("down");
  const years = document.getElementById("years");
  const rate = document.getElementById("rate");

  function naira(amount) {
    return `₦${Math.round(amount).toLocaleString("en-NG")}`;
  }

  function payment(balance, yearlyRate, term) {
    const months = term * 12;
    const monthlyRate = yearlyRate / 100 / 12;
    if (!months) return 0;
    if (!monthlyRate) return balance / months;
    return (balance * monthlyRate) / (1 - (1 + monthlyRate) ** -months);
  }

  function draw() {
    const downPct = Number(down.value);
    const term = Number(years.value);
    const yearly = Math.min(40, Math.max(0, Number(rate.value) || 0));
    const balance = price * (1 - downPct / 100);
    document.getElementById("down-label").textContent = String(downPct);
    document.getElementById("down-naira").textContent = `${naira(price - balance)} down`;
    document.getElementById("monthly").textContent = `${naira(payment(balance, yearly, term))} / month`;
    document.getElementById("balance").textContent = `On ${naira(balance)} after the down payment.`;
  }

  [down, years, rate].forEach((field) => field.addEventListener("input", draw));
  draw();
}
