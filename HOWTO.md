# How To Use a REST API (with an API key)

1. Obtain an **`API key`**

2. Note the **`API's base url`** (e.g. https://api.xxx.com/api/v1)

3. Get the API documentation

4. Determine which **`endpoint`** you need (e.g. /check)

5. For the endpoint, determine which *`*`HTTP method`** to use (e.g GET, POST, PUT, etc.)

6. Determine which **`parameters`** to send to the endpoint (e.g. ipAddress)

    a. If you are using GET it will be through the query string

    b. If you are using POST it will be through the body

7. Determine which **`headers`** need to be added as a part of the request

    a. If using an API key, most likely you will need to add:
    - `"Authoriziation": <insert_your_api_key>`
    
    b. If using JSON format, add:
    - `"Content-Type": "application/json"`

8. Apply that to the type of client you are creating (e.g. Python or Bash)

