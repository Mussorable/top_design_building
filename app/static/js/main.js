import {emailFieldValidation, phoneFieldValidation} from './formValidation.js';
import {contactInformationPopup, showPageDesc, contactFormInformation, showModalMessage} from "./textAnimation.js";
import {imageLevitation, imagePopupWhenScroll} from "./imageAnimation.js";
import {setVideoPlayer} from "./videoPlayer.js";
import {setGallery} from "./lightbox.js";
import {setServicesNavigation} from './serviceNavigation.js';

document.addEventListener("DOMContentLoaded", function() {
    //  Contact form validation
    emailFieldValidation();
    phoneFieldValidation();
    //  Text animation
    contactInformationPopup();
    showPageDesc();
    contactFormInformation();
    //  Image animation
    imageLevitation();
    imagePopupWhenScroll();
    //  Video player
    setVideoPlayer();
    //  Image gallery
    setGallery();
    //  Services navigation menu with animation
    setServicesNavigation();
    //  Modals
    showModalMessage();
});