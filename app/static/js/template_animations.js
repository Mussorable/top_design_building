document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.option-img');

    images.forEach(image => {
        const randomDuration = Math.random() * 5 + 5;

        image.style.animationDuration = `${randomDuration}s`;
    });
})