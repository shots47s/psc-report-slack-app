from app import db


class PublicPublications(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  citation = db.Column(db.Text())
  key_psc_author = db.Column(db.String(128))
  abstact = db.Column(db.Text())
  link = db.Column(db.Text())

  def __repr__(self):
    return "Publication: {}".format(citation)
