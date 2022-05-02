package main

import (
	"fmt"
	"time"
)

func receiver(c chan string) {
	for msg := range c {
		fmt.Printf("msg: %v\n", msg)
	}
}
func main() {
	messages := make(chan string, 2)
	messages <- "Hello"
	messages <- "World"
	close(messages)
	fmt.Println("Pushed two messages onto Channel with no receivers")
	time.Sleep(time.Second * 1)
	receiver(messages)

}
