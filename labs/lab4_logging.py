import logging
# Set up basic logging to track input events
logging.basicConfig(filename='activitly.log', level=logging.INFO)

user_input = input("Hi! Say something: ")

# Log the input for trackability
logging.info("User input recieved: " + user_input)

print("Input logged.")