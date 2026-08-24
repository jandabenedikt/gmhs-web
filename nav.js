// Rozbalovací menu v hlavičce — funguje na najetí myší i na klik, ale
// nezavírá se předčasně: jakmile je seznam otevřený, zůstává otevřený,
// dokud návštěvník nenajede na jinou hlavní položku, neklikne mimo menu,
// nebo nestiskne Escape. Neexistuje žádný "mezerový" okamžik, kdy by se
// seznam zavřel jen proto, že myš na cestě k položce chvíli opustí menu.
document.addEventListener('DOMContentLoaded', function () {
  var items = Array.prototype.slice.call(document.querySelectorAll('.nav-item'));

  function closeAll(except) {
    items.forEach(function (item) {
      if (item === except) return;
      item.classList.remove('open');
      var btn = item.querySelector('button.nav-link');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    });
  }

  function openItem(item) {
    closeAll(item);
    item.classList.add('open');
    var btn = item.querySelector('button.nav-link');
    if (btn) btn.setAttribute('aria-expanded', 'true');
  }

  items.forEach(function (item) {
    var btn = item.querySelector('button.nav-link');
    if (!btn) return;

    // Najetí myší otevře menu (a přepne z jiné otevřené položky).
    item.addEventListener('mouseenter', function () {
      openItem(item);
    });

    // Klik menu otevře, nebo ho zavře, pokud je zrovna tahle položka otevřená.
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      if (item.classList.contains('open')) {
        closeAll(null);
      } else {
        openItem(item);
      }
    });
  });

  // Kliknutí mimo menu ho zavře.
  document.addEventListener('click', function () {
    closeAll(null);
  });

  // Escape ho zavře taky.
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeAll(null);
  });
});
