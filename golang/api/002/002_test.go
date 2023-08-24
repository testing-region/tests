package main_test

import (
	"net/http"
	"testing"

	"github.com/stretchr/testify/assert"
	"golang.org/x/net/html"

	. "api"
)

func TestNormaliseUrl(t *testing.T) {
	url := "https://cht.SH/btrfs/"
	actual := NormaliseUrl(url)
	expected := "cht.sh/btrfs"

	t.Run("Normalise Url", func(t *testing.T) {
		assert.Equal(t, expected, actual, "Url was not normalised")
	})
}

func TestGetUrlsFromHtml(t *testing.T) {
	r, err := http.Get("http://0.0.0.0:8080/")
	if err != nil {
		t.Fatal(err)
	}

	inputHtml, err := html.Parse(r.Body)
	if err != nil {
		t.Fatal(err)
	}

	actual := GetUrlsFromHtml(inputHtml)
	expected := []string{"cht.sh", "boot.dev"}

	t.Run("Check if urls were crawled successfully", func(t *testing.T) {
		assert.Equal(t, expected, actual, "Link parsing failed")
	})
}
