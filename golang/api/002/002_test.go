package main_test

import (
	"testing"

	"github.com/stretchr/testify/assert"

	. "api"
)

func TestNormaliseUrl(t *testing.T) {
	url := "https://cht.SH/btrfs/"
	actual := NormaliseUrl("cht.sh", url)
	expected := "cht.sh/btrfs"

	t.Run("Normalise Url", func(t *testing.T) {
		assert.Equal(t, expected, actual, "Url was not normalised")
	})
}

func TestGetUrlsFromHtml(t *testing.T) {
	actual := GetUrlsFromHtml("0.0.0.0:8080")
	expected := []string{"cht.sh", "0.0.0.0:8080/path/"}

	t.Run("Check if urls were crawled successfully", func(t *testing.T) {
		assert.Equal(t, expected, actual, "Link parsing failed")
	})
}
