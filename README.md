

<!-- ABOUT THE PROJECT -->
## About The Project
We wanted to be able change the way students go about studying for their classes. By gamifying the experience and using space repition students can become more motivated to study for a variery of different topics. To accomplish this we decided to make a discord bot that students can implement into their class discord servers and utilzing by having the bot prompt them with random questions from a study set they upload. Additionally to increase engangement we wanted students to be able to challenge each other and compete by gaining points for questions they got right and displaying a leaderboard for top students.

### Built With
*Python
*Discord.py library
*MongoDB

## Getting Started

You will need to be able to download the lastest version of python, and set up a mongodb database.

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/decloon/RankSinatra
   ```
2. Create a and activate python enviornment in the backend folder
   ```sh
   python -m venv venv
   ```
   ```sh
   venv\Scripts\activate
   ```
3. Install python dependecies in the backend folder
   
   ```sh
   pip install -r requirements.txt
   ```
4. create a .env file for your connection variables
   ```sh
   touch .env
   ```
6. Run the python main file
   ```sh
   python main.py
   ```

<!-- USAGE EXAMPLES -->
## Usage

* Once you invited the bot to your discord server use !leaderboard to see the current rankings of students in the discord server, or !question to get a random question from the study set that has been uploaded

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Declan Staunton: https://github.com/decloon
* Hitarth Thanki: https://github.com/brohudev
* Jose Perla: https://github.com/joseperla1
  


