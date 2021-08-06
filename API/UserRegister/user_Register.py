
from API.model import User
from API import db, bcrypt
from flask import request, jsonify


from flask import Blueprint

user_register = Blueprint('user_register', __name__)


@user_register.route('/Registeruser', methods=['POST'])
def add_User():
    try:

        email = request.json['email']
        password = request.json['password']
        Fullname = request.json['Fullname']
        Address = request.json['Address']
        city = request.json['city']
        State = request.json['State']
        Country = request.json['Country']
        Pincode = request.json['Pincode']
        Phone = request.json['Phone']
        print(type(Phone))
        error = None

        if not ((isinstance(Phone, int)) and len(str(Phone)) == 10):
            error = 'Phone number should be 10 digits and should not contain alphabets'
            return jsonify({"error": error})
        if not ((isinstance(Pincode, int)) and len(str(Pincode)) == 6):
            error = 'Pincode should be 6 digit and should not contain alphabets'
            return jsonify({"error": error})
        if(not email or not email.strip() or '@' not in email):
            error = 'please enter a valid email address'
            return jsonify({"error": error})
        if not (len(password) >= 8 and (any(char.isupper() for char in password) or any(char.islower() for char in password))):
            error = 'password should contain minimum 8 characters and an uppercase and lowercase character'
            return jsonify({"error": error})
        if User.query.filter_by(email=email).first():
            return jsonify({"error": f"User with is mail id is already exist '{email}' try with another"})
        else:
            new_student = User(email=email, password=bcrypt.generate_password_hash(password), Fullname=Fullname, Address=Address,
                               city=city, State=State, Country=Country, Pincode=Pincode, Phone=Phone)
            db.session.add(new_student)
            db.session.commit()

            return jsonify({"sucess": "Login with your email and password", "Fullname": new_student.Fullname, "Address": new_student.Address, "city": new_student.city, "State": new_student.State, "Country": new_student.Country, "Pincode": new_student.Pincode}), 201
    except Exception as e:
        a = {"Required": {"email": "email", "password": "password", "Phone": "Phone", "Pincode": "Pincode", "Fullname": "Fullname"},
             "Optional": {"Address": "Address", "city": "City", "State": "State", "Country": "Country"}
             }
        return jsonify(a), 400
