package main

import (
	"fmt"
	"time"
)

func ping1(c chan string) {
	fmt.Println("11111111111111111111111111")
	time.Sleep(time.Second * 3)
	c <- "ping on channel1"

}

func ping2(c chan string) {
	fmt.Println("22222222222222222222222")
	time.Sleep(time.Second * 2)
	c <- "ping on channel2"

}

func main() {
	channel1 := make(chan string)
	channel2 := make(chan string)

	go ping1(channel1)
	go ping2(channel2)

	select {
	case msg1 := <-channel1:
		fmt.Printf("msg1: %v\n", msg1)
	case msg2 := <-channel2:
		fmt.Printf("msg2: %v\n", msg2)
	case <-time.After(500 * time.Millisecond):
		fmt.Println("no messages received. giving up.")
	}
}
