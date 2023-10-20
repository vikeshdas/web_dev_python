from app import app, db
from . import log_bp
from . import logs_bp

from flask.views import MethodView
from flask import jsonify,request


from ..models import Logs ,Consignment

class LogView(MethodView):
    def put(self):
        data = request.get_json()

        try:
            consignment = Consignment.query.get(data.get("con_id"))
            if not consignment:
                return jsonify({'error': 'Consignment with this id does not exist'}),404

            duplicate_log = Logs.query.filter_by(barcode=data.get('barcode')).first()

            if duplicate_log is not None:
                return jsonify({'error': 'Log with this barcode already exists'}),404

            log = Logs(consignment_id=data.get("con_id"), barcode=data.get('barcode'), length=data.get('length'), volume=data.get('volume'))
            db.session.add(log)
            db.session.commit()

            serialized_data = log.log_serializer()
            return jsonify({'message': 'Log inserted successfully', 'data': serialized_data}), 201

        except Exception as e:
            return jsonify({'error': str(e)}),400

    def get(self):
        try:
            data=request.get_json()
            log_id=data.get("id")
            log=Logs.query.filter_by(id=log_id).first()
            if not log:
                return jsonify({'error': 'Log not found'}),404
            serialized_data=log.log_serializer() 
            return jsonify({'message': 'Log inserted successfully', 'data': serialized_data}), 201
        except Exception as e:
            return jsonify({'error': str(e)}),400

class LogsView(MethodView):
    def get(self):
        try:
            data=request.get_json()
            con_id = data.get('con_id')
            consignment_exist=Consignment.query.filter_by(id=con_id).first()
            if not consignment_exist:
                return jsonify({'error': 'consignment with this id  not found'}),404
            
            logs = Logs.query.filter_by(consignment_id=con_id).all()
            serialized_data = [log.log_serializer() for log in logs]
            return jsonify({'data': serialized_data}), 201
        
        except Exception as e:
            return jsonify({'error': str(e)}),400

        
logs_bp.add_url_rule('/log_list', view_func=LogsView.as_view('log_list_'))        
log_bp.add_url_rule('/log', view_func=LogView.as_view('log_'))

