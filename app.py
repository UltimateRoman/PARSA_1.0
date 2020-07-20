from helper import expm, expf, telldate
from pyautogui import screenshot
from flask import Flask, render_template, redirect

app = Flask(__name__)

fln = telldate()
mlist = expm()
flist = expf()

@app.route("/")
def index():
    return render_template("index.html",mlist=mlist,flist=flist)

@app.route("/sshot")
def sshot():
    screenshot("images/"+fln+".png")
    return redirect("/")

if __name__ == "__main__":
    app.run()
