document.addEventListener('DOMContentLoaded', function() {
    // Make small images moving left-right with random speed in section around main image
    const images = document.querySelectorAll('.option-img');

    images.forEach(image => {
        const randomDuration = Math.random() * 5 + 5;

        image.style.animationDuration = `${randomDuration}s`;
    });

    // Image shows up when scrolling down
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

    // Add .is-focused when input field is focused
    const inputs = document.querySelectorAll('.form-control');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentNode.classList.add('is-focused');

            const inputMessages = {
              text: "We never share your sensitive personal information",
              password: "PASSWORD MESSAGE",
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
            console.log(span);
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

    // Make phone prefix in phone number field
    const emailInput = document.querySelector('#email');
    const emailRegex = /^[a-zA-Z0-9._%+-]{2,25}@[a-zA-Z0-9.-]{1,15}\.[a-zA-Z]{2,6}$/;
    emailInput.addEventListener('input', function() {
        const emailValue = this.value.trim();

       if (emailRegex.test(emailValue) || emailValue.length === 0) {
           this.classList.remove('invalid');
       } else {
           this.classList.add('invalid');
       }
    });

    const phoneNumberInput = document.querySelector('#phone_number');
    phoneNumberInput.addEventListener('input', function() {
        // Remove all non-digit characters except for '+'
        let cleanedValue = this.value.replace(/[^+\d]/g, '');

        // Add spaces after every 3 characters
        cleanedValue = cleanedValue.replace(/(.{3})/g, '$1 ');

        // Remove the trailing space (if any)
        cleanedValue = cleanedValue.trim();

        // Update the input field with the formatted value
        this.value = cleanedValue;

        // Validate the length of the input (including '+')
        const inputLength = cleanedValue.replace(/\s/g, '').length;

        // Check if the length is between 9 and 12 characters
        if ((cleanedValue.startsWith('+48') && inputLength === 12) || (!cleanedValue.startsWith('+48') && inputLength === 9)) {
            this.classList.remove('invalid');
        } else {
            this.classList.add('invalid');
        }
    });
})