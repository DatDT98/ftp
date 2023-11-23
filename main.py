from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Datdat98@localhost/postgres'
db = SQLAlchemy(app)


class Units(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    capital = db.Column(db.Integer, nullable=False)


class FTP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_capital = db.Column(db.Integer, nullable=False)


# Route để lấy dữ liệu từ cơ sở dữ liệu
@app.route('/')
def index():
    units = Units.query.all()
    ftp = FTP.query.first()
    return render_template('index.html', units=units, ftp=ftp)


# Route để cập nhật dữ liệu
@app.route('/update_capital', methods=['POST'])
def update_capital():
    data = request.get_json()
    unit_id = data['unit_id']
    new_capital = data['new_capital']

    unit = Units.query.get(unit_id)
    unit.capital = new_capital
    db.session.commit()

    return jsonify({'success': True})

@app.route('/add_unit', methods=['POST'])
def add_unit():
    data = request.get_json()
    new_unit = Units(name=data['name'], capital=data['capital'])
    db.session.add(new_unit)
    db.session.commit()

    return jsonify({'success': True})
# Thêm dữ liệu giả vào cơ sở dữ liệu
# Thêm dữ liệu giả vào cơ sở dữ liệu
# def add_fake_data():
#     with app.app_context():
#         # Thêm đơn vị
#         unit_names = ["Đơn vị Cho Vay", "Đơn vị Tiền Gửi", "Đơn vị Kinh Doanh"]
#         unit_capitals = [100000, 150000, 200000]
#
#         for name, capital in zip(unit_names, unit_capitals):
#             new_unit = Units(name=name, capital=capital)
#             db.session.add(new_unit)
#
#         # Thêm dữ liệu FTP
#         ftp_data = {"total_capital": 500000}
#         new_ftp = FTP(**ftp_data)
#         db.session.add(new_ftp)
#
#         # Lưu thay đổi vào cơ sở dữ liệu
#         db.session.commit()

# Route để thêm đơn vị mới từ API
@app.route('/add_unit_api', methods=['POST'])
def add_unit_api():
    data = request.get_json()
    new_unit = Units(name=data['name'], capital=data['capital'])
    db.session.add(new_unit)
    db.session.commit()

    return jsonify({'success': True})

# Route để thêm giá trị vào FTP từ API
@app.route('/update_ftp_api', methods=['POST'])
def update_ftp_api():
    data = request.get_json()
    new_ftp_value = data['new_ftp_value']

    ftp = FTP.query.first()
    ftp.total_capital = new_ftp_value
    db.session.commit()

    return jsonify({'success': True})
if __name__ == '__main__':
    # db.create_all()

    # add_fake_data()

    app.run(debug=True)
