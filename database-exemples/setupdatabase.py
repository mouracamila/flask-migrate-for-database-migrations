from basic import db,Cats

db.create_all()

sam = Cats('Sammy',3)
frank = Cats('Frankie',4)

#None
#None
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

db.session.commit()

