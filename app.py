from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
    <style>
    body{
        text-align:center;
        background:pink;
        margin-top:100px;
        font-family:Arial;
    }

    button{
        font-size:25px;
        padding:15px 30px;
        margin:20px;
    }

    #no{
        position:absolute;
    }

    #gif{
        display:none;
    }

    </style>
    </head>

    <body>

    <h1>Is dit jouw verjaardag? 🎂</h1>

    <button onclick="showGif()">Yes</button>

    <button id="no" onmouseover="moveButton()">No</button>

    <div id="gif">
        <h2>Gefeliciteerd!!! 🎉🎈</h2>

        <img src="https://media.giphy.com/media/feio2yIUMtdqWjRiaF/giphy.gif" width="300">
    </div>

    <script>

    function moveButton(){

        let button = document.getElementById("no");

        let x = Math.random() * 500;
        let y = Math.random() * 300;

        button.style.left = x + "px";
        button.style.top = y + "px";
    }

    function showGif(){
        document.getElementById("gif").style.display = "block";
    }

    </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()