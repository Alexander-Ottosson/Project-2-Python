from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from Class.Mech import Mech
from Repo.Mech_repo import Mechrepo

# TODO:  create MechService class
from services.mech_service import MechService

mr = Mechrepo()
ms = MechService(mr)


def route(app):
    @app.route("/mech", methods=['GET'])
    def get_all_mechs():
        return jsonify([mech.json() for mech in ms.get_all_Mechs()])

    @app.route("/mech/<id>", methods=['GET'])
    def get_mech(m_id):
        try:
            return ms.get_mech_by_id(int(m_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/mech", methods=["POST"])
    def post_mech():
        body = request.json

        mech = Mech(
            make=body["make"], model=body["model"], year=body["year"], color=body["color"], max_speed=body["max_speed"], weight=body["weight"], height=body["height"], description=body["description"], current_pilot=body["current_pilot"],pilot_count=body["pilot_count"],available=body["available"], confidential=body["confidential"])
        mech = ms.create_mech(mech)

        return mech.json()

    @app.route("/mech/<id>", methods=["PUT"])
    def put_movie(m_id):
        body = request.json
        mech = Mech(m_id=m_id, make=body["make"], model=body["model"], year=body["year"], color=body["color"], max_speed=body["max_speed"], weight=body["weight"], height=body["height"], description=body["description"], current_pilot=body["current_pilot"],pilot_count=body["pilot_count"],available=body["available"], confidential=body["confidential"])
        mech = ms.update_mech(mech)

        return mech.json()

    @app.route("/mech/<m_id>", methods=['DELETE'])
    def delete_mech(m_id):
        ms.delete_mech(m_id)
        return '', 204  # No Content
