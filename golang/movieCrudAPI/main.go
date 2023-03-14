package main

import (
	"encoding/json"
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
)

// Define the type of data the about a movie
type Movie struct {
	Id       string    `json:"id"`
	Isbn     string    `json:"isbn"`
	Title    string    `json:"title"`
	Director *Director `json:"director"`
}

// Define a struct for movie Director
type Director struct {
	FirstName string `json:"firstname"`
	LastName  string `json:"lastname"`
}

// Create a movie slide out `main()`
// This makes the variable accessible in all the functions defined in this package
var movies []Movie

// Request handler for displaying all movies available
func getMovies(w http.ResponseWriter, r *http.Request) {
	// Write header file to indicate the type of resource
	w.Header().Set("Content-Type", "application/json")

	// check if data is properly encoded
	if err := json.NewEncoder(w).Encode(movies); err != nil {
		log.Fatal("Cannot Encode data")
	}

	log.Println("All movie data has been accessed")
}

func getMovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	// get the variables associated with the current request
	params := mux.Vars(r)

	// find the movie associated with the given id
	for _, item := range movies {
		if item.Id == params["id"] {
			_ = json.NewEncoder(w).Encode(item)

			log.Printf("%s data has been accessed\n", item.Title)
			return
		}
	}

	fmt.Fprintf(w, "No movie has this id: %s\nError: GET request failed", params["id"])
}

func createMovie(w http.ResponseWriter, r *http.Request) {
	// return an error if request body is empty
	// or have incomplete data fields
	log.Println(r.ContentLength)
	if r.ContentLength == 0 {
		fmt.Fprintln(w, "Error: POST request has no body\nMovie data was not added")
		return
	} else if r.ContentLength <= 80 {
		// 80 bytes is the minimum amount needed for a field to be incomplete
		fmt.Fprintln(w, "Error: POST request may have incomplete fields\nMovie data was not added")
		return
	}

	w.Header().Set("Content-Type", "application/json")

	// create a movie variable
	var newMovie Movie

	// read body of request and store the value to newMovie
	_ = json.NewDecoder(r.Body).Decode(&newMovie)

	// add the newMovie to movies list
	movies = append(movies, newMovie)

	// Show the client the new movie data
	_ = json.NewEncoder(w).Encode(newMovie)

	log.Printf("%s was added to movies\n", newMovie.Title)
}

func updateMovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	params := mux.Vars(r)

	for index, item := range movies {
		if item.Id == params["id"] {
			movie := movies[index]

			_ = json.NewDecoder(r.Body).Decode(&movie)
			_ = json.NewEncoder(w).Encode(movie)
			log.Printf("ID: %s; has been updated", movie.Id)
			return
		}
	}

	fmt.Fprintf(w, "No movie has this id: %s\nError: PUT request failed", params["id"])
}

func deleteMovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	// mux.Vars returns any route variables in current request
	params := mux.Vars(r)

	// find movie associated with the given id
	for index, item := range movies {
		if item.Id == params["id"] {
			// deleting an item from a slice
			// break down the slice into 2 parts
			// Each part excludes the index of the value you want deleted
			movies = append(movies[:index], movies[index+1:]...)
			fmt.Fprintf(w, "%s has been deleted\n", movies[index].Title)
			return
		}
	}

	// NOTE r.RemoteAddr gets the client ip address

	fmt.Fprintln(w, "Movie ID does not exist\nError: DELETE request failed.")
}

func main() {
	// set default movies data
	movies = append(movies, Movie{
		Id:    "1",
		Title: "Movie 1",
		Isbn:  "000001",
		Director: &Director{
			FirstName: "Lowry",
			LastName:  "Bright",
		},
	})

	movies = append(movies, Movie{
		Id:    "2",
		Title: "Movie 2",
		Isbn:  "000010",
		Director: &Director{
			FirstName: "John",
			LastName:  "Doe",
		},
	})

	movies = append(movies, Movie{
		Id:    "3",
		Title: "Movie 3",
		Isbn:  "000011",
		Director: &Director{
			FirstName: "Gab",
			LastName:  "Doe",
		},
	})

	movies = append(movies, Movie{
		Id:    "4",
		Title: "Movie 4",
		Isbn:  "000100",
		Director: &Director{
			FirstName: "Dorothy",
			LastName:  "Doe",
		},
	})

	r := mux.NewRouter()
	r.HandleFunc("/movies", getMovies).Methods("GET")
	r.HandleFunc("/movies/{id}", getMovie).Methods("GET")
	r.HandleFunc("/movies", createMovie).Methods("POST")
	r.HandleFunc("/movies/{id}", updateMovie).Methods("PUT")
	r.HandleFunc("/movies/{id}", deleteMovie).Methods("DELETE")

	fmt.Println("Starting server at port 8000...")
	log.Fatal(http.ListenAndServe(":8000", r))
}
