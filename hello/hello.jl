function fact(x)::BigInt
    if x == 1
	return 1
    else
	return x * fact(x-1)
    end
end

println(fact(99999))
