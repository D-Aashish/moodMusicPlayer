document.addEventListener("DOMContentLoaded", function() {
  let song = document.getElementById("playingSong");
  if (!song) {console.warn("Audio element not found!");
    return;}
  let progress = document.getElementById("songProgress")
  let control =  document.getElementById("controlMusic")
  let bookmark = document.getElementById("bookmark");

song.onloadedmetadata = function (){
    progress.max = song.duration;
    progress.value = song.currentTime;
}

control.addEventListener('click', playPause);
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
    });

if (song.play()){
  setInterval(()=>{
    progress.value = song.currentTime;
    progress.max = song.duration;
    document.querySelector(".musicDuration").textContent = `${formatTime(progress.value)}`
    document.querySelector(".musicMax").textContent = `${formatTime(progress.max)}`
  });
}


bookmark.addEventListener('click', bookMarkSong);
function bookMarkSong(){
  const trackId = "{{ PlayedTrack.id }}";
    // const trackName = document.getElementById('trackName').innerText;
    // const artistName = document.getElementById('artistName').innerText;
    // const imageSrc = document.getElementById('trackImage').src;
    // const audioSrc = document.getElementById('playingSong').src;

    const data = {
        track_id: trackId,
        // track_name: trackName,
        // artist_name: artistName,
        // image_url: imageSrc,
        // audio_url: audioSrc
    };
    console.log("data from control play js bookmark")
  if(bookmark.classList.contains("fa-regular")){
    bookmark.classList.replace("fa-regular", "fa-solid");
    fetch('/bookmarked', {
              method: 'POST',
              headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
              },
              body: JSON.stringify(data)
        }).then(response => response.json())
              .then(data => console.log('Server response:', data))
              .catch(error => console.error('Error:', error))
      }
  else{
    bookmark.classList.replace("fa-solid", "fa-regular");
  }
}


});