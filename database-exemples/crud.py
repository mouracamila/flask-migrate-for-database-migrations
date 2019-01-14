from basic import db, Cats

##CREATE##
my_cat = Cats('Rufus',5)
db.session.add(my_cat)
db.session.commit()

##READ##
all_cats = Cats.query.all() #list of cats objects in the table!
print(all_cats)

#SELECT BY ID
cat_one = Cats.query.get(1)
print(cat_one.name)

#FILTERS
#PRODUCE SOME SQL CODE!
cat_frankie = Cats.query.filter_by(name='Frankie')
print(cat_frankie.all())

is_frankie = Cats.query.get(4)
print(f"Cat {is_frankie.name} is {is_frankie.age} year/s old")


#['Frankie is 3 year old"]

##### UPDATE
first_cat = Cats.query.get(1)
first_cat.age = 10
db.session.add(first_cat)
db.session.commit()

is_sammy = Cats.query.get(1)
print(f"Cat {is_sammy.name} is {is_sammy.age} year/s old")

##### DELETE
# second_cat = Cats.query.get(2)
# db.session.delete(second_cat)
# db.session.commit()

#
all_cats = Cats.query.all()
print(all_cats)