from flask import Flask, Blueprint, request, render_template
import os

images = os.path.join('static','img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = images

views = Blueprint('views', __name__)

@views.route("/")
@views.route("/home", methods=['POST','GET'])
def home():
    ben10 = os.path.join(app.config['UPLOAD_FOLDER'], 'ben10.jpg')
    adventureTime = os.path.join(app.config['UPLOAD_FOLDER'], 'Adventure Time.jpeg')
    alienForce = os.path.join(app.config['UPLOAD_FOLDER'], 'alienforce.jpg')
    am = os.path.join(app.config['UPLOAD_FOLDER'], 'am.jpg')
    americanDragon = os.path.join(app.config['UPLOAD_FOLDER'], 'americangragon.jpg')
    benBackground = os.path.join(app.config['UPLOAD_FOLDER'], 'benbackground.jpg')
    bravo = os.path.join(app.config['UPLOAD_FOLDER'], 'bravo.jpg')
    campLazlo = os.path.join(app.config['UPLOAD_FOLDER'], 'Camp Lazlo.jpg')
    codename = os.path.join(app.config['UPLOAD_FOLDER'], 'Codename.jpg')
    courage = os.path.join(app.config['UPLOAD_FOLDER'], 'courage.jpg')
    cover = os.path.join(app.config['UPLOAD_FOLDER'], 'cover.png')
    cowAndChicken = os.path.join(app.config['UPLOAD_FOLDER'], 'cowandchicken.jpg')
    dextersLab = os.path.join(app.config['UPLOAD_FOLDER'], 'dexterslabo.jpg')
    eddy = os.path.join(app.config['UPLOAD_FOLDER'], 'Eddy.jpg')
    foster = os.path.join(app.config['UPLOAD_FOLDER'], "Foster's Home for Imaginary Friends.jpg")
    genRex = os.path.join(app.config['UPLOAD_FOLDER'], 'genrex.jpg')
    weasel = os.path.join(app.config['UPLOAD_FOLDER'], 'I Am Weasel.jpg')
    label = os.path.join(app.config['UPLOAD_FOLDER'], 'label.png')
    monsuno = os.path.join(app.config['UPLOAD_FOLDER'], 'Monsuno.jpg')
    monkey = os.path.join(app.config['UPLOAD_FOLDER'], "Monkey.jpg")
    powerpuffgirls = os.path.join(app.config['UPLOAD_FOLDER'], 'powerpuffgirls.jpg')
    profilePic = os.path.join(app.config['UPLOAD_FOLDER'], 'pr.jpeg')
    rex = os.path.join(app.config['UPLOAD_FOLDER'], 'rex.png')
    rexBackground = os.path.join(app.config['UPLOAD_FOLDER'], 'rexbackground.webp')
    samJack = os.path.join(app.config['UPLOAD_FOLDER'], 'samjack.jpg')
    scooby = os.path.join(app.config['UPLOAD_FOLDER'], 'Scooby-Doo! Mystery Incorporated.jpg')
    stevenUniverse = os.path.join(app.config['UPLOAD_FOLDER'], 'Steven Universe.jpg')
    teenTitans = os.path.join(app.config['UPLOAD_FOLDER'], 'Teen Titans.jpg')
    grimAdventures = os.path.join(app.config['UPLOAD_FOLDER'], 'The Grim Adventures of Billy & Mandy.jpg')
    flapJack = os.path.join(app.config['UPLOAD_FOLDER'], 'The Marvelous Misadventures of Flapjack.jpg')
    ultimateAlien = os.path.join(app.config['UPLOAD_FOLDER'], 'ultimatealien.jpg')
    uncleGrandpa = os.path.join(app.config['UPLOAD_FOLDER'], 'Uncle Grandpa.jpeg')
    
    return render_template('index.html', ben10=ben10, adventureTime=adventureTime, alienForce=alienForce, am=am, americanDragon=americanDragon, 
    benBackground=benBackground, bravo=bravo, campLazlo=campLazlo, codename=codename, courage=courage, cover=cover, cowAndChicken=cowAndChicken, 
    dextersLab=dextersLab, eddy=eddy, foster=foster, genrex=genRex, weasel=weasel, label=label, monsuno=monsuno, monkey=monkey, 
    powerpuffgirls=powerpuffgirls, profilePic=profilePic, rex=rex, rexBackground=rexBackground, samJack=samJack, scooby=scooby, 
    stevenUniverse=stevenUniverse, teenTitans=teenTitans, grimAdventures=grimAdventures, flapJack=flapJack, ultimateAlien=ultimateAlien, uncleGrandpa=uncleGrandpa)


