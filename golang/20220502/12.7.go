package main

import (
	"fmt"
	"time"
)

func sender(c chan string) {
	t := time.NewTicker(1 * time.Second)
	for {
		c <- "I'm sending a message"
		<-t.C
	}
}

func main() {
	messages := make(chan string)
	stop := make(chan bool)
	go sender(messages)
	go func() {
		time.Sleep(time.Second * 5)
		fmt.Println("Time is up!")
		stop <- true

	}()
	for {
		select {
		case <- stop:
			return
		case msg := <- messages:
			fmt.Println(msg)
			
		}
	}
}
