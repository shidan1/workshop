// written by Elvin B. Gibson, Jr. (c) 2004//
 
 
 
//Array for your pictures//
 
// put the # of pictures in ()//
 
images=new Array(3)
 
 
 
//Array images//
 
 
 
images[0]=new Image;
 
 
 
//put your 1st image name//
 
images[0].src="welcome.jpg";
 
images[1]=new Image;
 
 
 
//put your 2nd image name//
 
images[1].src="imthe.jpg";
 
 
 
//put your 3rd image name//
 
images[1].src="jss01-big.gif";
 
 
 
//repeat the above process for more images//
 
 
 
//set to zero so the function has starting point//
 
index = 0;
 
 
 
function banner()
 
{
 
document.banner.src = images[index].src;
 
index++;
 
 
 
//Literal number of images//
 
if (index==2)
 
{
 
//restarts//
 
index=0;
 
}
 
 
 
//Time for each picture to run milliseconds//
 
setTimeout("banner()",1000);
 
return;
 
}