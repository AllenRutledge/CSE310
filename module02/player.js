// Select everything and assign it here
let trackSpot = document.querySelector(".song-spot");
let songName = document.querySelector(".song-name");
let songArtist = document.querySelector(".song-artist");

let playButton = document.querySelector(".playpause-song");
let nextButton = document.querySelector(".next-song");
let prevButton = document.querySelector(".prev-song");

let seekSlider = document.querySelector(".seek-slider");
let volumeSlider = document.querySelector(".volume-slider");
let timeNow = document.querySelector(".time-now");
let totalDuration = document.querySelector(".total-duration");

// Global stuff
let index = 0;
let isPlaying = false;
let updateTimer;

// Make program play audio
let songNow = document.createElement('audio');
// List of songs
let songs = [
{   name: "Party Sector",
	artist: "Joth",
    path: "Party_Sector.ogg"},

{   name: "Red Doors (v2)",
    artist: "Matthew Pablo",
	path: "red_doors2.ogg",},

{	name: "Low-Fi",
    artist: "Alexandr Zhelanov",
	path: "low-fi.ogg",},

{	name: "Space Dimensions",
    artist: "Matthew Pablo",
	path: "space_dimensions.ogg",}
];
function loadSong(index) {
    // Clear previous timer
    clearInterval(updateTimer);
    resetValues();
    
    // Load song
    songNow.src = songs[index].path;
    songNow.load();
    
    // Update song details
    songName.textContent = songs[index].name;
    songArtist.textContent = songs[index].artist;
    trackSpot.textContent = 
        "Song " + (index + 1) + " of " + songs.length;
    
    // 1-second interval for updating seek slider.
    updateTimer = setInterval(seekUpdate, 1000);
    
    // Go to next song when done
    songNow.addEventListener("ended", nextSong);
}
// Reset to default values
function resetValues() {
    timeNow.textContent = "00:00";
    totalDuration.textContent = "00:00";
    seekSlider.value = 0;
}
function playPause() {
    // Switch between play and pause
    if (!isPlaying) playSong();
    else pauseSong();
}   
function playSong() {
    // Play loaded song
    songNow.play();
    isPlaying = true;
    // Replace play with pause
    playButton.innerHTML = '<p class="play">II</p>';
}   
function pauseSong() {
    // Pause song
    songNow.pause();
    isPlaying = false;
    // Replace pause with play
    playButton.innerHTML = '<p class="play">[></p>';
}
function nextSong() {
    // Loop forward to first song if you press forward on last song
    if (index < songs.length - 1)
        index += 1;
    else index = 0;    
    // Load and play song
    loadSong(index);
    playSong();
}    
function prevSong() {
    // Loop back to last song if you press back on first song
    if (index > 0)
        index -= 1;
    else index = songs.length - 1;   
    // Load and play song
    loadSong(index);
    playSong();
}

function seekTo() {
    // Percentage-based location of where you are in the song
    seeking = songNow.duration * (seekSlider.value / 100);
    songNow.currentTime = seeking;
}
function setVolume() {
    // Percentage-based location of volume
    songNow.volume = volumeSlider.value / 100;
}
function seekUpdate() {
    let seekPosition = 0;   
    // Is the song's duration legible?
    if (!isNaN(songNow.duration)) {
        seekPosition = songNow.currentTime * (100 / songNow.duration);
        seekSlider.value = seekPosition;
        // Remaining time, then duration
        let currentMinutes = Math.floor(songNow.currentTime / 60);
        let currentSeconds = Math.floor(songNow.currentTime - currentMinutes * 60);
        let durationMinutes = Math.floor(songNow.duration / 60);
        let durationSeconds = Math.floor(songNow.duration - durationMinutes * 60);
        // Add a zero to the single digit time values
        if (currentSeconds < 10) { currentSeconds = "0" + currentSeconds; }
        if (durationSeconds < 10) { durationSeconds = "0" + durationSeconds; }
        if (currentMinutes < 10) { currentMinutes = "0" + currentMinutes; }
        if (durationMinutes < 10) { durationMinutes = "0" + durationMinutes; }
        // Display the updated duration
        timeNow.textContent = currentMinutes + ":" + currentSeconds;
        totalDuration.textContent = durationMinutes + ":" + durationSeconds;
    }
}