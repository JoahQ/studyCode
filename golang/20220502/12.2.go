package main

import (
	"fmt"
	"time"
)
var cc chan string = make(chan string)
func slowFunc() {
	time.Sleep(time.Second * 2)
	cc <- "slowFunc() finished"
}

func main() {
	// cc := make(chan string)
	go slowFunc()
	msg := <- cc

	fmt.Printf("msg: %v\n", msg)
}
