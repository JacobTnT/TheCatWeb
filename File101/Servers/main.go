package main

import (
	"fmt"
	"net/http"
)

func main() {

	http.HandleFunc("/hello-biden", helloUser)
	http.ListenAndServe(":8080", nil)
}
func helloUser(writer http.ResponseWriter, request *http.Request) {
	var greeting = "WebOCats!"
	
	fmt.Fprintln(writer, greeting)
}

func printTasks(JacobItems []string) {
	fmt.Println("Free Info")

	for index, Jacob := range JacobItems {
		fmt.Printf("%d: %s/n", index+1, Jacob)
	}
}
func addTask(JacobItems []string, newJacob string) []string {
	var updatedJacobItems = append(JacobItems, newJacob)
	return updatedJacobItems
}

