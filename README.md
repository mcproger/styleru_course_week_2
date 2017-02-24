# style course. week 2 #

This work consist of three programs written in Python 3.x. This programs allow to work with API's methods from api.superjob.ru 

# 1. api_superjob #

This program allow make list for 100 vacancies of programmers different programming languages from Moscow. It's use API-key to send requests to api.superjob.ru and add it to .json file.
User have to enter from keyboard API key and route for this file.

### Example of API key  ###
v1.r077061da289232ac013a12e2a6470da3e65357ae6e4869bfdba3c1906be79b5ad5d16218.17192fd1ef008069573a5d6aa5ffe26dedba90b4

# 2. vacancies_treatment #

This program treats .json file from previous program. It's leaves only the name of the professions, working conditions, payment and add it to new .json file.
User have to enter route from previous programm and route for new .json file.

# 3. rating_list #

This program make rating list based on .json file from previous programm. It considers quantity of vacancies for different programming languages and their average salary. 
Also this programm builds histogram based on rating for different programming languages. 

    
    
