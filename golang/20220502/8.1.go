package main

import (
	"fmt"
	"math"
	"strconv"
)

type Movie struct {
	Name   string
	Rating float64
}

func (m *Movie) summary() string {
	r := strconv.FormatFloat(m.Rating, 'f', 1, 64)
	return m.Name + ", " + r
}

type Sphere struct {
	Radius float64
}

func (s *Sphere) SurfaceArea() float64 {
	return float64(4) * math.Pi * (s.Radius * s.Radius)
}
func (s *Sphere) Volume() float64 {
	radiusCubed := s.Radius * s.Radius * s.Radius
	return (float64(4) / float64(3)) * math.Pi * radiusCubed
}

type Triangle struct{
	base float32
	height float32
}

func (t *Triangle) changeBase(f float32){
	t.base = f
	return
}
func main() {
	m := Movie{
		Name:   "Spiderman",
		Rating: 3.2,
	}

	fmt.Println(m.summary())

	s := Sphere{
		Radius: 5,
	}
	
	fmt.Println(s.SurfaceArea())
	fmt.Printf("s.Volume(): %v\n", s.Volume())

	t := Triangle{base:3,height:1}
	fmt.Printf("t: %v\n", t)
	t.changeBase(4)
	fmt.Printf("t: %v\n", t)
}
