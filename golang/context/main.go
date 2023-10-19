package main

import (
	"log"
	"net/http"
)

func hello(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()

	// a context is created for each request.

	log.Println("server: hello handler has started")
	defer log.Println("server: hello handler has ended")
}
