# This code taught me how to detect and block too many requests from the same user.
# Rate limiting is a defense mechanism to protect apps from spam, abuse and system crashes from overload.

import time
requests = {}
user = "test user"
now = time.time()
if user in requests and now - requests[user] < 10:
    # Block the request
    print("Too many requests. Try again later.")
else:
    # Allow request and store the timestamp
    requests[user] = now
    print("Accepted!")
