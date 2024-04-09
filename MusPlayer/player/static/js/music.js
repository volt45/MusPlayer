player = document.getElementById('player')
current_time = document.getElementById('current_time')





function play_this(event, name, author, url){
    player.setAttribute('src', 'https://firebasestorege.googleapis.com/v0/b/musicplayer-1e483.appspot.com/o/' + url)
    music_name.innerHTML = name
    music_author.innerHTML = author
    let buttons = document.getElementsByClassName("play_btn")
    for (let button of buttons){
        button.style = "opacity: 0"
    }
    event.target.getElementsByClassName("play_btn")[0].style = "opacity: 1"
    player.play()
}