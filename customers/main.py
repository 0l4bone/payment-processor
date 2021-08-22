import database
from models import Customer

def run():
    arroz = Customer('Anee')
    db.session.add(arroz)
    print(arroz.id)
    agua = Customer('Andre')
    db.session.add(agua)
    db.session.commit()
    print(arroz.id)


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()