from sqlalchemy.orm import joinedload

from Models.DB.Model_for_databases.Contact import Contact


#controller pour le models contact
class ContactController:
    def __init__(self,db):
        self.db = db

    def create_contact(self,data):
        contact = Contact(**data)
        self.db.add(contact)
        self.db.commit()

    def get_all_contacts(self):
        return self.db.query(Contact).options(joinedload(Contact.circuit)).all()

    def get_contact(self,contact_id):
        return self.db.query(Contact).options(joinedload(Contact.circuit)).filter(Contact.id == contact_id).first()

