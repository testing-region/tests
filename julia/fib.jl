print("Enter a number: ")
n = parse(BigInt, readline())

function fibonnaci(n)
    x::BigInt = 1
    y::BigInt = 0

    for i in 1:n
	y = x + y
	println(y)
	x = y - x
    end
end

fibonnaci(n)
