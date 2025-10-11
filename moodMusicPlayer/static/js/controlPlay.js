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
    // console.log('max:', progress.max, 'seconds');
    progress.value = song.currentTime;
    // console.log('min:', progress.value, 'seconds');
    // console.log('Duration:', song.duration, 'seconds');
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


 function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, "0")}`;
  }

    progress.addEventListener("input", function () {
        song.currentTime = progress.value;
        progress.max = song.duration;
        document.querySelector(".musicDuration").textContent = `${formatTime(progress.value)}`
        document.querySelector(".musicMax").textContent = `${formatTime(progress.max)}`
        console.log('min:', progress.value, 'seconds');
    console.log('Duration:', song.duration, 'seconds');
    });

if (song.play()){
  setInterval(()=>{
    progress.value = song.currentTime;
    progress.max = song.duration;
    document.querySelector(".musicDuration").textContent = `${formatTime(progress.value)}`
    document.querySelector(".musicMax").textContent = `${formatTime(progress.max)}`
        console.log('min:', progress.value, 'seconds');
    console.log("Changing")
    console.log('min:', progress.value, 'seconds');
    console.log('Duration:', song.duration, 'seconds');
  });
}
});