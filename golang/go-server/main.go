package main

import (
	"fmt"
	"log"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {

	// Just in case a wrong route enters this handler.
	// Might not be a practical use case, don't know yet; still learning.
	if r.URL.Path != "/hello" {
		http.Error(w, "404 not found", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "Method is not supported", http.StatusMethodNotAllowed)
		return
	}

	fmt.Fprintln(w, "Hello World!")
}

func formHandler(w http.ResponseWriter, r *http.Request) {

	if err := r.ParseForm(); err != nil {
		fmt.Fprintf(w, "Form was not able to be parsed properly\nError: %v", err)
		return
	}

	if r.Method == "GET" {
		http.ServeFile(w, r, "./static/form.html")
	}

	fmt.Fprintln(w, "POST request successful")
	name := r.FormValue("name")
	address := r.FormValue("address")
	fmt.Fprintf(w, "Name: %s\nAddress: %s\n", name, address)
}

func main() {
	// specify the root directory for website
	fileserver := http.FileServer(http.Dir("./static"))

	// register functions (handlers) for a given pattern (http request)
	http.Handle("/", fileserver)
	http.HandleFunc("/form", formHandler)
	http.HandleFunc("/hello", helloHandler)

	// message to display in console when server starts.
	fmt.Println("Starting server at port 8080...")

	// ListenAndServe always returns a non-nil error
	// checks if port is busy
	// shut down server if port is already in use
	if err := http.ListenAndServe("0.0.0.0:8080", nil); err != nil {
		log.Fatal(err)
	}
}
