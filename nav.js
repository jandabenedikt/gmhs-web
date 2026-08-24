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

// Odsazení pro skoky na kotvy — na stránkách s lištou rychlých odkazů
// (.anchor-nav, position: sticky nahoře) by se jinak nadpis cílové sekce
// po kliknutí na kotvu schoval pod touto lištou. Odsazení se počítá podle
// skutečné výšky lišty, aby fungovalo na všech velikostech obrazovky.
function updateScrollPadding() {
  var bar = document.querySelector('.anchor-nav');
  document.documentElement.style.scrollPaddingTop = bar ? (bar.offsetHeight + 16) + 'px' : '0px';
}
window.addEventListener('DOMContentLoaded', updateScrollPadding);
window.addEventListener('load', updateScrollPadding);
window.addEventListener('resize', updateScrollPadding);
