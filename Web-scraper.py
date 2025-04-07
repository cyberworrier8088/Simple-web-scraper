import requests  
import os  
import time  

while True:  
    # Prompt the user to enter a URL
    url = input("Enter your URL: ")  
    
    # Prompt the user to enter a filename (e.g., text.txt, text.html)
    result = input("Enter your file name like text.txt, text.html etc: ")  
    
    # Send a GET request to the entered URL
    r = requests.get(url)  
    
    # Print the response text
    print(r.text)  
    
    # Write the response text to the specified file
    with open(result, "w", encoding='utf-8') as file:  
        file.write(r.text)  
        print(f"Your result: {result}")  
    
    # Wait for 4 seconds before repeating
    time.sleep(4)  
    
    # Clear the console screen
    os.system('clear')
