from flask import request, jsonify

from exceptions.invalid_credentials import InvalidCredentials
from exceptions.mech_unavailable import MechUnavailable
from exceptions.resource_not_found import ResourceNotFound
from Class.Rating import Rating
from Repo.Rating_repo import Ratingrepo
from services.Rating_service import RatingService

rr = Ratingrepo()
rs = RatingService(rr)


def route(app):
    @app.route("/rating", methods=['GET'])
    def get_ratings():
        return jsonify([rating.json() for rating in rs.get_ratings()])

    @app.route("/rating/1/<mech_id>", methods=['GET'])
    def get_all_rating_mech(mech_id):
        # try:
        return jsonify([rating.json() for rating in rs.get_all_rating_mech(mech_id)])
        # except ValueError:
        #     return "Not a valid ID", 400
        # except ResourceNotFound as r:
        #     return r.message, 404

    @app.route("/rating/<r_id>", methods=['GET'])
    def get_rating(r_id):
        try:
            return rs.get_rating(int(r_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/rating", methods=["POST"])
    def post_rating():
        body = request.json

        rating = Rating(user_id=body["userId"], mech_id=body["mechId"], stars=body["stars"], review=body["review"])
        rating = rs.create_rating(rating)

        return rating.json()

    @app.route("/rating/<r_id>", methods=["PUT"])
    def put_rating(r_id):
        body = request.json
        rating = Rating(r_id=r_id, stars=body["stars"], review=body["review"])
        rating = rs.update_rating(rating)

        return rating.json()

    @app.route("/rating/<r_id>", methods=['DELETE'])
    def delete_rating(r_id):
        rs.delete_rating(r_id)
        return '', 204  # No Content
