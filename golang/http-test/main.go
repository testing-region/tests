package main

import (
	"fmt"
	"net/http"
)

func main() {
	mux := http.NewServeMux()
	api := http.NewServeMux()

	mux.HandleFunc("GET /path", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "You have hit the path\n")
	})

	mux.HandleFunc("/task/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := r.PathValue("id")
		fmt.Fprintf(w, "The task with the id: %s\n", id)
	})

	fmt.Println("Listening...")

	http.ListenAndServe(":8000", mux)
	http.ListenAndServe(":8080", api)
}
