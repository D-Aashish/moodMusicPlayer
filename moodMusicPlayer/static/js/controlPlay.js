document.addEventListener("DOMContentLoaded", function() {
  let song = document.getElementById("playingSong");
  if (!song) {
    console.warn("Audio element not found!");
    return;
  }
// let song = document.getElementById("playingSong")
let progress = document.getElementById("songProgress")
let control =  document.getElementById("controlMusic")

song.onloadedmetadata = function (){
    progress.max = song.duration;
    progress.value = song.currentTime;
    console.log('Duration:', song.duration, 'seconds');
}

document.getElementById("controlMusic").addEventListener('click', playPause);
function playPause(){
    if(control.classList.contains("fa-play")){
        song.play();
        // control.classList.remove("fa-play");
        // control.classList.add("fa-pause");
        control.classList.replace("fa-play", "fa-pause");
    }
    else{
        song.pause();
        // control.classList.remove("fa-pause");
        // control.classList.add("fa-play");
        control.classList.replace("fa-pause", "fa-play");
    }
}
});