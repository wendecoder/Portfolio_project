#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
from random import choices
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------

Show = db.Table('shows',
               db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
               db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'), primary_key=True),
               db.Column('start_time', db.DateTime(timezone=True), primary_key=True))
#def __init__(shows, artist_id, venue_id, start_time):
  #shows.artist_id = artist_id
  #shows.venue_id = venue_id
  #shows.start_time = start_time

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True)
    genres = db.Column(db.ARRAY(db.String(120)), nullable=True)
    playing_at = db.relationship('Venue', secondary=Show, backref=db.backref('hosts', lazy='joined'))
    start_time = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, name, city, state, phone, image_link, facebook_link, website, seeking_talent, seeking_description, genres):
      self.name = name
      self.city = city
      self.state = state
      self.phone = phone
      self.image_link = image_link
      self.facebook_link = facebook_link
      self.website = website
      self.seeking_talent = seeking_talent
      self.seeking_description = seeking_description
      self.genres = genres

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500), nullable=True) 
    genres = db.Column(db.ARRAY(db.String(120)), nullable=True) 
    start_time = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, name, city, state, address, phone, image_link, facebook_link, website, seeking_talent, seeking_description, genres):
      self.name = name
      self.city = city
      self.state = state
      self.address = address
      self.phone = phone
      self.image_link = image_link
      self.facebook_link = facebook_link
      self.website = website
      self.seeking_talent = seeking_talent
      self.seeking_description = seeking_description
      self.genres = genres

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  venue = Venue.query.all()
  i = len(venue)
  data = []
  for obj in range(0, i):
    dat={
      "city": venue[obj].city,
      "state": venue[obj].state,
    #venid = Venue.query.filter_by(city = venue[obj].city).all()
    #j = len(venid)
    #for ob in range(0, j):
      "venues": [{
        "id": venue[obj].id,
        "name": venue[obj].name,
        "num_upcoming_shows": [len(venue[obj].hosts)],
        }] }
      
    data.append(dat)
      #{
      #  "id": obj.id,
     #   "name": obj.name,
      #  "num_upcoming_shows": obj.num_upcoming_shows,
     # }]
    
    #, {
   # "city": venue[1].city,
   # "state": venue[1].state,
   # "venues": [{
    #  "id": venue[1].id,
    #  "name": venue[1].name,
    #  "num_upcoming_shows": venue[1].num_upcoming_shows,
    #}]
 # }]
  return render_template('pages/venues.html', areas=data);

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  form = SearchForm()
  search_term = request.form['search_term']
  venue = Venue.query.filter(Venue.name.ilike("%"+search_term+"%")).all()
  j = len(venue)
  response = {}
  temp2 = []
  for n in range(j):
    temp={
      "count": n + 1}
    response.update(temp)
    for n in range(j-(j-(n + 1))):
      tem = {
          "id": venue[n].id,
          "name":venue[n].name,
          "num_upcoming_shows": 0,
        }
    temp2.append(tem)
    temp3 = {
      "data": temp2
    }
    response.update(temp3)
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  venue = Venue.query.get(venue_id)
  data={
    "id": venue.id,
    "name": venue.name,
    "genres": venue.genres,
    "address": venue.address,
    "city": venue.city,
    "state": venue.state,
    "phone": venue.name,
    "website": venue.website,
    "facebook_link": venue.facebook_link,
    "seeking_talent": venue.seeking_talent,
    "seeking_description": venue.seeking_description,
    "image_link": venue.image_link}
  i = len(venue.hosts)
  pa = {}
  for n in range(i):
    pas= {"past_shows": [{
      "artist_id": venue.hosts[n].id,
      "artist_name": venue.hosts[n].name,
      "artist_image_link": venue.hosts[n].image_link,
      "start_time": str(venue.hosts[n].start_time)
      }],
    "upcoming_shows":[],
    "past_shows_count": [len(venue.hosts)],
    "upcoming_shows_count": len(venue.hosts) -1,
    }
    pa.update(pas)
  data.update(pa)
  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # called upon submitting the new venue listing form
  try:
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    address = request.form['address']
    phone = request.form['phone']
    image = request.form['image_link']
    genres = request.form['genres']
    facebook = request.form['facebook_link']
    website = request.form['website_link']
    seekingTalent = request.form['seeking_talent']
    if seekingTalent == 'y':
      seekingTalent = True
    else:
      seekingTalent = False
    seeking_description = request.form['seeking_description']

    object1 = Venue(name, city, state, address, phone, image, facebook, website, seekingTalent, seeking_description, [genres])
    db.session.add(object1)
    db.session.commit()
    temp = Venue.query.filter_by(name = name).first()
    venname = temp.name
    # on successful db insert, flash success
    flash('Venue ' + venname + ' was successfully listed!')
  except Exception:
    db.session.rollback()
    # on unsuccessful db insert, flash an error instead.
    flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
  finally:
    db.session.close()

  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):

  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  obj = Venue.query.filter_by(id = venue_id).first()
  db.session.delete(obj)
  db.session.commit()


  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return None

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  artist = Artist.query.all()
  j = len(artist)
  data = []
  for n in range(j):
    dat = {
      "id": artist[n].id,
    "name": artist[n].name,
    }
    data.append(dat)
    
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  form = SearchForm()
  search_term = request.form['search_term']
  artist = Artist.query.filter(Artist.name.ilike("%"+search_term+"%")).all()
  j = len(artist)
  response = {}
  temp2 = []
  for n in range(j):
    temp={
      "count": n + 1}
    response.update(temp)
    for n in range(j-(j-(n + 1))):
      tem = {
          "id": artist[n].id,
          "name":artist[n].name,
          "num_upcoming_shows": 0,
        }
    temp2.append(tem)
    temp3 = {
      "data": temp2
    }
    response.update(temp3)
    
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  artist = Artist.query.get(artist_id)
  data={
    "id": artist.id,
    "name": artist.name,
    "genres": artist.genres,
    "city": artist.city,
    "state": artist.state,
    "phone": artist.phone,
    "website": artist.website,
    "facebook_link": artist.facebook_link,
    "seeking_venue": artist.seeking_venue,
    "seeking_description": artist.seeking_description,
    "image_link": artist.image_link}
  i = len(artist.playing_at)
  pe = {}
  for n in range(i):
    des = {
      "past_shows": [{
      "venue_id": artist.playing_at[n].id,
      "venue_name": artist.playing_at[n].name,
      "venue_image_link": artist.playing_at[n].image_link,
      "start_time":str(artist.playing_at[n].start_time)
      }],    
      "upcoming_shows": [],
      "past_shows_count": len(artist.playing_at),
      "upcoming_shows_count": len(artist.playing_at) + 1,
    }
    pe.update(des)
  data.update(pe)

  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist1 = Artist.query.get(artist_id)
  artist={
    "id": artist1.id,
    "name": artist1.name,
    "genres": artist1.genres,
    "city": artist1.city,
    "state": artist1.state,
    "phone":artist1.phone,
    "website": artist1.website,
    "facebook_link": artist1.facebook_link,
    "seeking_venue": artist1.seeking_venue,
    "seeking_description": artist1.seeking_description,
    "image_link": artist1.image_link
  }
  
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  form = ArtistForm()
  try:
    artist = Artist.query.get(artist_id)
    artist.name = request.form['name']
    artist.genres = [request.form['genres']]
    artist.city = request.form['city']
    artist.state = request.form['state']
    artist.phone = request.form['phone']
    artist.website = request.form['website_link']
    artist.facebook_link = request.form['facebook_link']
    artist.seeking_venue = request.form['seeking_venue']
    if artist.seeking_venue == 'y':
      artist.seeking_venue = True
    else:
      artist.seeking_venue = False
    artist.seeking_description = request.form['seeking_description']
    artist.image_link = request.form['image_link']
    db.session.add(artist)
    db.session.commit()
    flash("Artist " + request.form['name'] + " had been edited successfully.")
  except Exception:
    db.session.rollback()
    flash("Error occured. Artist " + request.form['name'] + " couldn't be edited.")
  finally:
    db.session.close()
  # artist record with ID <artist_id> using the new attributes

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue1 = Venue.query.get(venue_id)
  venue={
    "id": venue1.id,
    "name": venue1.name,
    "genres": venue1.genres,
    "address": venue1.address,
    "city": venue1.city,
    "state":venue1.state,
    "phone": venue1.phone,
    "website":venue1.website,
    "facebook_link":venue1.facebook_link,
    "seeking_talent": venue1.seeking_talent,
    "seeking_description": venue1.seeking_description,
    "image_link": venue1.image_link
  }

  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  form = VenueForm()
  # venue record with ID <venue_id> using the new attributes
  try:
    venue = Venue.query.get(venue_id)
    venue.name = request.form['name']
    venue.genres = [request.form['genres']]
    venue.address = request.form['address']
    venue.city = request.form['city']
    venue.state = request.form['state']
    venue.phone = request.form['phone']
    venue.website = request.form['website_link']
    venue.facebook_link = request.form['facebook_link']
    venue.seeking_talent = request.form['seeking_talent']
    if venue.seeking_talent == 'y':
      venue.seeking_talent = True
    else:
      venue.seeking_talent = False
    venue.seeking_description = request.form['seeking_description']
    venue.image_link = request.form['image_link']
    db.session.add(venue)
    db.session.commit()
    flash("Venue " + request.form['name'] + " had been edited successfully")
  except Exception:
    db.session.rollback()
    flash("An error occured. Venue " + request.form['name'] + " couldn't be edited.")
  finally:
    db.session.close()

  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  try:
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    phone = request.form['phone']
    image = request.form['image_link']
    genres = request.form['genres']
    facebook = request.form['facebook_link']
    website = request.form['website_link']
    seekingTalent = request.form['seeking_venue']
    if seekingTalent == 'y':
      seekingTalent = True
    else:
      seekingTalent = False
    seeking_description = request.form['seeking_description']

    object1 = Artist(name, city, state, phone, image, facebook, website, seekingTalent, seeking_description, [genres])
    db.session.add(object1)
    db.session.commit()
    temp = Artist.query.filter_by(name = name).first()
    venname = temp.name
    # on successful db insert, flash success
    flash('Artist ' + venname + ' was successfully listed!')
  except Exception:
    db.session.rollback()
    # on unsuccessful db insert, flash an error instead.
    flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
  finally:
    db.session.close()

  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows

  shows = db.session.query(Show).join(Artist).all()
  
  data = []
  i = len(shows)
  for i in range(i):
    artist_id = shows[i].artist_id
    venue_id = shows[i].venue_id
    artist = Artist.query.get(artist_id)
    venue = Venue.query.get(venue_id)
    
    dat = {
      "venue_id": venue.id,
      "venue_name": venue.name,
      "artist_id": artist.id,
      "artist_name": artist.name,
      "artist_image_link": artist.image_link,
      "start_time": str(shows[i].start_time)
    }
    data.append(dat)
  
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  
  try:
    artist_id = request.form['artist_id']
    venue_id = request.form['venue_id']
    start_time = request.form['start_time']
  
    db.session.execute(Show.insert(), params={"artist_id": artist_id, "venue_id": venue_id, "start_time": start_time})
    db.session.commit()
    # on successful db insert, flash success
    flash('Show was successfully listed!')
  except Exception:
    db.session.rollback()
    # on unsuccessful db insert, flash an error instead.
    flash('An error occurred. Show could not be listed.')
  finally:
    db.session.close()

  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
