# Importing the selectData function for fetching data from the database
from workWithDataBase import selectData

# Function to search for a street by name
def searchStreet(nameStreet):
    # Convert the street name to lowercase to make the search case-insensitive
    nameStreet = nameStreet.lower()
    
    # Initialize a dictionary to store information about the found street
    dataForStreet = {
        "oldName": "",  # old street name
        "newName": "",  # new street name
        "history": "",  # history of the street renaming
    }
    
    # Fetch all data from the database using the selectData function
    data = selectData("example.db")
    
    # Iterate over the data and look for a match with the street name
    for i in data:
        # Check if the old or new street name matches the provided one
        if nameStreet == i[1].lower() or nameStreet == i[2].lower():
            # If a match is found, store the relevant data in the dictionary
            dataForStreet["oldName"] = i[1]
            dataForStreet["newName"] = i[2]
            dataForStreet["history"] = i[3]
            break  # Stop the loop after the first match is found
    
    # If the street wasn't found, return a message indicating that nothing was found
    if dataForStreet["oldName"] == "":
        dataForStreet = 'Nothing found'
    
    # Return the found data (or a message indicating nothing was found)
    return dataForStreet

# Test the function by printing the result of searching for a street
if __name__ == "__main__":
    print(searchStreet('Admiral Lazarev Street'))
