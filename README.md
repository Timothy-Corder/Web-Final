# My Hatchery & Pet Management Application: Geneti-pets

## Overview

Geneti-pets is a dynamic web-based game designed to manage virtual pets. The application allows users to view and manage a collection of pets, each with customizable visual traits influenced by genetic inheritance. Players can hatch eggs with randomized traits, assign names to newly hatched pets, and even breed pets to pass on genetic traits. The system incorporates a variety of features, including an intricate elemental typing system with over 120 type combinations. Players can also explore pet breeding, which involves the inheritance of physical traits from parents, as well as the potential for genetic mutations.

## Distinctiveness and Complexity

Geneti-pets is a unique application that stands apart from other CS50W projects. Unlike the projects involving e-commerce or social networking, Geneti-pets serves as a virtual pet simulator with an emphasis on genetics, breeding mechanics, and interactive gameplay. The project introduces a genetic system encoded in 32 alleles, used to determine visual and functional traits of the pets. These genetics influence everything from color to symbols and characteristics, providing a degree of depth and complexity beyond standard web applications. 

The complexity of Geneti-pets lies in the integration of Django’s backend capabilities with a dynamic and interactive front-end powered by JavaScript. The project employs four models to manage pets, eggs, and user-related data while utilizing Django’s template engine to render dynamic content. CSS is extensively used to create responsive and visually appealing interfaces, ensuring the application is polished and user-friendly. The genetic inheritance system, implemented through encoded strings, adds a layer of algorithmic complexity, while JavaScript facilitates real-time updates, such as countdown timers for egg hatching. These features collectively highlight the distinctiveness and technical depth of the application.

## File Descriptions

The project includes a variety of templates to support its functionality. The `layout.html` file provides the base layout for all pages. The `pets.html` template displays a list of pets with their traits visualized using layered CSS styles, dynamically rendered through Django’s context. The `breed.html` template enables users to breed pets, allowing them to select a male and female pair to produce an egg that inherits traits from both parents. The `hatchery.html` template manages the egg-hatching process, displaying eggs, countdown timers, and an interface for naming newly hatched pets. Other templates include `login.html` and `register.html` for user authentication, `settings.html` for adjusting user preferences, and `home.html` for a game interface under development.

The CSS files further enhance the user experience. The `petView.css` file styles pet cards to reflect their attributes, while `eggView.css` provides visualizations for eggs. A `style.css` file ensures consistent site-wide styling, and `symbolStyle.css` supports complex visualizations for traits and symbols using modular sprite components. Images and assets are dynamically loaded from the `/static/assets/` directory based on parameters such as quality and type.

On the backend, Django handles logic for trait rendering, pet and egg storage, and custom filters for dynamic content. A custom filter allows fetching values from dictionaries, which simplifies data rendering.

## How to Run the Application

The easiest way to run the application is by executing the `runserver.bat` file, which automates the process. Once the server starts, the application can be accessed in a web browser at `http://127.0.0.1:8000`.

For those who prefer manual setup, the required Python dependencies can be installed using `pip install -r requirements.txt`. The database should then be set up by running `python manage.py makemigrations` followed by `python manage.py migrate`. Afterward, the server can be started with `python manage.py runserver`, and the application can be accessed at the same URL.

## Additional Information

Geneti-pets incorporates several advanced features. Real-time timers implemented using JavaScript allow users to track egg-hatching progress down to the second. The settings page enables users to adjust visual quality and animations dynamically. A hidden feature for superusers, accessible at `/wibblywobbly`, provides the ability to accelerate egg hatching for testing purposes.

Future enhancements to the application include introducing an in-game currency, an auction house for buying and selling pets, and a cost mechanism for breeding. Plans also include implementing aging and maturity mechanics, anti-incest tracking for parentage, expanded trait and body type options, combat features, and further styling improvements.

## Video

A demonstration video for Geneti-pets is available at the following link: [https://youtu.be/tdjSumwCkJg](https://youtu.be/tdjSumwCkJg).
