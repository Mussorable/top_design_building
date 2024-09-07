export function imageLevitation() {
    const images = document.querySelectorAll('.option-img');

    images.forEach(image => {
        const randomDuration = Math.random() * 5 + 5;

        image.style.animationDuration = `${randomDuration}s`;
    });
}

export function imagePopupWhenScroll() {
    const showsUpBlocks = document.querySelectorAll('.scrolling-fast-up');

    function checkVisibility() {
        showsUpBlocks.forEach(block => {
            const rect = block.getBoundingClientRect();
            const windowHeight = window.innerHeight;

            if (rect.top <= windowHeight && rect.bottom >= 0) {
                block.classList.add('visible');
            }
        })
    }

    window.addEventListener('scroll', checkVisibility);
    window.addEventListener('resize', checkVisibility);
}