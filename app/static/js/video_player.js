document.addEventListener("DOMContentLoaded", function() {
    const video = document.querySelector("#video-presentation");
    const playButton = document.querySelector("#play-button");
    const icon = document.querySelector("#play-icon");

    function play() {
        if (video.paused) {
            video.play();
            icon.classList.remove('fa-circle-play');
            icon.classList.add('fa-circle-pause');
        } else {
            video.pause();
            icon.classList.remove('fa-circle-pause');
            icon.classList.add('fa-circle-play');
        }
    }

    playButton.addEventListener("click", play);
    video.addEventListener("click", play);
});