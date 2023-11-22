# docker_flask_homework
HHA 504- Assignment #7- Week 8


## Part 1:
- First, I went ahead and created a simple flask application and ensured that I was able to deploy it locally in my Google Shell environment.
<img width="700" alt="Screenshot 2023-11-20 at 10 15 30 PM" src="https://github.com/angeliki-tzanou/docker_flask_homework/assets/141374140/b729709e-b8e2-473d-841b-208e8ac06bc2">
- Then I created a Dockerfile for my Flask app in which I included and explained the Python version and used as a parent image, the working directory my app was located in, copied the contents of my app to the new app container, ensured that all packages would be installed from my ```requirements.txt``` file, specified the port # I wanted to expose my docker app in, and included the name of the app in order to be able to ```python app.py```, in my case, and run it.
- After doing so I ran the command ```docker build -t __name_of_the_app__``` in order to name and create the docker image for my flask app, as well as run all and install all the necessary packages from my already created ```requirements.txt file```
- After the command successfully ran, I used ```docker images``` in order to ensure that my docker images was indeed successfully created by using the previous command
- Then I used ```docker run -p port:port``` substituting with the preferred ports in order to expose it and run it in the port chosen.
- After that I ran ```docker -d -p port:port __name_of_flask__``` in order to ensure that my app could run detached while working. (While getting as an output the ID of the container the app is and will be running in)
- Then by using ```docker ps``` it provided me with a list of all the docker containers I have running along with their IDs.
- Finally to stop my docker from running in the container I used ```docker stop __ID of container running__``` and it stopped my instance.
- Just to double check if I wanted to start it back up again I used the ```docker run -d -p port:port __name_of_app__```.
