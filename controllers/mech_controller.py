from flask import request, jsonify

from Class.User import User
from exceptions.invalid_credentials import InvalidCredentials
from exceptions.mech_unavailable import MechUnavailable
from exceptions.resource_not_found import ResourceNotFound
from Class.Mech import Mech
from Repo.Mech_repo import Mechrepo

# TODO:  create MechService class
from services.Mech_service import MechServices

mr = Mechrepo()
ms = MechServices(mr)


def route(app):
    @app.route("/mech", methods=['GET'])
    def get_mechs():
        args = request.args

        search_params = dict()

        if 'onlyAvailable' in args:
            search_params['available'] = True
        # make sure a search term was included and not blank
        if 'searchTerm' in args and args['searchTerm']:
            search_params['search_term'] = f"%{args['searchTerm']}%"

        return jsonify([mech.json() for mech in ms.get_mechs(**search_params)])

    @app.route("/mech/<m_id>", methods=['GET'])
    def get_mech(m_id):
        try:
            return ms.get_mech(int(m_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/mech", methods=["POST"])
    def post_mech():
        body = request.json

        mech = Mech(make=body["make"], model=body["model"], year=body["year"], color=body["color"],
                    max_speed=body["maxSpeed"], weight=body["weight"], height=body["height"],
                    des=body["description"], cp=body["currentPilot"], pc=body["pilotCount"], ava=body["available"],
                    con=body["confidential"])
        mech = ms.create_mech(mech)

        return mech.json()

    @app.route("/mech/<m_id>", methods=["PUT"])
    def put_mech(m_id):
        body = request.json
        mech = Mech(m_id=m_id, make=body["make"], model=body["model"], year=body["year"], color=body["color"],
                    max_speed=body["maxSpeed"], weight=body["weight"], height=body["height"], des=body["description"],
                    cp=body["currentPilot"], pc=body["pilotCount"], ava=body["available"], con=body["confidential"])
        mech = ms.update_mech(mech)

        return mech.json()

    @app.route("/mech/checkout/<m_id>", methods=["PATCH"])
    def checkout_mech(m_id):
        # TODO: get user info from a log in feature
        try:
            m_id = int(m_id)
            user = User(u_id=1, username="shinji13", password="password", is_pilot=True, is_admin=False)
            if not user and not user.is_pilot:
                raise InvalidCredentials('You do not have clearance to pilot a mech')

            mech = ms.get_mech(m_id=m_id)

            if not mech.ava:
                raise MechUnavailable('Mech is not available to pilot')

            mech.cp = user.u_id
            mech.ava = False

            ms.update_mech(mech)

        except ValueError as e:
            return 'Please input a proper mech id', 400
        except InvalidCredentials as e:
            return e.message, 403
        except ResourceNotFound as e:
            return e.message, 404

    @app.route("/mech/<m_id>", methods=['DELETE'])
    def delete_mech(m_id):
        ms.delete_mech(m_id)
        return '', 204  # No Content

    @app.route("/1/mech", methods=['GET'])
    def get_mechs_con():
        return jsonify([mech.json() for mech in ms.get_mechs_con()])
