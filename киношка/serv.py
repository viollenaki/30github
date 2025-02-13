from flask import Flask, jsonify, request
from collections import defaultdict
app = Flask(__name__)

class Movie:
    def __init__(self, movie, price):
        self.name = movie
        self.price = price
        self.seances = {}
        self.seances_profit = defaultdict(list)

    def add_seance(self, seance):
        if seance not in self.seances:
            self.seances[seance] = []

    def add_booking(self, seance, seats):
        self.seances[seance].extend(seats)
        self.seances_profit[seance] += [len(seats)*self.price]

    def get_seances(self):
        arr = []
        for i in self.seances.keys():
            arr.append(i)
        return arr

    def get_seances_booked(self,seance):
        return self.seances.get(seance, [])

    def get_seance_profit(self, seance):
        return sum(self.seances_profit[seance])

    def get_total_profit(self):
        total = 0
        for i,j in self.seances_profit.items():
            total += sum(j)
        return total



class Cinema:
    def __init__(self):
        self.movies = {}
        self.history = []
        self.total = {}

    def add_movie(self, movie, seance, price):
        if movie not in self.movies:
            self.movies[movie] = Movie(movie, price)
            self.movies[movie].add_seance(seance)

        else:
            self.movies[movie].add_seance(seance)
            self.movies[movie].price = price

    def booking(self, user, movie, seance, seats):
        self.movies[movie].add_booking(seance, seats)

        self.history.append((user, movie, seance))



    def get_movies(self):
        arr = []
        for i in self.movies.keys():
            arr.append(i)
        return arr

    def get_movie_seances(self, movie):
        return self.movies[movie].get_seances()

    def get_movie_booked_seats(self,movie, seance):
        return self.movies[movie].get_seances_booked(seance)

    def get_movie_price(self,movie):
        return self.movies[movie].price


    def get_movie_profit(self, movie):
        total = 0
        for i in self.movies[movie].seances_profit.values():
            total += sum(i)
        return total

    def get_movie_seances_count(self, movie):
        return len(self.movies[movie].seances.keys())

    def get_movie_people(self,movie):
        arr = []
        for u,m,s in self.history:
            if m == movie:
                arr.append((u,s))
        return arr

    def get_seance_people(self,movie, seance):
        arr = []
        for u,m,s in self.history:
            if m == movie and s == seance:
                arr.append((u,s))
        return arr

    def get_user_history(self,user):
        arr = []
        for u,m,s in self.history:
            if u == user:
                arr.append((m,s))
        return arr
    def get_total(self):
        total = 0
        for i,j in self.movies.items():
            total += j.get_total_profit()
        return total

cinema = Cinema()

users = {}

@app.route('/get_user')
def get_user():
    user = request.args.get('user')
    if user in users.keys():
        return jsonify(True)
    else:
        return jsonify(False)

@app.route('/add_user')
def add_user():
    user = request.args.get('user')
    password = request.args.get('password')
    users[user] = password
    return jsonify('Added user')

@app.route('/login')
def login():
    name = request.args.get('user')
    password = request.args.get('password')
    if users[name] == password:
        return jsonify(True)
    else:
        return jsonify(False)

@app.route('/add_movie')
def add_movie():
    movie = request.args.get('movie')
    seance =  request.args.get('seance')
    price =  request.args.get('price')
    price = float(price)
    cinema.add_movie(movie,seance,price)
    return jsonify(True)


@app.route('/get_movies')
def get_films():
    return jsonify(cinema.get_movies())

@app.route('/get_movie_seances')
def get_movie_seances():
    movie = request.args.get('movie')
    return jsonify(cinema.get_movie_seances(movie))



@app.route('/movie_seance_booking')
def movie_seance_booking():
    user = request.args.get('user')

    movie = request.args.get('movie')
    seance = request.args.get('seance')
    seats = request.args.get('seats').split(',')
    cinema.booking(user,movie,seance,seats)
    return jsonify('booked')



@app.route('/get_movie_booked_seats')
def get_movie_booked_seats():
    movie = request.args.get('movie')
    seance = request.args.get('seance')
    return jsonify(cinema.get_movie_booked_seats(movie, seance))


@app.route('/get_movie_price')
def get_movie_price():
    movie = request.args.get('movie')
    return jsonify(cinema.get_movie_price(movie))

@app.route('/get_movie_info')
def get_movie_info():
    movie = request.args.get('movie')
    return jsonify(cinema.get_movie_info(movie))


@app.route('/get_seance_profit')
def get_seance_profit():
    movie = request.args.get('movie')
    seance = request.args.get('seance')
    return jsonify(cinema.get_seance_profit(movie, seance))

@app.route('/get_movie_profit')
def get_movie_profit():
    movie = request.args.get('movie')
    return jsonify(cinema.get_movie_profit(movie))

@app.route('/get_movie_seances_count')
def get_movie_infor():
    movie = request.args.get('movie')
    return jsonify(cinema.get_movie_seances_count(movie))

@app.route('/get_movie_people')
def get_movie_people():
    movie = request.args.get('movie')
    return jsonify(cinema.get_movie_people(movie))

@app.route('/get_seance_people')
def get_seance_people():
    movie = request.args.get('movie')
    seance = request.args.get('seance')
    return jsonify(cinema.get_seance_people(movie, seance))



@app.route('/get_user_history')
def get_user_history():
    user = request.args.get('user')
    return jsonify(cinema.get_user_history(user))

@app.route('/get_users_list')
def get_users_list():
    return jsonify(list(users))

@app.route('/get_total_profit')
def get_total_profit():
    return jsonify(cinema.get_total())