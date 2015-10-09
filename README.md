# FlaskSample Project

A python flask project that uses Angular JS for the UI and client logic, and Python Flask as the server engine that provide the initial page URL, and a REST API for the client model.

## Introduction

I wanted to generate a basic working web application skeleton that would do the following:

  * Serve up a single page web application
  * Use Angular JS
  * Provide a REST API for the UI's model
  * The REST API would use a Mongo DB Back end storage via Python
  * Uses Bootstrap.js for styling and responsive design 

The 

## Files

   * App.py: The main app that will run the Flask server. It defines the routes.
   * restHandlers.py: Provides calls for the basic CRUD methods that the REST API will provide.
   * templates/index.html: The main page that contains the app.
   * static/notesController.js: Angular JS for the Notes application controller


   http://localhost:5000

   Will bring up the Notes application. 


## REST API

   * GET	/note/			Gets the list of notes
   * GET	/note/<note_id>		Gets a specific note
   * POST /note			Creates a note
   * PUT  /note/<note_id> 	Updates note in post data
   * DELETE /note/<note_id>	Deletes a specific note
   * DELETE /note/drop		Drops the entire notes table

