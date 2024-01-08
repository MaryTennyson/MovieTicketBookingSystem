from datetime import datetime

from cinema_class import CinemaHall





class Movie:
    def __init__(self,movie_id, title, description, duration_in_mins, language, release_date, country, genre, added_by):
        self.movie_id=movie_id
        self.title = title
        self.description = description
        self.duration_in_mins = duration_in_mins
        self.language = language
        self.release_date = release_date
        self.country = country
        self.genre = genre
        self.movie_added_by = added_by

        self.shows = []

    def get_shows(self):
        None

class Show:
    def __init__(self, id,created_on, cinemahall_id, movie_id, start_time, end_time):
        self.show_id = id
        self.created_on = created_on
        self.start_time = start_time
        self.end_time = end_time
        self.cinemahall_id = cinemahall_id
        self.movie_id = movie_id
        