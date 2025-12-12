document.addEventListener('DOMContentLoaded', function () {
        const audioElements = document.querySelectorAll('audio');
        // console.log(audio);
        // console.log('Found audio elements:', audioElements.length);
        audioElements.forEach((audio, index) => {
            audio.addEventListener('play', function () {
                // console.log(`Track ${index + 1} played`);
                const trackId = audio.dataset.trackId;
                // console.log(`Track id ${trackId} `);
                const songSection = audio.closest('.song-section');
                const imageSrc = songSection.querySelector('img').src;
                const audioSrc = audio.querySelector('source').src;
                const duration = audio.duration;

                const trackName = songSection.querySelector('h3')?.innerText || '';
                const artistName = songSection.querySelector('p:nth-of-type(1)')?.innerText.replace('Artist: ', '') || '';
                const albumName = songSection.querySelector('p:nth-of-type(2)')?.innerText.replace('Album: ', '') || '';
                const releaseDate = songSection.querySelector('p:nth-of-type(3)')?.innerText.replace('Released: ', '') || '';

                
                fetch('/trackPlayed/', {
                    method: 'POST',
                    headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({
                            track_id: trackId,
                            track_name: trackName,
                            artist_name: artistName,
                            album_name: albumName,
                            releasedate: releaseDate,
                            image_url: imageSrc,
                            audio_url: audioSrc,
                            duration: duration
                })
            }).then(response => response.json())
              .then(data => console.log('Server response:', data))
              .catch(error => console.error('Error:', error));
        });

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

    })
});
