function loop(x::Int64)
    while x != 0
    for num = 1:1000
       if x % 2 == 0
           x /= 2
           println(x)
       else
           x = 3x+1
           println(x)
       end
   end
   end
end
   
