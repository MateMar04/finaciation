# Generated by Django 4.2.1 on 2023-08-20 01:04

from django.db import migrations


class Migration(migrations.Migration):
    operations = [
        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_role\" (name, description)"
            "VALUES ('Referente', 'El rol de referente es aquel que constestara las consultas que no puedan los Asesores'),"
            "('Secretario/a', 'El rol de secretario/a es el encargado de agendar visitas y proveer informacion sobre ella'),"
            "('Administrador', 'Este rol es capaz de hacer cualquier cosa en el sistema')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_division\" (name, description)"
            "VALUES ('Rentas Cordoba', 'Direccion General de Rentas de la Provincia de Cordoba'),"
            "('Registro Civil', 'Registro Civil'),"
            "('Catastro', 'Datos de inmuebles'),"
            "('Caja de Jubilaciones', 'Caja de Jubilaciones, Pensiones y Retiros de la Provincia de Córdoba'),"
            "('CiDi', 'Ciudadano Digital'),"
            "('IPJ', 'Inspecion de Personas Juridicas'),"
            "('Registro de la Propiedad', 'Registro de la Propiedad'),"
            "('Otros', 'Otros')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_faq\" (name, division_id)"
            "VALUES ('Impresión Cedulón 2023', 1),"
            "('Asesoramiento de gestiones online (Rentas)', 1),"
            "('Asesoramiento de gestiones online (Registro Civil)', 2),"
            "('Asesoramiento de gestiones online (Catastro)', 3),"
            "('Asesoramiento de gestiones online (Caja de Jubilaciones)', 4),"
            "('Asesoramiento de gestiones online (IPJ)', 6),"
            "('Asesoramiento de gestiones online (Registro de la Propiedad)', 7),"
            "('Consulta y regularización de deuda', 1),"
            "('Pago online con tarjetas de débito y crédito', 1),"
            "('Adhesión a débito automático', 1),"
            "('Consulta de extenciones impositivas', 1),"
            "('Tramite de DNI y Pasaporte', 2),"
            "('Inicio de tramite de partidas de nacimiento y matrimonio', 2),"
            "('Jubilaciones o pensiones', 4),"
            "('Futuros beneficiarios', 4),"
            "('Subsidios por fallecimiento o seguros', 4),"
            "('Historia Laboral', 4),"
            "('Creacion de cuentas de Ciudadano Digital Nivel 2', 5),"
            "('Recuperacion de cuentas', 5),"
            "('Actualizacion de mails', 5),"
            "('Inscripcion de vivienda como Bien de Familia', 7),"
            "('Sociedades, Asociaciones Civiles y Fundaciones', 6),"
            "('Otros (Rentas)', 1),"
            "('Otros (Registro Civil)', 2),"
            "('Otros (Catastro)', 3),"
            "('Otros (Caja de Jubilaciones)', 4),"
            "('Otros (CiDi)', 5),"
            "('Otros (IPJ)', 6),"
            "('Otros (Registro de la Propiedad)', 7),"
            "('Otros', 8)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_why\" (name)"
            "VALUES ('No conoce los cales de atencion habilitados'),"
            "('No logro realizar la gestion via web/online'),"
            "('No dispone de acceso a tecnologia/internet'),"
            "('Prefiere atencion presencial')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_visitstatus\" (name, description)"
            "VALUES ('No Confirmada', 'La visita no se confirmo todavia'),"
            "('Pendiente', 'La visita esta confirmada pero todavia no se realizo'),"
            "('En proceso', 'La visita esta siendo realizada'),"
            "('Finalizada', 'La visita se realizo')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_requeststatus\" (name, description)"
            "VALUES ('Resuelta', 'La consulta ha sido resuelta'),"
            "('No resuelta', 'La consulta ni ha sido resuelta'),"
            "('Pendiente', 'La consulta esta en proceso')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_userstatus\" (name, description)"
            "VALUES ('Disponible', 'El usuario esta disponile para una visita'),"
            "('Ocupado', 'El usuario no esta disponible')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_address\" (street, number)"
            "VALUES ('Loncoche', 8136),"
            "('Hualil', 1880),"
            "('Hilario Ascasubi', 330),"
            "('Garden Grove', 123),"
            "('Sunset Boulevard', 456),"
            "('Maple Avenue', 789),"
            "('Oak Street', 1011),"
            "('River Road', 1213),"
            "('Willow Lane', 1415),"
            "('Meadow Lane', 1617),"
            "('Springfield Drive', 1819),"
            "('Pine Street', 2021),"
            "('Cedar Avenue', 2223),"
            "('Lakeside Drive', 2425),"
            "('Cherry Street', 2627),"
            "('Hillcrest Avenue', 2829),"
            "('Birch Lane', 3031),"
            "('Riverside Drive', 3233),"
            "('Forest Street', 3435),"
            "('Meadowbrook Road', 3637),"
            "('Creek Road', 3839),"
            "('Pleasant Avenue', 4041),"
            "('Elm Street', 4243),"
            "('Lakeview Drive', 4445),"
            "('Sycamore Lane', 4647),"
            "('Hickory Street', 4849),"
            "('River Street', 5051),"
            "('Valley Road', 5253),"
            "('Rosewood Avenue', 5455),"
            "('Sunrise Court', 5657),"
            "('Main Street', 5859),"
            "('Harbor Drive', 6061),"
            "('Cypress Lane', 6263),"
            "('Mountain View', 6465),"
            "('Grove Avenue', 6667),"
            "('Laurel Lane', 6869),"
            "('Highland Avenue', 7071),"
            "('Oakwood Court', 7273),"
            "('Meadow Street', 7475),"
            "('Hillside Drive', 7677),"
            "('Chestnut Street', 7879),"
            "('Riverfront', 8081),"
            "('Forest Lane', 8283),"
            "('Sunset Court', 8485),"
            "('Winding Road', 8687),"
            "('Lake Avenue', 8889),"
            "('Holly Lane', 9091),"
            "('Linden Street', 9293),"
            "('Greenwood Avenue', 9495),"
            "('Cherry Lane', 9697),"
            "('Pine Lane', 9899)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_agreement\" (name, description) "
            "VALUES ('IAU', 'IAU'), "
            "('MUC', 'MUC')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_contactedreferrer\" (first_name, last_name, position) "
            "VALUES ('John', 'Doe', 'Manager'),"
            "('Jane', 'Smith', 'Analyst'),"
            "('Michael', 'Johnson', 'Director'),"
            "('Emily', 'Williams', 'Associate'),"
            "('David', 'Brown', 'Assistant Manager'),"
            "('Sarah', 'Jones', 'Coordinator'),"
            "('Robert', 'Miller', 'Consultant'),"
            "('Jessica', 'Davis', 'Executive'),"
            "('William', 'Garcia', 'Supervisor'),"
            "('Amanda', 'Rodriguez', 'Specialist'),"
            "('James', 'Martinez', 'Administrator'),"
            "('Linda', 'Lopez', 'Team Lead'),"
            "('Daniel', 'Perez', 'Manager'),"
            "('Michelle', 'Wilson', 'Analyst'),"
            "('Christopher', 'Taylor', 'Director'),"
            "('Karen', 'Anderson', 'Associate'),"
            "('Matthew', 'Thomas', 'Assistant Manager'),"
            "('Patricia', 'Moore', 'Coordinator'),"
            "('Jennifer', 'Jackson', 'Consultant'),"
            "('Richard', 'Harris', 'Executive'),"
            "('Elizabeth', 'Clark', 'Supervisor'),"
            "('Joseph', 'Young', 'Specialist'),"
            "('Mary', 'Lee', 'Administrator'),"
            "('Thomas', 'Martin', 'Team Lead'),"
            "('Lisa', 'Walker', 'Manager'),"
            "('Charles', 'Hall', 'Analyst'),"
            "('Nancy', 'Allen', 'Director'),"
            "('Andrew', 'King', 'Associate'),"
            "('Maria', 'Wright', 'Assistant Manager'),"
            "('Brian', 'Scott', 'Coordinator'),"
            "('Susan', 'Green', 'Consultant'),"
            "('Kevin', 'Baker', 'Executive'),"
            "('Margaret', 'Adams', 'Supervisor'),"
            "('Paul', 'Nelson', 'Specialist'),"
            "('Ashley', 'Hill', 'Administrator'),"
            "('Donald', 'Rivera', 'Team Lead'),"
            "('Dorothy', 'Mitchell', 'Manager'),"
            "('Steven', 'White', 'Analyst'),"
            "('Helen', 'Carter', 'Director'),"
            "('Mark', 'Turner', 'Associate'),"
            "('Barbara', 'Harris', 'Assistant Manager'),"
            "('George', 'Lewis', 'Coordinator'),"
            "('Betty', 'Robinson', 'Consultant'),"
            "('Edward', 'Parker', 'Executive'),"
            "('Sandra', 'Cooper', 'Supervisor'),"
            "('Kenneth', 'Peterson', 'Specialist'),"
            "('Deborah', 'Morris', 'Administrator'),"
            "('Ronald', 'Reed', 'Team Lead'),"
            "('Kimberly', 'Cook', 'Manager'),"
            "('Gary', 'Morgan', 'Analyst'),"
            "('Sharon', 'Murphy', 'Director')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_contactedreferreremail\" (mail, contacted_referrer_id)"
            "VALUES ('y.ribone@gmail.com', 1),"
            "('l.ribone@gmail.com', 2),"
            "('e.ribone@gmail.com', 3),"
            "('john.smith@example.com', 1),"
            "('emily.johnson@example.com', 2),"
            "('michael.williams@example.com', 3),"
            "('emma.jones@example.com', 4),"
            "('james.brown@example.com', 5),"
            "('olivia.davis@example.com', 6),"
            "('william.miller@example.com', 7),"
            "('ava.wilson@example.com', 8),"
            "('alexander.taylor@example.com', 9),"
            "('sophia.anderson@example.com', 10),"
            "('benjamin.thomas@example.com', 11),"
            "('isabella.martinez@example.com', 12),"
            "('elijah.hernandez@example.com', 13),"
            "('charlotte.lopez@example.com', 14),"
            "('daniel.gonzalez@example.com', 15),"
            "('mia.moore@example.com', 16),"
            "('logan.jackson@example.com', 17),"
            "('amelia.garcia@example.com', 18),"
            "('lucas.martin@example.com', 19),"
            "('harper.rodriguez@example.com', 20),"
            "('jackson.martinez@example.com', 21),"
            "('ella.hernandez@example.com', 22),"
            "('aiden.lopez@example.com', 23),"
            "('scarlett.gonzalez@example.com', 24),"
            "('matthew.lewis@example.com', 25),"
            "('luna.lee@example.com', 26),"
            "('oliver.walker@example.com', 27),"
            "('chloe.perez@example.com', 28),"
            "('samuel.hall@example.com', 29),"
            "('avery.young@example.com', 30),"
            "('daniel.allen@example.com', 31),"
            "('abigail.sanchez@example.com', 32),"
            "('joseph.wright@example.com', 33),"
            "('sofia.king@example.com', 34),"
            "('alexander.scott@example.com', 35),"
            "('grace.torres@example.com', 36),"
            "('ethan.nguyen@example.com', 37),"
            "('lily.hill@example.com', 38),"
            "('christopher.flores@example.com', 39),"
            "('hazel.green@example.com', 40),"
            "('david.adams@example.com', 41),"
            "('ella.baker@example.com', 42),"
            "('michael.hill@example.com', 43),"
            "('nora.coleman@example.com', 44),"
            "('ryan.rogers@example.com', 45),"
            "('aria.gomez@example.com', 46),"
            "('isaac.reed@example.com', 47),"
            "('penelope.wood@example.com', 48),"
            "('leo.brooks@example.com', 49),"
            "('elizabeth.long@example.com', 50)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_contactedreferrerphone\" (phone_number, contacted_referrer_id)"
            "VALUES (3511111111, 1),"
            "(3512222222, 2),"
            "(3513333333, 3),"
            "(1234567890, 1),"
            "(9876543210, 2),"
            "(5555555555, 3),"
            "(1111111111, 4),"
            "(9999999999, 5),"
            "(4444444444, 6),"
            "(8888888888, 7),"
            "(7777777777, 8),"
            "(6666666666, 9),"
            "(2222222222, 10),"
            "(3333333333, 11),"
            "(8888777766, 12),"
            "(1122334455, 13),"
            "(9988776655, 14),"
            "(6677889900, 15),"
            "(9999888877, 16),"
            "(4444555566, 17),"
            "(3333444455, 18),"
            "(7777666677, 19),"
            "(2222111133, 20),"
            "(8888222288, 21),"
            "(1111222233, 22),"
            "(7777888811, 23),"
            "(4444333322, 24),"
            "(5555666677, 25),"
            "(7777444455, 26),"
            "(9999111122, 27),"
            "(2222444433, 28),"
            "(6666555599, 29),"
            "(3333999988, 30),"
            "(8888999977, 31),"
            "(6666777766, 32),"
            "(4444111199, 33),"
            "(2222888899, 34),"
            "(9999222211, 35),"
            "(5555444499, 36),"
            "(7777111133, 37),"
            "(6666333399, 38),"
            "(8888444411, 39),"
            "(1111999999, 40),"
            "(6666111122, 41),"
            "(2222777788, 42),"
            "(4444888899, 43),"
            "(7777333311, 44),"
            "(5555222299, 45),"
            "(3333999999, 46),"
            "(8888777788, 47),"
            "(6666555566, 48),"
            "(2222444422, 49),"
            "(7777444433, 50)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_mayor\" (first_name, last_name, location_id)"
            "VALUES ('Martin', 'Llaryora', 1),"
            "('Horacio', 'Larreta', 2),"
            "('Juan', 'Schiaretti', 3),"
            "('Eleanor', 'Windsor', 4),"
            "('Maxwell', 'Evergreen', 5),"
            "('Victoria', 'Silverstone', 6),"
            "('Oliver', 'Hartford', 7),"
            "('Isabella', 'Harrington', 8),"
            "('Lucas', 'Montgomery', 9),"
            "('Penelope', 'Whitaker', 10),"
            "('Sebastian', 'Fitzgerald', 11),"
            "('Amelia', 'Sinclair', 12),"
            "('Henry', 'Wellington', 13),"
            "('Charlotte', 'Blackwood', 14),"
            "('Benjamin', 'Pembroke', 15),"
            "('Sophia', 'Winthrop', 16),"
            "('Alexander', 'Cunningham', 17),"
            "('Grace', 'Hawthorne', 18),"
            "('William', 'Montague', 19),"
            "('Emma', 'Beaumont', 20),"
            "('James', 'Arlington', 21),"
            "('Madeline', 'Pendleton', 22),"
            "('Liam', 'Channing', 23),"
            "('Ava', 'Hollister', 24),"
            "('Elijah', 'Langley', 25),"
            "('Lillian', 'Fitzroy', 26),"
            "('Jackson', 'Fairchild', 27),"
            "('Evelyn', 'Waverly', 28),"
            "('Michael', 'Kensington', 29),"
            "('Olivia', 'Ashford', 30),"
            "('Andrew', 'Harrington', 31),"
            "('Abigail', 'Preston', 32),"
            "('Daniel', 'Blackwell', 33),"
            "('Emily', 'Kingsley', 34),"
            "('Matthew', 'Hathaway', 35),"
            "('Scarlett', 'Stanford', 36),"
            "('Joseph', 'Langdon', 37),"
            "('Samantha', 'Kensington', 38),"
            "('Christopher', 'Sutton', 39),"
            "('Isabelle', 'Westerly', 40),"
            "('Anthony', 'Hartwell', 41),"
            "('Hannah', 'Fairfax', 42),"
            "('David', 'Ainsworth', 43),"
            "('Grace', 'Pennington', 44),"
            "('John', 'Hamilton', 45),"
            "('Elizabeth', 'Monroe', 46),"
            "('Nicholas', 'Chadwick', 47),"
            "('Avery', 'Crawford', 48),"
            "('Andrew', 'Weston', 49),"
            "('Anna', 'Hawthorne', 50),"
            "('Samuel', 'Pembroke', 51),"
            "('Aria', 'Prescott', 52)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_mayoremail\" (mail, mayor_id)"
            "VALUES ('m.llaryora@gmail.com', 1),"
            "('j.schiaretti@gmail.com', 2),"
            "('h.larreta@gmail.com', 3),"
            "('john.smith@example.com', 1),"
            "('emily.johnson@example.com', 2),"
            "('michael.williams@example.com', 3),"
            "('emma.jones@example.com', 4),"
            "('james.brown@example.com', 5),"
            "('olivia.davis@example.com', 6),"
            "('william.miller@example.com', 7),"
            "('ava.wilson@example.com', 8),"
            "('alexander.taylor@example.com', 9),"
            "('sophia.anderson@example.com', 10),"
            "('benjamin.thomas@example.com', 11),"
            "('isabella.martinez@example.com', 12),"
            "('elijah.hernandez@example.com', 13),"
            "('charlotte.lopez@example.com', 14),"
            "('daniel.gonzalez@example.com', 15),"
            "('mia.moore@example.com', 16),"
            "('logan.jackson@example.com', 17),"
            "('amelia.garcia@example.com', 18),"
            "('lucas.martin@example.com', 19),"
            "('harper.rodriguez@example.com', 20),"
            "('jackson.martinez@example.com', 21),"
            "('ella.hernandez@example.com', 22),"
            "('aiden.lopez@example.com', 23),"
            "('scarlett.gonzalez@example.com', 24),"
            "('matthew.lewis@example.com', 25),"
            "('luna.lee@example.com', 26),"
            "('oliver.walker@example.com', 27),"
            "('chloe.perez@example.com', 28),"
            "('samuel.hall@example.com', 29),"
            "('avery.young@example.com', 30),"
            "('daniel.allen@example.com', 31),"
            "('abigail.sanchez@example.com', 32),"
            "('joseph.wright@example.com', 33),"
            "('sofia.king@example.com', 34),"
            "('alexander.scott@example.com', 35),"
            "('grace.torres@example.com', 36),"
            "('ethan.nguyen@example.com', 37),"
            "('lily.hill@example.com', 38),"
            "('christopher.flores@example.com', 39),"
            "('hazel.green@example.com', 40),"
            "('david.adams@example.com', 41),"
            "('ella.baker@example.com', 42),"
            "('michael.hill@example.com', 43),"
            "('nora.coleman@example.com', 44),"
            "('ryan.rogers@example.com', 45),"
            "('aria.gomez@example.com', 46),"
            "('isaac.reed@example.com', 47),"
            "('penelope.wood@example.com', 48),"
            "('leo.brooks@example.com', 49),"
            "('elizabeth.long@example.com', 50)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_mayorphone\" (phone_number, mayor_id)"
            "VALUES (3514444444, 1),"
            "(3515555555, 2),"
            "(3516666666, 3),"
            "(1234567890, 1),"
            "(9876543210, 2),"
            "(5555555555, 3),"
            "(1111111111, 4),"
            "(9999999999, 5),"
            "(4444444444, 6),"
            "(8888888888, 7),"
            "(7777777777, 8),"
            "(6666666666, 9),"
            "(2222222222, 10),"
            "(3333333333, 11),"
            "(8888777766, 12),"
            "(1122334455, 13),"
            "(9988776655, 14),"
            "(6677889900, 15),"
            "(9999888877, 16),"
            "(4444555566, 17),"
            "(3333444455, 18),"
            "(7777666677, 19),"
            "(2222111133, 20),"
            "(8888222288, 21),"
            "(1111222233, 22),"
            "(7777888811, 23),"
            "(4444333322, 24),"
            "(5555666677, 25),"
            "(7777444455, 26),"
            "(9999111122, 27),"
            "(2222444433, 28),"
            "(6666555599, 29),"
            "(3333999988, 30),"
            "(8888999977, 31),"
            "(6666777766, 32),"
            "(4444111199, 33),"
            "(2222888899, 34),"
            "(9999222211, 35),"
            "(5555444499, 36),"
            "(7777111133, 37),"
            "(6666333399, 38),"
            "(8888444411, 39),"
            "(1111999999, 40),"
            "(6666111122, 41),"
            "(2222777788, 42),"
            "(4444888899, 43),"
            "(7777333311, 44),"
            "(5555222299, 45),"
            "(3333999999, 46),"
            "(8888777788, 47),"
            "(6666555566, 48),"
            "(2222444422, 49),"
            "(7777444433, 50)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_politicparty\" (name, description)"
            "VALUES ('UCR', 'UCR'),"
            "('HPC', 'HPC'),"
            "('VECINAL', 'VECINAL')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_group\" (name)"
            "VALUES ('Grupo 1'),"
            "('Grupo 2'),"
            "('Grupo 3')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_vehiclebrand\" (name)"
            "VALUES ('Stellar Motors'),"
            "('Lunar Wheels'),"
            "('Cosmic Carriage'),"
            "('Celestial Motors'),"
            "('Astral Auto'),"
            "('Supernova Vehicles'),"
            "('Galactic Gears'),"
            "('Eclipse Motors'),"
            "('Nebula Wheels'),"
            "('Starlight Autos'),"
            "('Infinity Rides'),"
            "('Solar Drive'),"
            "('Metropolis Motors'),"
            "('Nova Automobiles'),"
            "('Orion Wheels'),"
            "('Astro Cars'),"
            "('Voyager Motors'),"
            "('Cosmos Auto'),"
            "('Zenith Wheels'),"
            "('Moonbeam Motors'),"
            "('Solstice Vehicles'),"
            "('Aurora Autos'),"
            "('Comet Rides'),"
            "('Astute Motors'),"
            "('Horizon Wheels'),"
            "('Luminous Cars'),"
            "('Jupiter Motors'),"
            "('Eclipse Autos'),"
            "('Galaxy Wheels'),"
            "('Lunar Drive'),"
            "('Zenith Rides'),"
            "('Meteor Motors'),"
            "('Nimbus Wheels'),"
            "('Stardust Autos'),"
            "('Celestial Drive'),"
            "('Aurora Wheels'),"
            "('Stellar Autos'),"
            "('Spectrum Motors'),"
            "('Nebula Drive'),"
            "('Moonlight Wheels'),"
            "('Supernova Autos'),"
            "('Galactic Drive'),"
            "('Solar Wheels'),"
            "('Astro Autos'),"
            "('Voyager Drive'),"
            "('Comet Wheels'),"
            "('Horizon Autos'),"
            "('Nova Drive'),"
            "('Luminous Wheels')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_vehiclemodel\" (name, brand_id)"
            "VALUES ('Stellar Sedan', 1),"
            "('Lunar Cruiser', 2),"
            "('Cosmic Compact', 3),"
            "('Celestial Convertible', 4),"
            "('Astral SUV', 5),"
            "('Supernova Sports', 6),"
            "('Galactic Hatchback', 7),"
            "('Eclipse Electric', 8),"
            "('Nebula Minivan', 9),"
            "('Starlight Roadster', 10),"
            "('Infinity Hybrid', 11),"
            "('Solar Pickup', 12),"
            "('Metropolis Luxury', 13),"
            "('Nova Off-Road', 14),"
            "('Orion Coupe', 15),"
            "('Astro Van', 16),"
            "('Voyager Wagon', 17),"
            "('Cosmos Crossover', 18),"
            "('Zenith Truck', 19),"
            "('Moonbeam Micro', 20),"
            "('Solstice Super', 21),"
            "('Aurora All-Terrain', 22),"
            "('Comet Classic', 23),"
            "('Astute Performance', 24),"
            "('Horizon Hybrid', 25),"
            "('Luminous Limousine', 26),"
            "('Jupiter Jet', 27),"
            "('Eclipse Eco', 28),"
            "('Galaxy Grand', 29),"
            "('Lunar Luxury', 2),"
            "('Zenith Zephyr', 19),"
            "('Meteor Midsize', 30),"
            "('Nimbus Navigator', 9),"
            "('Stardust Subcompact', 31),"
            "('Celestial Cruiser', 4),"
            "('Aurora Alphine', 22),"
            "('Stellar Streamline', 1),"
            "('Spectrum Sports', 32),"
            "('Nebula Navigator', 9),"
            "('Moonlight Monarch', 20),"
            "('Supernova Speedster', 6),"
            "('Galactic Glide', 7),"
            "('Solar Supremacy', 12),"
            "('Astro Attitude', 16),"
            "('Voyager Venture', 17),"
            "('Comet Commuter', 23),"
            "('Horizon Hiker', 25),"
            "('Nova Navigator', 14),"
            "('Luminous Luxury', 26)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_vehicleplate\" (plate)"
            "VALUES ('ABC1234'),"
            "('XYZ5678'),"
            "('QWE8901'),"
            "('JKL2345'),"
            "('MNO6789'),"
            "('RST0123'),"
            "('UVW4567'),"
            "('PQR8901'),"
            "('DEF2345'),"
            "('GHI6789'),"
            "('LMN0123'),"
            "('STU4567'),"
            "('VWX8901'),"
            "('YZA2345'),"
            "('BCD6789'),"
            "('EFG0123'),"
            "('HIJ4567'),"
            "('KLM8901'),"
            "('NOP2345'),"
            "('QRS6789'),"
            "('TUV0123'),"
            "('WXY4567'),"
            "('ZAB8901'),"
            "('CDE2345'),"
            "('FGH6789'),"
            "('IJK0123'),"
            "('LMN4567'),"
            "('OPQ8901'),"
            "('RST2345'),"
            "('UVW6789'),"
            "('PQR0123'),"
            "('DEF4567'),"
            "('GHI8901'),"
            "('JKL2345'),"
            "('MNO6789'),"
            "('RST0123'),"
            "('UVW4567'),"
            "('PQR8901'),"
            "('DEF2345'),"
            "('GHI6789'),"
            "('LMN0123'),"
            "('STU4567'),"
            "('VWX8901'),"
            "('YZA2345'),"
            "('BCD6789'),"
            "('EFG0123'),"
            "('HIJ4567'),"
            "('KLM8901')"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_vehicle\" (plate_id, brand_id, model_id)"
            "VALUES (1, 1, 1),"
            "(2, 2, 2),"
            "(3, 3, 3),"
            "(4, 4, 4),"
            "(5, 5, 5),"
            "(6, 6, 6),"
            "(7, 7, 7),"
            "(8, 8, 8),"
            "(9, 9, 9),"
            "(10, 10, 10),"
            "(11, 11, 11),"
            "(12, 12, 12),"
            "(13, 13, 13),"
            "(14, 14, 14),"
            "(15, 15, 15),"
            "(16, 16, 16),"
            "(17, 17, 17),"
            "(18, 18, 18),"
            "(19, 19, 19),"
            "(20, 20, 20),"
            "(21, 21, 21),"
            "(22, 22, 22),"
            "(23, 23, 23),"
            "(24, 24, 24),"
            "(25, 25, 25),"
            "(26, 26, 26),"
            "(27, 27, 27),"
            "(28, 28, 28),"
            "(29, 29, 29),"
            "(30, 30, 30),"
            "(31, 31, 31),"
            "(32, 32, 32),"
            "(33, 33, 33),"
            "(34, 34, 34),"
            "(35, 35, 35),"
            "(36, 36, 36),"
            "(37, 37, 37),"
            "(38, 38, 38),"
            "(39, 39, 39),"
            "(40, 40, 40),"
            "(41, 41, 41),"
            "(42, 42, 42),"
            "(43, 43, 43),"
            "(44, 44, 44),"
            "(45, 45, 45),"
            "(46, 46, 46),"
            "(47, 47, 47),"
            "(48, 48, 48),"
            "(48, 47, 46),"
            "(46, 47, 48)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_useraccount\" (password, last_login, ssn, email, first_name, last_name, is_staff, is_active,"
            "is_superuser, phone_number, profile_picture, role_id, user_status_id)"
            "VALUES ('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344730, 'mateo.marchisone@gmail.com', 'Mateo', 'Marchisone', true, true, true, 3513497968, 'adada', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20456934987, 'julymaxrosas@gmail.com', 'Julian', 'Rosas', true, true, true, 3512071828, 'adada', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20464505149, 'lorenzo.galaverna1@gmail.com', 'Lorenzo', 'Galaverna', true, true, true, 3517725070, 'adada', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20454866798, 'tomimartiarena@gmail.com', 'Tomas', 'Martiarena', true, true, true, 3513133171, 'adada', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20458334537, 'tade6funes@gmail.com', 'Tadeo', 'Funes', true, true, true, 3515303037, 'adada', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20463085626, 'sinchesmateo@gmail.com', 'Mateo', 'Sinches', true, true, true, 3517580012, 'adada', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20460322694, 'lautivelez28@gmail.com', 'Lautaro', 'Velez', true, true, true, 3512753717, 'adada', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344737, 'mateo.marchisone+8@gmail.com', 'Paulo', 'Londra', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344738, 'mateo.marchisone+9@gmail.com', 'Mauro', 'Lombardo', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344739, 'mateo.marchisone+10@gmail.com', 'Mauro Roman', 'Monzon', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344740, 'mateo.marchisone+11@gmail.com', 'Ivo Alfredo Thomas', 'Serue', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344741, 'mateo.marchisone+12@gmail.com', 'Tomas Manuel', 'Campos', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344742, 'mateo.marchisone+13@gmail.com', 'Valentin', 'Oliva', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344743, 'mateo.marchisone+14@gmail.com', 'Sebastian', 'Chinellato', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344744, 'mateo.marchisone+15@gmail.com', 'Alejo Nahuel', 'Acosta', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344745, 'mateo.marchisone+16@gmail.com', 'Gonzalo Julian', 'Conde', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344746, 'mateo.marchisone+17@gmail.com', 'Indra', 'Bhalavan', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344747, 'mateo.marchisone+18@gmail.com', 'Ignacio Matias', 'Spallati', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344748, 'mateo.marchisone+19@gmail.com', 'Dylan Leon', 'Masa', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344749, 'mateo.marchisone+20@gmail.com', 'Mateo', 'Palacios Corazzina', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344750, 'mateo.marchisone+21@gmail.com', 'Joaquin', 'Cordovero', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344751, 'mateo.marchisone+22@gmail.com', 'Agustin', 'Zeballos', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344752, 'mateo.marchisone+23@gmail.com', 'Benito Antonio', 'Martínez Ocasio', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344753, 'mateo.marchisone+24@gmail.com', 'Juan Facundo', 'Almenara Ordóñez', true, true, true, 3513497968, 'adsads', 1, 1),"
            "('pbkdf2_sha256$600000$Pi72o55AT3cB2zYs5anZIU$ncyZnnXqcejNOEJlGw5KASb2u54WN74e95Z7bGggUnA=', current_timestamp,"
            "20459344754, 'mateo.marchisone+25@gmail.com', 'Enzo', 'Sauthier', true, true, true, 3513497968, 'adsads', 1, 1)"),

        migrations.RunSQL("INSERT INTO \"financiationAPI_coordinator\" (group_id, user_id)"
                          "VALUES (1, 1),"
                          "(1, 2),"
                          "(2, 3),"
                          "(2, 4),"
                          "(3, 5),"
                          "(3, 6)"),

        migrations.RunSQL("INSERT INTO \"financiationAPI_advisor\" (group_id, user_id)"
                          "VALUES (1, 7),"
                          "(1, 8),"
                          "(1, 9),"
                          "(2, 10),"
                          "(2, 11),"
                          "(2, 12),"
                          "(3, 13),"
                          "(3, 14),"
                          "(3, 15)"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_visit\" (visit_date, start_time, finish_time, flyer, rent_observations, "
            "distance, travel_time, civil_registration, place_name, accommodation, modernization_fund, "
            "address_id, contacted_referrer_id, group_id, mayor_id, "
            "politic_party_id, visit_status_id, location_id) "
            "SELECT tabla_1.*, tabla_2.id as location_id "
            "FROM ("
            "SELECT cast(visit_stamp as date)                       as visit_date, "
            "cast(visit_stamp as time)                       as start_time, "
            "cast(visit_stamp as time) + interval '1 hour'   as finish_time, "
            "mod(extract(MINUTE FROM visit_stamp), 2) = 1    as flyer, "
            "(SELECT 'observation: ' || "
            "string_agg(substring('abcdefghijklmnopqrstuvwxyz', round(random() * 26)::integer, 1), '') "
            "FROM generate_series(1, 9))                    as rent_observation, "
            "cast(random() * 300 as int)                     as distance, "
            "1 as travel_time, "
            "mod(extract(MINUTE FROM visit_stamp), 2) = 1    as civil_registration, "
            "(SELECT 'place: ' || "
            "string_agg(substring('abcdefghijklmnopqrstuvwxyz', round(random() * 26)::integer, 1), '') "
            "FROM generate_series(1, 20))                   as place_name, "
            "mod(extract(MINUTE FROM visit_stamp), 2) = 1    as accommodation, "
            "mod(extract(MINUTE FROM visit_stamp), 3) = 1    as modernization_fund, "
            "address_id, "
            "contacted_refferer_id, "
            "group_id, "
            "mayor_id, "
            "politic_party_id, "
            "visit_status_id "
            "FROM ( "
            "SELECT current_date + interval '1 hour' * (row_number() "
            "over (order by A.id, CF.id, G.id, M.id, PP.id, VS.id) / "
            "24.00) as visit_stamp, "
            "A.id                                       as address_id, "
            "CF.id                                      as contacted_refferer_id, "
            "G.id                                       as group_id, "
            "M.id                                       as mayor_id, "
            "PP.id                                      as politic_party_id, "
            "VS.id                                      as visit_status_id "

            "FROM \"financiationAPI_address\" AS A, "
            "\"financiationAPI_contactedreferrer\" AS CF, "
            "\"financiationAPI_group\" AS G, "
            "\"financiationAPI_mayor\" AS M, "
            "\"financiationAPI_politicparty\" AS PP, "
            "\"financiationAPI_visitstatus\" AS VS "
            "WHERE mod(A.id, 8) = mod(CF.id, 8) "
            "AND mod(CF.id, 3) = mod(G.id, 3) "
            "AND mod(M.id, 3) = mod(PP.id, 3) "
            "AND mod(PP.id, 3) = mod(VS.id, 3)) as d limit 10) as tabla_1, "
            "(SELECT id from \"financiationAPI_location\") as tabla_2 "
            "ORDER BY tabla_2.id"),

        migrations.RunSQL(
            "INSERT INTO \"financiationAPI_request\" (visit_id, request_datetime, advisor_id, faq_id, status_id, why_id, observation) "
            "SELECT id as id_visit, tabla_1.* "
            "from \"financiationAPI_visit\" as V, "
            "(SELECT (V.visit_date + V.start_time) + interval '1.5 min' * "
            "row_number() over (partition by V.id, W.id) as request_datatime, "
            "A.id                                                                        as advisor_id, "
            "F.id                                                                        as faq_id, "
            "RS.id                                                                       as status_id, "
            "W.id                                                                        as why_id, "
            "'hola' "
            "FROM \"financiationAPI_advisor\" as A, "
            "\"financiationAPI_faq\" as F, "
            "\"financiationAPI_requeststatus\" as RS, "
            "\"financiationAPI_visit\" as V, "
            "\"financiationAPI_why\" as W "
            "WHERE mod(A.id, 3) = mod(F.id, 3) "
            "AND mod(F.id, 3) = mod(RS.id, 3) "
            "limit 50) as tabla_1")
    ]
    dependencies = [
        ('financiationAPI', '0002_locations'),
    ]
