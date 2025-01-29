document.addEventListener("DOMContentLoaded", function () {
  // Анимация стульев
  gsap.fromTo(
    ".chair",
    {
      x: 0, // начальная позиция
      opacity: 0.5,
    },
    {
      x: 500, // конечная позиция
      opacity: 1,
      duration: 2,
      repeat: -1, // повторять анимацию бесконечно
      yoyo: true, // возвращаться к начальной позиции
    }
  );
});

console.log('Canvas initialized:', canvas);
console.log('Objects received:', objects);