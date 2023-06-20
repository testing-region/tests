# Pointers

```go
a := 42
b := a
```

- Go copies the data in `a` and assigns it to `b`. `b` and `a` point to different locations in memory.
- A pointer allows different variables to point to the same memory location.

```go
var a int = 42
var b *int = &a
fmt.Println(a, *b)
```

- `*int` refers to a pointer to an integer.

> To define the data type of a pointer, precede its name with `*`.

- `&` is called the `address of` operator.
- `b` is not holding the value 42, but the memory location of the data.
- When `*` precedes a pointer, it is referred to as a **dereferencing operator**. It gets the value of the data that the memory address points to.

```go
// from the code above
fmt.Println(*b)     // displays 42
```

## Using Pointers Without Declaring variables

```go
type myStruct struct {
    some int
}

func main() {
    var ms *myStruct
    ms = &myStruct{some: 24}
    fmt.Println(ms)
}
```

### The `new()` Function

- It does not use the object initialisation syntax. It creates an empty object.

```go
var ms *myStruct
ms = new(myStruct)
```
- To be able to use the struct field that the pointer has been initialised to using the `new()` function, you have to deference it to get access to the struct and consequently to the fields it has.

```go
(*ms).some = 21
```
> Dereferencing of pointers is implicit in go. Instead of `(*ms).some = 21`, you could also write `ms.some = 21` and get the same results.
> This only works if the pointer was created using the `new()` function.

## Pointer Arithmetic

- Pointer arithmetic is not allowed in Go by default.
- If you need to do it, you can import the `unsafe` package.

## What is The Use Cases for Pointers

- Copying large structs.
- Mutability of variables (when using functions).
- Enforces API consistency.
- To signify true absence of a value (since an empty pointer holds `<nil>`).

# Note

- The zeroth value of an initialised pointer holds the value, `<nil>`.
- The dereferencing operator, `*` has lower precedence compared to the dot operator, `.`. When dereferencing pointers, use parameters to make sure the pointer is deferenced before any field is accessed (in the case of structs).
- All assignments in Go are copy operations. However, slices and maps contain internal pointers. Hence, they point to the same underlying data.

