/*
Counter script
By JavaScript Kit (http://javascriptkit.com)
Over 400+ free scripts here!
Above notice MUST stay entact for use
*/

function fakeCounter(){

//decrease/increase counter value (depending on perceived popularity of your site!)
var decreaseIncrease = 50000;

var counterDate=new Date();
var currentHits=counterDate.getTime().toString();
currentHits=parseInt(currentHits.substring(2,currenthits.length-4))+decreaseIncrease;

document.write("You are visitor # <b>"+currentHits+"</b> to my site!");
}
fakeCounter();