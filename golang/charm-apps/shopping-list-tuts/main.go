package main

import (
	"fmt"
	"os"

	tea "github.com/charmbracelet/bubbletea"
)

/*
Bubbletea programs is comprised of a model that describes the application
state and the three main methods on that model:
  `Init()` -> initial command for application to run
  `Update()` -> handles incoming events and updates the model accordingly
  `View()` -> renders the UI based on the data in the model
*/

// Create model
type model struct {
	choices  []string         // shopping items
	cursor   int              // item the cursor is pointing
	selected map[int]struct{} // selected items
}

// initialisation stage
func initialModel() model {
	return model{
		choices: []string{
			"Ice cream",
			"Bread",
			"Salad",
			"Chips",
			"Carrots",
		},
		selected: make(map[int]struct{}),
	}
}

/*
Init method

`Cwd` allows the method to perform input/output operations.
Returning nil translates to "no command.
*/
func (m model) Init() tea.Cmd {
	return nil
}

// Update method
func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {

	// is it a key press?
	case tea.KeyMsg:

		// what key was pressed?
		switch msg.String() {
		case "ctrl+c", "q":
			return m, tea.Quit // exit the program

		case "up", "k":
			if m.cursor > 0 {
				m.cursor-- // move the cursor up
			}

		case "down", "j":
			if m.cursor < len(m.choices)-1 {
				m.cursor++ // move the cursor down
			}

		case "enter", " ":
			if _, ok := m.selected[m.cursor]; ok {
				delete(m.selected, m.cursor)
			} else {
				m.selected[m.cursor] = struct{}{}
			}
		}
	}

	// return the updated model
	return m, nil
}

func (m model) View() string {
	// add headers
	s := "Grocery List\n\n"

	for i, choice := range m.choices {
		// is the cursor on this choice?
		cursor := " " // no cursor
		if m.cursor == i {
			cursor = ">"
		}

		// is this choice selected?
		checked := " " // not selected
		if _, ok := m.selected[i]; ok {
			checked = "x" // selected
		}

		// Render the row
		s += fmt.Sprintf("%s [%s] %s\n", cursor, checked, choice)
	}

	s += "\nPress q to quit.\n"

	return s
}

func main() {
	p := tea.NewProgram(initialModel())
	if _, err := p.Run(); err != nil {
		fmt.Printf("Alas, there's been an error: %v", err)
		os.Exit(1)
	}
}
