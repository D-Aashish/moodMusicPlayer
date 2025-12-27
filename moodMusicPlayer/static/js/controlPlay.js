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
  // const trackId = "{{ PlayedTrack}}";
  const trackId = bookmark.dataset.playedTrackId;  
  if (!trackId) {
    console.warn("No track ID found, skipping bookmark");
    return;
  }
  console.log("Track ID:", trackId);

  console.log("track id from bookmark")
  console.log("This is being sent from template :")
  console.log(trackId)

    const data = {
        track_id: trackId,
    };
    console.log("data from control play js bookmark")
    console.log("before bookmark change")
    
    if(bookmark.classList.contains("fa-regular")){
      bookmark.classList.replace("fa-regular", "fa-solid");
      console.log("before change")
    fetch('/bookmarked/', {
              method: 'POST',
              headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
              },
              body: JSON.stringify(data)
        }).then(response => response.json())
              .then(data =>{
                console.log('Server response:', data)
                console.log("this is inside fetch")
              } 
            )
              .catch(error => console.error('Error:', error))
      }
      else{
        bookmark.classList.replace("fa-solid", "fa-regular");
        console.log("inside else of bookmark icon change")
      }
      console.log("after bookmark change")
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

});