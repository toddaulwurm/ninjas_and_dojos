from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        results = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)

        return results 

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninja_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))

        return dojos

    @classmethod
    def dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"

        results = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)

        dojo = cls(results[0])

        for row in results:
            ninja_data = {
                "id" : row["ninjas.id"],
                "dojo_id" : row["dojo_id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo
        


