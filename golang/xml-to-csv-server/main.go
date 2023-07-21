package main

import (
	"io"
	"log"
	"net/http"

	convert "DaveSaah/xml-to-csv/conversion"
)

const MAX_UPLOAD_SIZE = 10 * (1024 * 1024) // 10MB

func indexHandler(w http.ResponseWriter, r *http.Request) {
	// serve index.html
	w.Header().Add("Content-Type", "text/html")
	http.ServeFile(w, r, "public/index.html")
}

func uploadHandler(w http.ResponseWriter, r *http.Request) {
	// reject any http requests that is not POST
	if r.Method != "POST" {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}

	// serve upload.html
	w.Header().Add("Content-Type", "text/html")
	http.ServeFile(w, r, "public/upload.html")

	// extract file
	file, _, _ := r.FormFile("xmlFile")

	// convert uploaded file into a string of bytes
	fileBytes, err := io.ReadAll(file)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

	// convert file to csv
	convert.XmlToCsv(fileBytes)
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", indexHandler)
	mux.HandleFunc("/upload", uploadHandler)

	if err := http.ListenAndServe(":8080", mux); err != nil {
		log.Fatal(err)
	}
}
