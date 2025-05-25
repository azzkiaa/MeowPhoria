from flask import Blueprint, request, jsonify
from services.perawatan_service import tambah_perawatan, get_perawatan_by_user

perawatan_bp = Blueprint('perawatan', __name__)

@perawatan_bp.route('/perawatan', methods=['POST'])
def tambah():
    data = request.json
    perawatan = tambah_perawatan(
        user_id=data['user_id'],
        cat_name=data['cat_name'],
        jenis_perawatan=data['jenis_perawatan']
    )
    return jsonify({"message": "Perawatan ditambahkan", "id": perawatan.id})

@perawatan_bp.route('/perawatan/<int:user_id>', methods=['GET'])
def lihat(user_id):
    hasil = get_perawatan_by_user(user_id)
    return jsonify([{
        "id": p.id,
        "jenis": p.jenis_perawatan,
        "tanggal": p.tanggal.isoformat(),
        "status": p.status
    } for p in hasil])
