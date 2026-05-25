from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    height:100vh;
    font-family:Arial, sans-serif;

    background: radial-gradient(circle at top, #4fc3ff, #0077ff 45%, #004fc4);

    overflow:hidden;

    display:flex;
    justify-content:center;
    align-items:center;

    text-align:center;
    color:white;
}

.confetti{
    position:absolute;
    font-size:28px;
}

.c1{top:12%; left:18%;}
.c2{top:20%; right:22%;}
.c3{bottom:14%; left:16%;}
.c4{bottom:18%; right:18%;}
.c5{top:30%; left:6%;}
.c6{top:32%; right:6%;}

.container{
    z-index:2;
}

.cake{
    font-size:45px;
    margin-bottom:15px;
}

h1{
    font-size:45px;
    margin:0;
    text-shadow:3px 3px 10px #004080;
}

.big{
    color:#ffe45c;
    font-size:60px;
}

p{
    font-size:18px;
    text-shadow:2px 2px 8px #004080;
}

.farsi{
    font-size:22px;
    margin-top:20px;
    color:#ffe45c;
}

.buttons{
    display:flex;
    justify-content:center;
    gap:25px;
    margin-top:35px;
}

button{
    width:180px;
    height:80px;

    border:none;
    border-radius:18px;

    font-size:24px;
    font-weight:bold;

    color:white;
    cursor:pointer;

    box-shadow:0 6px 0 rgba(0,0,0,0.25);
}

small{
    font-size:14px;
}

#yes{
    background:linear-gradient(#7df56f, #15b84f);
}

#no{
    background:linear-gradient(#ff6f9f, #e92f68);
}

#no.moving{
    position:absolute;
}

.result{
    text-align:center;
}

.result h1{
    font-size:70px;
    margin-bottom:25px;
}

video{
    width:700px;
    border-radius:25px;
    box-shadow:0 0 25px rgba(255,255,255,0.5);
}

</style>

</head>

<body>

<div class="confetti c1">🎈</div>
<div class="confetti c2">💖</div>
<div class="confetti c3">🎉</div>
<div class="confetti c4">🎊</div>
<div class="confetti c5">🎈</div>
<div class="confetti c6">🎈</div>

<div class="container">

    <div class="cake">🎂</div>

    <h1>
        Is vandaag<br>
        <span class="big">JOUW</span> speciale dag?
    </h1>

    <p class="farsi">
        لبخندت قشنگ‌ترین هدیه‌ایه که زندگی بهم داده 💛
    </p>

    <div class="buttons">

        <button id="yes" onclick="showGif()">
            🤍 Ja!
            <br>
            <small>Dat ben ik! 🎉</small>
        </button>

        <button id="no" onmouseover="moveButton()">
            💔 Nee
            <br>
            <small>Niet vandaag 😅</small>
        </button>

    </div>

</div>

<script>

function moveButton(){

    let button = document.getElementById("no");

    button.classList.add("moving");

    let x = Math.random() * (window.innerWidth - 220);
    let y = Math.random() * (window.innerHeight - 100);

    button.style.left = x + "px";
    button.style.top = y + "px";
}

function showGif(){

    document.querySelector(".container").innerHTML = `

        <div class="result">

            <h1>🎉🎂✨</h1>

            <video autoplay loop muted playsinline>
                <source src="https://i.imgur.com/UMzgKUf.mp4" type="video/mp4">
            </video>

        </div>

    `;
}

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
