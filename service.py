from flask.views import MethodView
from flask import Flask, request, jsonify
from error import HttpError
from Models import Session, Advert


def get_advertisement(id_: int, session: Session):
    """Функция проверяет существует ли объявление в БД по указанному ID"""
    advertisement = session.get(Advert, id_)
    if advertisement is None:
        raise HttpError(404, "Advertisement not found")
    return advertisement


class Advertisement(MethodView):
    def get(self, advertisement_id: int):
        with Session() as session:
            advertisement = get_advertisement(advertisement_id, session)
            return jsonify({
                'id': advertisement.id,
                'heading': advertisement.heading,
                'description': advertisement.description,
                'owner': advertisement.owner,
                'date_create': advertisement.date_creat.isoformat()
            })

    def post(self):
        json_data = request.json
        with Session() as session:
            advertisement = Advert(**json_data)
            session.add(advertisement)
            session.commit()
            return {"id": advertisement.id}

    def delete(self, advertisement_id: int):
        with Session() as session:
            advertisement = get_advertisement(advertisement_id, session)
            session.delete(advertisement)
            session.commit()
            return jsonify({advertisement_id: "Удален из базы"})