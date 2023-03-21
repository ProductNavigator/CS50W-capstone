# Product Questions

#### Distinctiveness and Complexity
The project is building and changing the idea intially created by me for the final project for CS50. The idea has been modified, with the biggest change of core value to users: from access to the full database of questions, to the answering of concrete problem of users - having handy list of product question for specific meeting/interview/survey. That is why the project moved from presenting full database of product questions to generating Sets of Product Questions, which might be stored and reused. In order to create them I:
1. Ask user to specify concrete need - what kind of question she/he is looking, why he/she wants to ask it, to whom, and when.
2. Based on the database (now not public anymore), I select suitable questions based on initial selection based on categorisation and random selection amongst already pre-vetted suitable questions. 
3. I present them to the user.

I took extra effort to analyze user journeys in the app, and designed the flows in order to:
1. Finalize the value delivery to the user in less than 4 steps from value promise, to delivery (with value refreshment after 2 step)
2. Allow user to create a set even without logging/registering, but not allow to see it fully without this step. 
3. Build system to organically build the database, by collecting the proposed questions from users who are generating sets - concrete question while they create set: "what would be your proposed question in that scenario?"




#### How to run the application 
1. Download files 
2. Install Python 
3. Install Django 
4. In the main file, run shell comman ```python manage.py runserver``` or ```python3 manage.py runserver``` depending on the version of Python you are using 

#### Description:

## Intro

The idea behind the Product Questions project is simple. It starts with the notion that people working as product managers, owners or leads have one superpower: asking awsome questions.

The Product Questions web application aims at helping them to discover their full potential. It is doing so by building and publishing online the biggest open database of product questions. Questions that product people are asking every day across the world to make their products successful.

## For users

Everyone can join the Product Questions community by generating Product Questions Set. The form asks user to specify first the concrete scenario when the product questions will be used:

- **Types of questions** - specifies the type of the question. It gives the user 6 options to select from: Agree/Disagree, Multiple choice, Open, Scale, Single choice, Yes/No/Don't know.
- **Why you want to ask them** - specifies the goal of the person asking the question. 7 possible options are on the table: Contextualization, To map job to be done, To pinpoint problem(s, To setup metrics, To understand the ultimate goal, To understand the use case, Validation. 
- **Who you want to ask** - specifies the usual addressee of the question. It gives the user 4 groups to select from:  Customer, Data (analytics), End user, Internal stakeholder, Yourself
- **When you want to use them** - What will be the context of asking this question, will you speak directly or maybe it is part of online survey? 6 possible scenarions are available: Data exploration, Desktop research, Feedback form/survey, In-depth interview, Panel discussion, Quick sync.

Once the set is generated, user is asked to login or register. If this is first time when the Set is presented to the user, Product Questions will also request feedback from user, asking what kind of question user will ask in specified scenario. This way we are making the Product Question community-based growing dabase of questions.

The form is presented as a seperate route and is available from every page of the web application, thanks to the top-bar button "Generate"

Apart from the main value for the user, which is the possibility to generate Product Questions, user can also: 

1. See his previous Product Questions sets
2. Visit "Hall of Fame" where top product minds share questions they use on daily basis. 


## Structure of the web application

### >>>Product Question Django Project

##### >manage.py
Python file managing the Django project. 

##### >db.sqlite3
SQLite database gathers information from users and enables the display of information, to make this project truly open and community-driven. It is build and managed via Django Models avaialble to manage via Django Admin panel. 

There are 5 key models, and 4 supporting. 

Key models:
1. User - users of the app, uses generic Django User class 
2. Question - product questions 
3. Set - sets of questions that are generated by users and presented to them 
4. Proposed Questions - questions send by users as propostions
5. Hall of Fame - entries presented to users in the Hall of Fame, currenty inly manually added via Django Admin

Supporting models - all are related to Question:
- Type - type of the questions.
- Why - goal of the questions. 
- Who - who will be asked.
- When - When this question will be asked.

#### >> PQ application 

##### >urls.py 
Defines all routs in the app 

##### >models.py 
Defines all models in the app 

##### >admin.py 
Defines the possible options in the Django Admin 

##### >viewes.py 
Defines and manages all views served based on requests to urls. It defines POST as well as GET for all routes.

Main viewes: 
- index - Mainpage 
- login, logout, register - Managing users authentication 
- generate - Displays form to generate product questions sets. Generates product questions set based on user POST requests. 
- set - presensts Product Question Set to the user 
- user - presents user with a list of all his Product Question sets
- halloffame - presents Hall of Fame 


#### >>>Templates

###### >layout.html
By using jinja syntax and layouts I aim at improving the scalability of the project in the next steps. The narrow focus of the first functionalities might be easily wider based on the existing template in layout.

It includes the:
- Top bar with logo and top navigation, and "Generate" button
- Footer

###### >index.html
Presentes the main idea of the project and aims at navigating the user to the "Generate" action. 

###### >generate.html
For to generate Product Question set based on database 

###### >set.html
Presents the Product Quesiton set. Thanks to modals, it allows user to login or register, if user is not authenticated. It also prompts user to share his question, if the set is presented to the user for the firs time (exeption: right after registraction we don't ask for this)

###### >{{user.name}}.html
Present to the user all his Produc Question sets 

###### >halloffame.html
Presents Hall of Fame with product questions.

#### >>>Static
###### >layout.js
Provides dynamic element of the main look - the changing topbar during scroll 

###### >setregister.js
Provides dynamic element for the set presentaion - helps to manage 3 modals dynamically on that page.

###### >styles.css
Includes styles, both from the Bootstrap documentation as well as custom.


