from flask import( Flask , render_template , request)
from ssss import data


app = Flask(__name__)

ru_alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',' ы', 'ь', 'э', 'ю', 'я']

@app.route('/', methods=["GET","POST"])
def main():
    if request.method == 'POST':
        name = request.form.get('name')
        subs_all = request.form.get('subs_all')
        subs_inst = request.form.get('subs_inst')
        subs_Facebook = request.form.get('subs_Facebook')
        subs_Twitter = request.form.get('subs_Twitter')
        info = request.form.get('info')
        url_img = request.form.get('url-img')
        if data[-1]['name'] != name:
            di:dict ={

                'name':name,
                'subs_all': subs_all,
                'subs_inst':subs_inst,
                'subs_Facebook': subs_Facebook,
                'subs_Twitter': subs_Twitter,
                'info' :info,
                'url-img':url_img
            }
            for i in ru_alf:
                if di['name'].lower()[0] == i:
                        data.append(di)
                        return render_template('index.html' , r = data)
    return render_template('index.html', r = data)
if __name__ == "__main__":
    app.run(port=8086, debug=True)