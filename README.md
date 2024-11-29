# My Hatchery & Pet Management Application: Geneti-pets

## Overview

Geneti-pets is a dynamic web-based game for managing virtual Pets. It provides features to:
- View and manage a collection of Pets, complete with customizable visual traits based on genetics.
- Hatch eggs with randomized traits and assign names to newly hatched Pets.
- Visualize traits such as colors, symbols, and characteristics for Pets and eggs, using detailed styles and animations.
- A complexish Elemental Typing system including 120+ type combinations.
- Pet breeding, and the inheritance of physical traits from parent to child.

## Distinctiveness and Complexity

### Distinctiveness
Geneti-pets is quite unlike any CS50w project that I know of. It:
- Is effectively a virtual Pet simulator with the power to selectively breed for certain traits.
- Has an interesting genetic code currently involving 32 alleles, which are used to encode information.
- Uses Django in the styling

### Complexity
The project involves:
- Integration of Django’s template engine with custom logic to render dynamic content.
- Four models
- Extensive CSS for responsive and layered visual designs, ensuring a polished interface.
- JavaScript for client-side interactivity, including live updates like countdown timers.
- Server-client communication for managing the lifecycle of Pets and eggs.
- A genetic inheritance system written through the encoding and decoding of 32 character long strings
- Breeding, with chance of mutation

## File Descriptions

### Core Templates
- **`layout.html`**: Just the base layout of the page
- **`pets.html`**: Displays the list of all Pets with their traits visualized through layered CSS styles. Each Pet’s data is dynamically styled using custom filters and Django’s context rendering.
- **`breed.html`**: Allows for the breeding of Pets, letting the user choose one male and one female Pet that they own, and producing an egg that will eventually hatch into a brand new Pet.
- **`hatchery.html`**: Manages the egg hatching process, including displaying eggs, their parentage, countdown timers for hatching, and a modal interface for naming Pets upon hatching.
- **`login.html`**: A fairly standard login page.
- **`register.html`**: A fairly standard registration page.
- **`settings.html`**: Lets the user change their settings, currently only including Quality
- **`home.html`**: A currently empty page that will eventually include a fully responsive game interface

### CSS & Assets
- **`petView.css`**: Styles for Pet cards, ensuring each Pet's appearance reflects their attributes.
- **`eggView.css`**: CSS for visualizing eggs and styling the hatchery interface.
- **`style.css`**: Simple site-wide styling.
- **`typeStyle.css`**: Currently unused CSS that colors Type tags based on their given parameters.
- **`symbolStyle.css`**: Complex CSS used to visualize symbol images dynamically through the use of little modular bits and pieces of sprites.
- Symbol and trait images, stored in `/static/assets/`, are dynamically loaded based on the quality and type parameters.

### Backend
- Django to handle trait rendering logic, Pet storage, and egg storage.
- A custom filter to fetch values from dictionaries.

## How to Run the Application

### The Easy Way:

1. **Run the Application**
   - Simply run `runserver.bat`. It will handle everything.

2. **Access the web interface**
   - Access the application in a web browser at `http://127.0.0.1:8000`.

### The Slightly Less Easy Way:

1. **Install dependencies**:
   - Ensure Python and Django are installed.
   - Install required libraries: `pip install -r requirements.txt`.

2. **Set up the database**:
   - Make migrations: `python manage.py makemigrations`, just to be thorough.
   - Run migrations: `python manage.py migrate`.

3. **Start the server**:
   - Run `python manage.py runserver`.
   - Access the application in a web browser at `http://127.0.0.1:8000`.

## Additional Information

### Super Cool stuff
- **Real-time timers**: Countdown functionality updates every second using JavaScript to show when an egg is ready to hatch.
- **Customization**: The quality of images and animations can be adjusted dynamically through user settings, found at /settings.

### Mildly Funny stuff
- **Doctor Who?**: Superusers are able to go to `/wibblywobbly` in order to accelerate the hatching of eggs ([Wibbly Wobbly Timey Wimey](https://www.youtube.com/watch?v=mwoI4BqHt3E))

## Future Enhancements
Planned improvements include:
- Adding ingame currency
- Adding an auctionhouse for Pets to be bought and sold
- Adding a cost to Pet breeding
- Adding fighting and trait-based abilities
- Adding aging and maturity
- Adding anti-incest (Tracking parentage)
- Adding more traits and body types for Pets
- Adding substantially better styling
- Adding more jokes for myself in the backend

## Video
[Here it is](https://youtu.be/tdjSumwCkJg)
https://youtu.be/tdjSumwCkJg