export function emailFieldValidation() {
    const emailInput = document.querySelector('#email');
    const emailRegex = /^[a-zA-Z0-9._%+-]{2,25}@[a-zA-Z0-9.-]{1,15}\.[a-zA-Z]{2,6}$/;

    if (emailInput) {
        emailInput.addEventListener('input', function () {
            const emailValue = this.value.trim();

            if (emailRegex.test(emailValue) || emailValue.length === 0) {
                this.classList.remove('invalid');
            } else {
                this.classList.add('invalid');
            }
        });
    }
}

export function phoneFieldValidation() {
    const phoneNumberInput = document.querySelector('#phone_number');

    if (phoneNumberInput) {
        phoneNumberInput.addEventListener('input', function () {
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
    }
}