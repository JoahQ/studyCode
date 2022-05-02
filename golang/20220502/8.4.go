package main

import (
	"errors"
	"fmt"
)

type Robot interface {
	PowerOn() error
}

type T850 struct {
	Name string
}

func (a *T850) PowerOn() error {
	return nil
}

type R2d2 struct {
	Boken bool
}

func (r *R2d2) PowerOn() error {
	if r.Boken {
		return errors.New("R2d2 is broken")
	} else {
		return nil
	}
}

func Boot(r Robot) error {
	return r.PowerOn()
}
func main() {
	t := T850{
		Name: "The Terminator",
	}

	r := R2d2{Boken: true}

	err := Boot(&r)
	if err != nil {
		fmt.Printf("err: %v\n", err)
	} else {
		fmt.Println("Robot is powered on!")
	}

	err = Boot(&t)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Robot is powered on!")
	}

	r.Boken = false
	err = Boot(&r)
	if err != nil{
		fmt.Println(err)
	}else{
		fmt.Printf("%v is powered on!\n", r)
	}

	s := "I am an interpreted string literal \nnI am an interpreted string literal \n\tt I am an interpreted string literal "
	fmt.Printf("s: %v\n", s)

	s1 := `I am an interpreted string literal 
	nI am an interpreted string literal 
		t I am an interpreted string 
			literal`
	fmt.Printf("s: %v\n", s1)

	ss := "Can you hear me?"
	ss += "\nHear me screamin'?"
	fmt.Printf("ss: %v\n", ss)
}
