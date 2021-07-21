var pos = 0 	//starting position

// Getting the box element
var box = document.getElementById("box")

function move(){
    console.log(this.pos)
	this.pos += 10
	box.style.left = String(this.pos + "px") 
}


setInterval(move, 1000)

