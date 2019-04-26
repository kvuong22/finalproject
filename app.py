import os
from db_populate import *
from SI507project_tools import *
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import csv

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'something something for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./jp_bloom.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#Flask setup with debugging
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


##### Models #####
class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer, primary_key=True)
    areaname = db.Column(db.String(250))
    areatype = db.Column(db.String(250))
    bloomsites = db.relationship('Bloomsite',backref='Area') # list of Site ins


class Bloomdate(db.Model):
    __tablename__ = 'bloomdates'
    id = db.Column(db.Integer, primary_key=True)
    bloomdate = db.Column(db.String(250))
    bloomsites = db.relationship('Bloomsite',backref='Bloomdate')


class Bloomsite(db.Model):
    __tablename__ = "bloomsites"
    id = db.Column(db.Integer, primary_key=True)
    sitename = db.Column(db.String(250), unique=True)
    area_id = db.Column(db.Integer,db.ForeignKey("areas.id"))
    bloom_id = db.Column(db.Integer,db.ForeignKey("bloomdates.id"))



#### Set up Route functions ####
###Main Route
@app.route('/')
def homepage():
    return render_template('home_page.html')


@app.route('/search/<area>/')
def area_search(area):
    if Area.query.filter_by(areaname=area).first():
        area_searched = Area.query.filter_by(areaname=area).first()
        site_bloom_return = []
        matched_areasites = Bloomsite.query.filter_by(area_id=area_searched.id).all()
        for s in matched_areasites:
            site_return = Bloomsite.query.filter_by(sitename=s.sitename).first()
            site_bloom_return.append(s.sitename)
        return render_template('search_area.html',site_bloom_return=site_bloom_return)
    else:
        return render_template('invalid_input.html')


@app.route('/all_site_info/')
def see_all_site_info():
    all_info = []
    blooms = Bloomsite.query.all()
    for b in blooms:
        area = Area.query.filter_by(id=b.area_id).first()
        date = Bloomdate.query.filter_by(id=b.bloom_id).first()
        all_info.append((b.sitename,area.areaname,area.areatype,date.bloomdate))
    return render_template('all_sites.html', all_info=all_info)



if __name__ == '__main__':
    db.create_all() 
    get_bloom_site_data(START_URL)
    get_area_info('site_area_data.csv')
    get_site_info(bloom_site_data)
    get_bloomdate_info(bloom_site_data)

    app.run()
