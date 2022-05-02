package main

import (
	"errors"
	"fmt"
	"io/ioutil"
)

func main() {
	file, err := ioutil.ReadFile("D:\\vscodewsp\\golang\\hello\\2.1\\foo.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("file: %v\n", file)
	fmt.Printf("file: %s\n", file)

	e := errors.New("Something went wrong")
	if e != nil {
		fmt.Printf("e: %v\n", e)
	}
	name, role := "Richard Jupp", "Drumer"
	ee := fmt.Errorf("The %v %v quit", role, name)

	if ee != nil {
		fmt.Println(ee)
	}

	panic("Oh no. I can do no more. Goodbye.")
	fmt.Println("This is not executed")
}
