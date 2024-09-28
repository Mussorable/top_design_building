export function setGallery() {
    const images = document.querySelectorAll('.content-image');
    const magnifiers = document.querySelectorAll('.fa-magnifying-glass');
    const lightboxModal = document.getElementById('lightbox-modal');
    const lightboxImage = document.getElementById('lightbox-image');
    const closeImage = document.querySelector('.close');

    function openLightboxModal(e) {
        lightboxModal.style.display = 'block';
        if (e.target.src) {
            lightboxImage.src = e.target.src;
        } else {
            const image = e.target.closest('.content').querySelector('.content-image');
            if (image) {
                lightboxImage.src = image.src;
            } else {
                console.error('src attribute is missing');
            }
        }
    }

    if (images.length > 0) {
        images.forEach(image => {
            image.addEventListener('click', openLightboxModal);
        });
        magnifiers.forEach(magnifier => {
            magnifier.addEventListener('click', openLightboxModal);
        })

        closeImage.addEventListener('click', () => {
            lightboxModal.style.display = 'none';
        });
        lightboxModal.addEventListener('click', () => {
            lightboxModal.style.display = 'none';
        });
    }
}

export function setImagesWidth() {
    const imagesBlocks = document.querySelectorAll('.images-block');

    if (imagesBlocks.length > 0) {
        imagesBlocks.forEach((block, index) => {
            const lightboxSections = block.querySelectorAll('.lightbox-section');

            if (index % 2 === 0) {
                lightboxSections[0].classList.add('col-lg-4');
                if (lightboxSections[1]) {
                    lightboxSections[1].classList.add('col-lg-8');
                }
            } else {
                lightboxSections[0].classList.add('col-lg-8');
                if (lightboxSections[1]) {
                    lightboxSections[1].classList.add('col-lg-4');
                }
            }
        });
    }
}