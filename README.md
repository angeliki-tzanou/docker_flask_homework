# docker_flask_homework
HHA 504- Assignment #7- Week 8


## Part 1:
- First, I went ahead and created a simple flask application and ensured that I was able to deploy it locally in my Google Shell environment.
<img width="700" alt="Screenshot 2023-11-20 at 10 15 30 PM" src="https://github.com/angeliki-tzanou/docker_flask_homework/assets/141374140/b729709e-b8e2-473d-841b-208e8ac06bc2">

- Then I created a Dockerfile for my Flask app in which I included and explained the Python version and used as a parent image, the working directory my app was located in, copied the contents of my app to the new app container, ensured that all packages would be installed from my 
 ```requirements.txt``` file, specified the port # I wanted to expose my docker app in, and included the name of the app in order to be able to 
 ```python app.py```, in my case, and run it.

- After doing so I ran the command  ```docker build -t __name_of_the_app__``` in order to name and create the docker image for my flask app, as well as run all and install all the necessary packages from my already created 
 ```requirements.txt file```

- After the command successfully ran, I used  ```docker images``` in order to ensure that my docker images was indeed successfully created by using the previous command
  <img width="700" alt="Screenshot 2023-11-21 at 11 12 14 AM" src="https://github.com/angeliki-tzanou/docker_flask_homework/assets/141374140/4cdcff40-02e5-4521-8036-1bd580bd40cf">

- Then I used ```docker run -p port:port _name_of_app_``` substituting with the preferred ports in order to expose it and run it in the port chosen.
  <img width="700" alt="Screenshot 2023-11-21 at 11 20 45 AM" src="https://github.com/angeliki-tzanou/docker_flask_homework/assets/141374140/59f6c272-29b9-4a0b-ac71-615a381c2992">

  <img width="700" alt="Screenshot 2023-11-21 at 11 20 33 AM" src="https://github.com/angeliki-tzanou/docker_flask_homework/assets/141374140/c692b39e-0d99-4343-a353-a2ff7a2ea37b">

- After that I ran  ```docker -d -p port:port __name_of_flask__``` in order to ensure that my app could run detached while working. (While getting as an output the ID of the container the app is and will be running in)
  <img width="700" alt="Screenshot 2023-11-21 at 11 21 05 AM" src="https://github.com/angeliki-tzanou/docker_flask_homework/assets/141374140/db01c47a-9fb7-48b5-9ece-fe4f453d3c4e">

- Then by using  ```docker ps``` it provided me with a list of all the docker containers I have running along with their IDs.
  <img width="700" alt="Screenshot 2023-11-21 at 11 21 25 AM" src="https://github.com/angeliki-tzanou/docker_flask_homework/assets/141374140/b21b463b-8a9d-47e2-8ce7-c49c7702b1f6">

- Finally to stop my docker from running in the container I used  ```docker stop __ID of container running__``` and it stopped my instance.
  
- Just to double check if I wanted to start it back up again I used the 
 ```docker run -d -p port:port __name_of_app__```.
