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
    console.log('max:', progress.max, 'seconds');
    progress.value = song.currentTime;
    console.log('min:', progress.value, 'seconds');
    console.log('Duration:', song.duration, 'seconds');
}

document.getElementById("controlMusic").addEventListener('click', playPause);
function playPause(){
    if(control.classList.contains("fa-play")){
        song.play();
        control.classList.replace("fa-play", "fa-pause");
    }
    else{
        song.pause();
        control.classList.replace("fa-pause", "fa-play");
    }
}

// song.addEventListener("timeupdate", function () {
//         progress.value = song.currentTime;
//         console.log("Changing")
//     },500);

    progress.addEventListener("input", function () {
        song.currentTime = progress.value;
    });

if (song.play()){
  setInterval(()=>{
    progress.value = song.currentTime;
    console.log("Changing")
  });
}
});