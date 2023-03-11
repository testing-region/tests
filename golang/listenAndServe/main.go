package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	fileserver := http.FileServer(http.Dir("../go-server/static"))

	http.Handle("/", fileserver)

	fmt.Println("Server is starting...")

	if err := http.ListenAndServe(":8080", nil); err == nil {
		log.Println(err)
	}
}
