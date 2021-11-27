from flask import Flask, request,jsonify,Response,render_template,Markup,redirect
from flask_cors import CORS
import json
import requests
from utils import get_entities,prof_list,get_title_freq,person2id
import datetime
import io
import random
import numpy as np
from matplotlib.backends.backend_svg import FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

CORS(app)

prof_D = prof_list()
D_m,D_f = get_entities()
F_m,F_f = get_title_freq()

l = sorted(['%s/%s'%(m,prof_D[m]) for m in D_m])


def get_r(name,D):
    r = []
    counts = []
    if name is not None and name in D:
        ents = set([k for y in D[name] for k in D[name][y]])
        ents = list(ents)
        ent_counts = {}
        for y in D[name]:
            for k in ents:
                if k in D[name][y]:
                    if not k in ent_counts:
                        ent_counts[k] = 0
                    ent_counts[k] = ent_counts[k] + D[name][y][k]
        ents = [e for _,e in sorted(zip(ent_counts.values(),ent_counts.keys()),reverse=True)]
        counts = sorted(ent_counts.values(),reverse=True)[:200]
        r = []
        for e in ents[:200]:
            elem = {'name': e, 'data': [], 'type':'area'}
            for y in sorted(D[name]):
                if e in D[name][y]:
                    elem['data'].append([y,D[name][y][e]])
                else:
                    elem['data'].append([y,0])
            r.append(elem)
    return r,counts

@app.route('/query',methods=['GET'])
def get_person():
    result = {}
    url = 'https://query.wikidata.org/sparql'
    job = request.args.get('job')
    person = request.args.get('person')
    if job and person:
        query = """
SELECT ?itemLabel ?image ?birth WHERE {
  ?item wdt:P31 wd:Q5.
  ?item ?label "%s"@it .
  ?item wdt:P106 ?occupation.
  ?occupation ?label "%s"@it .
  ?item wdt:P18 ?image.
  ?item wdt:P569 ?birth.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "it". }
}
"""%(person,job)
        r = requests.get(url, params={'format': 'json', 'query': query})
        data = r.json()
        results = data['results']['bindings']
        if len(results)> 0:
            result['name'] = results[0]['itemLabel']['value']
            result['birth'] = results[0]['birth']['value'].split('T')[0]
            result['image'] = results[0]['image']['value']
    return jsonify(result)

def create_figure(person):
    if person in person2id:
        i = int(person2id[person])
        words = []
        a = []
        folder = int(i/1000)
        with open('nns/%d/%d.tsv'%(folder,i)) as f:
            for j,line in enumerate(f):
                line = line[:-1].split('\t')
                if j == 0:
                    words = line[1:]
                else:
                    a.append([float(v) for v in line[1:len(words)]])
        a = np.array(a).T
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_xticks(range(0,2005-1948,8))
        axis.set_xticklabels(range(1948,2006,8))
        axis.set_yticks(range(10))
        axis.set_yticklabels(["%s"%w for w in words])
        cax = axis.imshow(a,aspect='auto')
        fig.colorbar(cax)
        fig.tight_layout()
        return fig
    else:
        return None

@app.route('/plot')
def plot_png():
    person = request.args.get('person')
    if person:
        fig = create_figure(person)
        if not fig == None:
            output = io.BytesIO()
            FigureCanvas(fig).print_svg(output)
            return Response(output.getvalue(), mimetype='image/svg')
        else:
            return Response("<svg></svg>", mimetype='image/svg')
    else:
        return Response("<svg></svg>", mimetype='image/svg')

@app.route('/index.html',methods=['GET'])
def home():
    if request.args.get('job'):
        name = request.args.get('job').split('/')[0]
        name_f = prof_D[name]
        r,counts = get_r(name,D_m)
        r2,counts2 = get_r(name_f,D_f)
        if name_f in F_f:
            fr_f = {'name': 'cumulativa', 'data': F_f[name_f], 'type': 'line'}
        if name in F_m:
            fr_m = {'name': 'cumulativa', 'data': F_m[name], 'type': 'line'}
    else:
        name = ""
        name_f = ""
        r = {}
        counts = []
        r2 = {}
        counts2 = []
        fr_m = {}
        fr_f = {}
    return render_template("index.html", prof_m=name, prof_f=name_f, timeseries=r, counts=counts, timeseries_f=r2, counts_f=counts2, item_list=l, fr_f=fr_f, fr_m=fr_m)

@app.route('/')
def hello():
    return redirect("index.html", code=302)

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run()







