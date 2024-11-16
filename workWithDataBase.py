import sqlite3

# Function to fetch data from the database
def selectData(name):
    # Establish a connection to the database file
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    
    # Execute a query to fetch all rows from the 'users' table
    cursor.execute("SELECT * FROM streets")
    rows = cursor.fetchall()

    # Close the database connection
    connection.close()
    
    # Return the fetched data (all rows from the 'users' table)
    return rows


# connection = sqlite3.connect("street.db")  # Connect to the database
# cursor = connection.cursor()

# # Create the 'users' table if it doesn't already exist
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS streets (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nameOld TEXT NOT NULL,
#     nameNew TEXT NOT NULL,
#     history TEXT NOT NULL,
#     url TEXT NOT NULL  -- Ensure this matches the insertion fields
# )
# """)

# # Commit the changes to the database
# connection.commit()

# # Sample data with corrected field names
# data = [
#     ("вулиця Ільфа і Петрова", "сім'ї Глодан", 
#         "Вулицю переіменували на честь Сім’ї Глодан – родини одеського пекаря Юрія, яка мешкала у житловому комплексі “Тірас”. У квітні 2022 року через російський ракетний удар у квартирі загинули його дружина Валерія, тримісячна донька Кіра та теща Людмила.Після цієї втрати Юрій долучився до лав Збройних сил: спочатку служив в полку “Азов”, а потім — у 3-й окремій штурмовій бригаді. Юрій Глодан загинув у вересні 2023-го поблизу міста Бахмут Донецької області.", 
#         "https://www.google.com/maps/place/%D1%83%D0%BB.+%D0%A1%D0%B5%D0%BC%D1%8C%D0%B8+%D0%93%D0%BB%D0%BE%D0%B4%D0%B0%D0%BD,+%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%B0,+%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C,+65000/@46.394196,30.7133267,17z/data=!3m1!4b1!4m6!3m5!1s0x40c63356de2d1e65:0xb323f09d45d523d9!8m2!3d46.3941923!4d30.7159016!16s%2Fg%2F1tl8j6kl?hl=ru&entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoASAFQAw%3D%3D"),
# ]

# # Insert data into the 'users' table
# cursor.executemany("""
#     INSERT INTO streets (nameOld, nameNew, history, url)
#     VALUES (?, ?, ?, ?)
# """, data)

# # Commit the changes to the database
# connection.commit()

# # Close the database connection
# connection.close()
