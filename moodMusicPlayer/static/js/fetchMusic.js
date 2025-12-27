 function fetchMusicByMood(mood) {
     fetch(`/api/?mood=${encodeURIComponent(mood)}`)
            .then(response => {
                if (!response.ok) throw new Error("Mood not found or API error");
          return response.json();
        })
        .then(data => {
            console.log("Fetched songs:", data.songs);
        })
        .catch(error => {
            console.error("Error fetching songs:", error);
            alert(error.message);
        });
          }
document.querySelectorAll(".artist-card").forEach(card => {
  card.addEventListener("click", () => {
    const artist = card.dataset.artist;
    fetchArtistSongs(artist);
  });
});

function fetchArtistSongs(artistName) {
  fetch(`/api/artist-songs/?artist=${encodeURIComponent(artistName)}`)
    .then(res => res.json())
    .then(data => renderSongs(data.songs));
}``