package main

import (
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/bwmarrin/discordgo"
)

func main() {
	sess, err := discordgo.New("Bot {token...}")
	if err != nil {
		log.Println(err)
	}

	// handle create msg event
	sess.AddHandler(func(s *discordgo.Session, m *discordgo.MessageCreate) {
		// check if bot is the one sending the message
		if m.Author.ID == s.State.User.ID {
			return
		}

		// check msg content by users and make the bot respond
		if m.Content == "hello" {
			s.ChannelMessageSend(m.ChannelID, "world!")
		}
	})

	// send intent to discord servers
	sess.Identify.Intents = discordgo.IntentsAllWithoutPrivileged

	// create a session
	err = sess.Open()
	if err != nil {
		log.Fatal(err)
	}

	defer sess.Close()
	fmt.Println("Bot is online")

	// keep session online until user closes it
	sc := make(chan os.Signal, 1) // exit status 1 (CTRL-C)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt)
	<-sc
}
