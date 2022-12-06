<p align="center">
  <img
    width="400"
    src="https://flashcards-519da.web.app/static/media/logo.6d3f27e3fc0c4a7bc3b3.png"
    alt="Starship – Cross-shell prompt"
  />
</p>
<p align="center">
  <a href="https://github.com/csc510-fall22-p2-g33/FlashCards/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/csc510-fall22-p2-g33/flashcards?style=plastic"></a>
  <img src="https://img.shields.io/github/languages/count/csc510-fall22-p2-g33/flashcards">
  <a href="https://github.com/csc510-fall22-p2-g33/FlashCards/graphs/contributors" alt="Contributors">
<img src="https://img.shields.io/github/contributors/csc510-fall22-p2-g33/FlashCards?style=plastic"/> </a>
<a href="https://github.com/csc510-fall22-p2-g33/FlashCards/actions/workflows/Application.yml" alt="Python application">
<img src="https://github.com/csc510-fall22-p2-g33/FlashCards/actions/workflows/Application.yml/badge.svg?style=plastic?branch=main"/> </a>
<a href="https://github.com/csc510-fall22-p2-g33/FlashCards/actions/workflows/Coverage.yml/badge.svg" alt="Code coverage">
<img src="https://github.com/csc510-fall22-p2-g33/FlashCards/actions/workflows/Coverage.yml/badge.svg"/> </a>
<a href="https://codecov.io/github/csc510-fall22-p2-g33/FlashCards" >
<img src="https://codecov.io/github/csc510-fall22-p2-g33/FlashCards/branch/main/graph/badge.svg?token=RYRDY1IZNM"/></a>
<a href="https://zenodo.org/badge/latestdoi/564548849" alt="DOI">
<img src="https://zenodo.org/badge/564548849.svg"/> </a>
<a href="https://img.shields.io/badge/python-v3.8+-yellow.svg" alt="Python version">
<img src="https://img.shields.io/badge/python-v3.8+-yellow.svg"/> </a>
<a href="https://img.shields.io/github/repo-size/csc510-fall22-p2-g33/FlashCards?color=brightgreen" alt="Repo size">
<img src="https://img.shields.io/github/repo-size/csc510-fall22-p2-g33/FlashCards?color=brightgreen"/> </a>
<img src="https://img.shields.io/github/languages/top/csc510-fall22-p2-g33/Flashcards?style=plastic">
<img src="https://img.shields.io/tokei/lines/github/csc510-fall22-p2-g33/flashcards?style=plastic">
<a href="https://github.com/csc510-fall22-p2-g33/FlashCards/issues">
  <img src="https://img.shields.io/github/issues-raw/csc510-fall22-p2-g33/flashcards?style=plastic"></a>


<a href="https://img.shields.io/github/release/csc510-fall22-p2-g33/FlashCards?color=brightblue" alt="Release">
<img src="https://img.shields.io/github/release/csc510-fall22-p2-g33/FlashCards?color=brightblue"/> </a>
</p>

## Description
Are you a student and having trouble preparing for tests and exams? Look no further. FlashCards also helps you memorize all that hard-to-remember information with online flashcards so that you ace your exams!

FlashCards is a spaced repetition learning platform to <b>create</b>, <b>memorize</b> and <b>share</b> your knowledge list using flashcards.

1. Create and customize your own deck of cards
2. Practice mode

## Watch Flashcards in Action
https://user-images.githubusercontent.com/17693596/194787705-309ebf62-2a3d-4075-94b4-6da814a953a8.mp4

## Tech Stack
<a href="https://flask.palletsprojects.com/en/2.2.x/"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" /></a>
<a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" /></a>
<a href="https://reactjs.org/"><img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /></a>
<a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=black" /></a>
<a href="https://github.com/"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://ant.design/"><img src="https://img.shields.io/badge/Ant%20Design-1890FF?style=for-the-badge&logo=antdesign&logoColor=white" /></a>

## Getting started & Installation:

### Production

From the root folder, the application can be run in a production environment with the following command:

**NOTE:** make sure you follow the steps for setting up Firebase in the Backend README file (see below).

```
sudo docker-compose -f docker-compose.production.yml up --build --scale backend=2 --scale frontend=2
```

**NOTE:** the above command creates 2 frontend instances and 2 backend instances. The number of instances can be modified by changing the corresponding numbers in the command.

### Development

#### Backend

[See README.md](https://github.com/csc510-fall22-p2-g33/FlashCards/blob/main/backend/Readme.md)

#### Frontend

[See README.md](https://github.com/csc510-fall22-p2-g33/FlashCards/blob/main/frontend/README.md)

## Current Screens
<p>
  <img
    width="100%"
    src="./frontend/src/assets/images/1.png"
    alt="Demo Screens 1"
  />

  <img
    width="100%"
    src="./frontend/src/assets/images/2.png"
    alt="Demo Screens 2"
  />
</p>

## Future Roadmap

[See here](https://github.com/orgs/csc510-fall22-p2-g33/projects/1)

### Phase 1:
- [x] Create database ER diagram
- [x] User Login
- [x] User Signup/Create Account
- [x] Explore or Search Public FlashCards
- [x] Create/Read/Update/Delete <b>Decks</b> <i>(collections of cards)</i>
- [x] Create/Read/Update/Delete <b>Cards</b>
- [x] FlashCard Practice Mode
- [x] Add Unit testing
- [x] Setup backend and frontend deployment

### Phase 2:
- [x] Containerize/Dockerize application
- [x] Create production optimized build
- [x] Add service scaling and load balancing
- [x] Rate a deck which is public
- [x] Make a card deck public/private
- [x] Invite friends to a private Study Deck
- [x] Login with 3rd Party Auth
- [ ] *See more issues at Github Project link above*

## Contributions to the Project
Please refer to the [Contributing.md](https://github.com/csc510-fall22-p2-g33/FlashCards/blob/main/Contributing.md) if you want to contrbute to the FlashCards source code. Follow all the guidelines mentioned and raise a pull request for the developers to review before the code goes to the main source code.

## Help

Email any queries to the contributors -
1. [Swarangi Gaurkar](sgaurka@ncsu.edu)
2. [Kritika Javali](ksjavali@ncsu.edu)
3. [John Damilola](djbabalo@ncsu.edu)
4. [Aaron Dias Barreto](aadiasba@ncsu.edu)
5. [Leo Hsiang](yhsiang@ncsu.edu)

## Authors 

1. [Kritika Javali](https://github.com/ksjavali)
2. [Swarangi Gaurkar](https://github.com/Swarangigaurkar)
3. [Aaron Dias Barreto](https://github.com/aaron278)
4. [Leo Hsiang](https://github.com/leoohsiang)
5. [Damilola Babalola](https://github.com/JohnDamilola)

## License
[MIT](https://tldrlegal.com/license/mit-license)

## Funding
Our project at the moment is not funded by any organization/individual.
