from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ely'}
    color = {
            'id': 0,
            'author': {'username': 'Ely' },
            'turn': 1,
            'body': "Estate Edgen sits on the periphery of the King's land, nestled in the crook of the river Carrow. It is a complex of broad, regal buildings cut from thick blocks of tightly-fit stone. The stone is pale in color and well-polished.  In the center of the Edgen complex, there is a wide, dirt field in which carpenters have assembled a series of scaffolds. A short distance away, at the edge of the field, lies the main mansion. A stone road leads from the edge of the property, around the dirt field, to the ornate wooden doors and steel portcullis that cover the house's entrance.  At the other end of the road there is a gate. The gate is made of thick iron, and it is set in a tall wall of stone which surrounds the entire property. Guards stand beside the gate at all hours.  House Edgen's servants wear velvet half-masks across their noses and mouths. The masks are colored a pale cream and show no features save for an embossed mark of the House's insignia: A round stone tower beneath a crown with spiked tines. Their livery is also pale cream with a blood-red sash and cummerbund. They all dress impeccably: If their suits ever show a crease, the sensechal beats them. Their heads are covered with ivory hoods. Every last one of them shows perfect posture and never speaks unless directly ordered to.  To the west of the estate, soldiers with red-enameled halberds patrol the edges of the House Edgen stone quarry. A hill here has been sliced in half, showing a core of milky-white stone. Blocky steps lead down into a broad cavern beneath the hill where stonecutters work tirelessly at all hours.  The head of House Edgen is Duke Fariss Edgen. He is an old but cunning man with gray hair and a sharply-trimmed beard. His apartments are in the main mansion, but he keeps no bed there. The room holds a table of polished oak and a pair of gilt and velveted chairs under a massive platinum chandelier. Its lights are visible through the curtained windows at odd hours of the night. Nobody knows where the duke actually sleeps.  His wife, the queen's sister, is the Duchess Oila Rege-Edgen. Rumor says that she married the Duke for his money, and he her for her connections at the royal court. She keeps a sumptuous wine cellar hidden somewhere on the Estate and holds lavish parties every odd weekend. The queen is a frequent guest.  The king never attends. There is bad blood between him and the duke going back generations. Perhaps it's because the kings' Great Tower overlooks Edgen land, visible from everywhere on the estate." 
            }
    return render_template('index.html', user=user, color=color)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Pretending to log in user {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
