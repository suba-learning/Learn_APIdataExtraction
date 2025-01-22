# Learn_APIdataExtraction

This project demonstrates how to extract and process data from API responses using Python. The examples use the Pokémon API to showcase various data extraction techniques.

## Code Overview

### Sending GET Requests
The code demonstrates how to send GET requests to APIs using the `requests` library and print various details of the response, such as status code, content, and headers.

### Pretty Printing JSON Data
The code shows how to pretty print JSON data from an API response using the `json.dumps` method with indentation for better readability.

### Extracting JSON Data
The code provides examples of extracting specific information from JSON data, such as abilities and game indices of a Pokémon from the Pokémon API.

### Looping Through JSON Data
The code includes examples of looping through JSON data to print specific attributes and extract data based on certain conditions.

## Usage

To run the code, simply execute the `json_extraction.py` script. The script will send GET requests to the specified APIs, handle the responses, and print the extracted information to the console.

```bash
python json_extraction.py


Scenarios
Here are some scenarios you can work on to practice processing data from the JSON response of the given API:  
Extract and Print Pokémon Name and ID:  
Extract the name and ID of the Pokémon from the JSON response and print them.
List All Abilities:  
Extract and print all the abilities of the Pokémon.
Filter and Print Hidden Abilities:  
Extract and print only the hidden abilities of the Pokémon.
List All Game Indices:  
Extract and print all the game indices where the Pokémon appears.
Filter Game Indices by Version:  
Extract and print the game indices for a specific version (e.g., "red").
Extract and Print Base Stats:  
Extract and print all the base stats (e.g., HP, attack, defense) of the Pokémon.
Filter and Print Stats Above a Threshold:  
Extract and print stats that are above a certain threshold (e.g., base stat > 50).
Pretty Print the Entire JSON Response:  
Pretty print the entire JSON response with indentation for better readability.
Count the Number of Moves:  
Extract and count the number of moves the Pokémon can learn.
Extract and Print Move Names:  
Extract and print the names of all moves the Pokémon can learn.
These scenarios will help you get hands-on experience with JSON data extraction and manipulation using Python.  


**Requirements**
The project requires the following Python packages:  
certifi==2024.12.14
charset-normalizer==3.4.1
idna==3.10
requests==2.32.3
urllib3==2.3.0

You can install the required packages using the following command:
pip install -r requirements.txt

view of the project, usage instructions, scenarios for practice, and the required dependencies.