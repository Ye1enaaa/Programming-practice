const person = {
    "name": "Erickson",
    "age": 22,
    "course": "BSIT",
    get crs(){
        return this.course
    }
}

console.log(person.crs, person.course)
