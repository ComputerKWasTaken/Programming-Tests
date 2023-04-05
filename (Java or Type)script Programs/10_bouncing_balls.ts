// Typescript code for a window with 10 bouncing balls in the middle
// Each ball can be dragged and moved around

// Define a class for a ball object
class Ball {
    // Properties: x and y coordinates, radius, color, velocity
    x: number;
    y: number;
    r: number;
    color: string;
    vx: number;
    vy: number;
  
    // Constructor: initialize the properties with random values
    constructor() {
      this.x = Math.random() * window.innerWidth;
      this.y = Math.random() * window.innerHeight;
      this.r = Math.random() * 50 + 10;
      this.color = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
      this.vx = Math.random() * 10 - 5;
      this.vy = Math.random() * 10 - 5;
    }
  
    // Method: draw the ball on the canvas context
    draw(ctx: CanvasRenderingContext2D) {
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
      ctx.fill();
      ctx.closePath();
    }
  
    // Method: update the position and velocity of the ball
    update() {
      // Bounce off the edges of the window
      if (this.x + this.r > window.innerWidth || this.x - this.r < 0) {
        this.vx = -this.vx;
      }
      if (this.y + this.r > window.innerHeight || this.y - this.r < 0) {
        this.vy = -this.vy;
      }
      // Move by adding the velocity to the coordinates
      this.x += this.vx;
      this.y += this.vy;
    }
  
    // Method: check if the ball is being dragged by the mouse
    drag(mouseX: number, mouseY: number) {
      // Calculate the distance between the mouse and the ball center
      let dx = mouseX - this.x;
      let dy = mouseY - this.y;
      let dist = Math.sqrt(dx * dx + dy * dy);
      // If the distance is less than the radius, set the ball position to the mouse position
      if (dist < this.r) {
        this.x = mouseX;
        this.y = mouseY;
        // Set the velocity to zero to stop bouncing
        this.vx = 0;
        this.vy = 0;
      }
    }
  }
  
  // Get the canvas element and its context
  let canvas = document.getElementById("canvas") as HTMLCanvasElement;
  let ctx = canvas.getContext("2d");
  
  // Set the canvas size to match the window size
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  
  // Create an array of 10 balls
  let balls: Ball[] = [];
  for (let i = 0; i < 10; i++) {
    balls.push(new Ball());
  }
  
// Define a function to animate the balls 
function animate(): void { 
    // Check if ctx is null or undefined 
    if (ctx === null || ctx === undefined) return; 
    // Clear the canvas 
    ctx.clearRect(0, 0, canvas.width, canvas.height); 
    // Loop through the balls array 
    for (let ball of balls) { 
      // Draw each ball 
      ball.draw(ctx); 
      // Update each ball's position and velocity 
      ball.update(); 
      // Drag each ball if the mouse is pressed on it 
      ball.drag(mouseX, mouseY); 
    } 
    // Request the next animation frame 
    requestAnimationFrame(animate); 
  }  
  
  // Define variables to store the mouse position
  let mouseX = -1;
  let mouseY = -1;
  
  // Add an event listener for mouse move
  canvas.addEventListener("mousemove", function (e) {
    // Get the mouse position relative to the canvas
    mouseX = e.clientX - canvas.offsetLeft;
    mouseY = e.clientY - canvas.offsetTop;
  });
  
  // Call the animate function to start the animation loop
  animate();