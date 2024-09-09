export function showPageDesc() {
    document.querySelectorAll('.page-desc').forEach(block => {
        const rect = block.getBoundingClientRect();
        const windowHeight = window.innerHeight;

        if (rect.top <= windowHeight && rect.bottom >= 0) {
            block.classList.add('show');
        }
    });
}

export function contactFormInformation() {
    const inputs = document.querySelectorAll('.form-control');

    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentNode.classList.add('is-focused');

            const inputMessages = {
              text: "We never share your sensitive personal information",
              email: "We will never share your email outside",
            };

            if (!this.parentNode.querySelector(".bmd-notation")) {
                const span = document.createElement("span");
                span.classList.add("bmd-notation");
                span.textContent = inputMessages[this.type] || '';
                this.parentNode.appendChild(span);
            }
        });

        input.addEventListener('blur', function() {
            this.parentNode.classList.remove('is-focused');

            const span = this.parentNode.querySelector(".bmd-notation");
            if (span) {
                this.parentNode.removeChild(span);
            }

            if (this.value !== "") {
                this.parentNode.classList.add('is-filled');
            } else {
                this.parentNode.classList.remove('is-filled');
            }
        });

        input.addEventListener("input", function() {
            if (this.value !== "") {
                this.parentNode.classList.add("is-filled");
            } else {
                this.parentNode.classList.remove("is-filled");
            }
        });

        if (input.value !== "") {
            input.parentNode.classList.add("is-filled");
        }
    });
}

export function contactInformationPopup() {
    const contactInformationBlocks = document.querySelectorAll('.contact-information');

    function checkContactInfoBlocks() {
        contactInformationBlocks.forEach((block, index) => {
            const rect = block.getBoundingClientRect();
            const windowHeight = window.innerHeight;

            if (rect.top <= windowHeight && rect.bottom >= 0) {
                setTimeout(() => {
                    block.classList.add('show');
                }, index * 120);
            }
        });
    }

    window.addEventListener('scroll', checkContactInfoBlocks);
    window.addEventListener('resize', checkContactInfoBlocks);
    checkContactInfoBlocks();
}

export function showModalMessage() {
    const modal = document.querySelector('.messages');

    if (modal) {
        modal.classList.add('show');

        setTimeout(() => {
            modal.style.maxHeight = '0';

            setTimeout(() => {
                modal.classList.remove('show');
            }, 1000);
        }, 5000);
    }
}