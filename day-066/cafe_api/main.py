from dataclasses import dataclass
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


@dataclass
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    random_cafe = db.session.execute(
        db.select(Cafe).order_by(db.sql.func.random()).limit(1)).scalar()

    return jsonify(random_cafe)


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(
        db.select(Cafe).order_by(Cafe.id)).scalars().all()

    return jsonify(all_cafes)


@app.route("/search")
def search_for_cafe():
    location = request.args.get("location")
    location_cafes = db.session.execute(
        db.select(Cafe).where(Cafe.location == location)).scalars().all()

    if len(location_cafes) > 0:
        return jsonify(location_cafes)
    else:
        return jsonify(error={"Not Found": "No cafe found for location."}), 404


@app.route("/add", methods=["POST"])
def add_cafe():
    cafe = Cafe()
    for column in Cafe.__table__.columns:
        name = column.name
        if name == "id":
            continue

        value = request.form.get(name)
        if not value:
            return jsonify(error={"message": f"'{column.name}' missing."}), 404

        if value.lower() in ["true", "false"]:
            setattr(cafe, name, value.lower() == "true")
        else:
            setattr(cafe, name, value)

    try:
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={"Success": f"Cafe '{cafe.name}' was added."})
    except Exception as e:
        return jsonify(error={"message": str(e)}), 500


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.form.get("new_price")
    if not new_price:
        return jsonify(error={"Bad Param": f"Invalid price:{new_price}"}), 500

    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": f"No cafe with id:{cafe_id}"}), 404

    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"Success": f"Price for '{cafe.name}' updated."})


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    del_key = request.args.get("del-key")
    if del_key != "EnterDeleteKeyHere":
        return jsonify(error={"Forbidden": "Operation not allowed."}), 403

    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": f"No cafe with id:{cafe_id}."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"Success": f"'{cafe.name}' was deleted."})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
