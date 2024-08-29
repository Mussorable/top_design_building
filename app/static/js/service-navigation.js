function setInitServiceActive(button, container) {
    button.classList.add('active');
    container.classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
    const serviceButtons = document.querySelectorAll('.service-button');
    const serviceContainers = document.querySelectorAll('.service-container');

    setInitServiceActive(serviceButtons[0], serviceContainers[0]);

    serviceButtons.forEach((button, index) => {
        button.addEventListener('click', (e) => {
            e.preventDefault();

            if (!serviceContainers[index].classList.contains('active')) {
                serviceContainers.forEach((serviceContainer) => {
                    serviceContainer.classList.remove('active');
                });

                serviceContainers[index].classList.add('active');

                serviceButtons.forEach(button => {
                    button.classList.remove('active');
                });
                button.classList.add('active');
            }
        });
    });
});