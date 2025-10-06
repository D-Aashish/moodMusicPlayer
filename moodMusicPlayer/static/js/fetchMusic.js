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