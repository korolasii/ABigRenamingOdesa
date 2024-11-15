import sqlite3

# Function to fetch data from the database
def selectData(name):
    # Establish a connection to the database file
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    
    # Execute a query to fetch all rows from the 'users' table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Close the database connection
    connection.close()
    
    # Return the fetched data (all rows from the 'users' table)
    return rows


# Uncomment the following section if you need to create the 'users' table and add some sample data:

# connection = sqlite3.connect("example.db")  # Connect to the database
# cursor = connection.cursor()

# Create the 'users' table if it doesn't already exist

# Commit the changes to the database
# connection.commit()

# Insert sample data into the 'users' table
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Адмирала Лазарева", "Улица Михаила Болтенко", 
#                 "Переименована в честь Михаила Болтенко, известного командующего во время Второй мировой войны."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Академика Воробьева", "Улица Виталия Нестеренко", 
#                 "Переименована в честь Виталия Нестеренко, знаменитого ученого в области физики и астрономии."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Проспект Академика Глушко", "Проспект Князя Ярослава Мудрого", 
#                 "Переименован в честь Князя Ярослава Мудрого, одного из величайших правителей Киевской Руси."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Академика Панкратовой", "Улица Дмитрия Сигаревича", 
#                 "Переименована в честь Дмитрия Сигаревича, выдающегося ученого в области биохимии."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Амвросия Бучмы", "Улица Михаила Билинского", 
#                 "Переименована в честь Михаила Билинского, известного украинского писателя и драматурга."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Переулок Апполона Скальковского", "Переулок Зои Пасечной", 
#                 "Переименован в честь Зои Пасечной, известного украинского культурного деятеля."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Армейская", "Улица Независимости", 
#                 "Переименована в честь Дня Независимости Украины."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Бабеля", "Улица Дмитрия Иванова", 
#                 "Переименована в честь Дмитрия Иванова, известного украинского писателя и поэта."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Багрицкого", "Улица Михаила Бойчука", 
#                 "Переименована в честь Михаила Бойчука, выдающегося художника и основателя бойчуковского стиля."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Переулок Бадаева", "Переулок Марии Станишевской", 
#                 "Переименован в честь Марии Станишевской, известной украинской актрисы и режиссера."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Переулок Барятинский", "Переулок Дмитрия Лесича", 
#                 "Переименован в честь Дмитрия Лесича, выдающегося украинского ученого в области географии."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Братьев Поджио", "Улица Василия Фащенко", 
#                 "Переименована в честь Василия Фащенко, известного украинского деятеля культуры."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Бунина", "Улица Нины Пестрой", 
#                 "Переименована в честь Нины Пестрой, выдающейся украинской писательницы."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Высоцкого", "Улица Ярослава Баиса", 
#                 "Переименована в честь Ярослава Баиса, украинского писателя и философа."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Вице-адмирала Азарова", "Улица Андрея Гулого-Гуленко", 
#                 "Переименована в честь Андрея Гулого-Гуленко, украинского политического деятеля."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Переулок Вице-адмирала Жукова", "Переулок Ивана Луценко", 
#                 "Переименован в честь Ивана Луценко, известного украинского писателя."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Веры Инбер", "Улица Владимира Рутковского", 
#                 "Переименована в честь Владимира Рутковского, украинского писателя и поэта."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Гагарина", "Улица Семена Камирного", 
#                 "Переименована в честь Семена Камирного, советского и украинского космонавта."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Переулок Гагарина", "Переулок Михаила Гордиевского", 
#                 "Переименован в честь Михаила Гордиевского, украинского инженера и ученого."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Проспект Гагарина", "Проспект Леси Украинки", 
#                 "Переименован в честь Леси Украинки, великой украинской писательницы и поэтессы."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Гагаринское плато", "Аркадийское плато", 
#                 "Переименовано в честь Аркадия, украинского писателя и общественного деятеля."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Гавришова", "Улица Андрея Соловьёва", 
#                 "Переименована в честь Андрея Соловьёва, известного украинского археолога и историка."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Гайдара", "Улица Валентина Симонова", 
#                 "Переименована в честь Валентина Симонова, известного украинского писателя и дипломата."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Горького", "Улица Богдана Хмельницкого", 
#                 "Переименована в честь Богдана Хмельницкого, гетмана Украины."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Грекова", "Улица Николая Устименко", 
#                 "Переименована в честь Николая Устименко, украинского архитектора и историка."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Грозненский проспект", "Проспект Петра Калнышевского", 
#                 "Переименован в честь Петра Калнышевского, украинского гетмана и общественного деятеля."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Декабристов", "Улица Якова Гурина", 
#                 "Переименована в честь Якова Гурина, известного украинского ученого и государственного деятеля."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Переулок Дзержинского", "Переулок Михаила Загребельного", 
#                 "Переименован в честь Михаила Загребельного, известного украинского писателя и поэта."))
# cursor.execute("INSERT INTO users (nameOld, nameNew, history) VALUES (?, ?, ?)", 
#                 ("Улица Дзержинского", "Улица Андрея Платонова", 
#                 "Переименована в честь Андрея Платонова, выдающегося русского писателя."))

# Commit the changes to the database
# connection.commit()


# Close the database connection
# connection.close()