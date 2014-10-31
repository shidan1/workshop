from svmutil import svm_predict
from Project.ScriptVector import scriptVectorize
from Project.TrainData import createModel

def evaluate(s):
    values = scriptVectorize(s)
    m = createModel()
    p_label, p_acc, p_val = svm_predict([0], values, m, '-q')
    return p_label


s = r'''
function onMouseDrag(t){lastDelta=t.delta}function onMouseUp(t){var i=new Ball(t.point,lastDelta);balls.push(i),lastDelta=null}function onFrame(){for(var t=0,i=balls.length;i>t;t++)balls[t].iterate()}var Ball=function(t,i){this.vector=!i||i.isZero()?5*Point.random():2*i,this.point=t,this.dampen=.4,this.gravity=3,this.bounce=-.6;var a={hue:360*Math.random(),saturation:1,brightness:1},o=new Gradient([a,"black"],!0),s=this.radius=50*Math.random()+30,e=new CompoundPath({children:[new Path.Circle({radius:s}),new Path.Circle({center:s/8,radius:s/3})],fillColor:new Color(o,0,s,s/8)});this.item=new Group({children:[e],transformContent:!1,position:this.point})};Ball.prototype.iterate=function(){var t=view.size;this.vector.y+=this.gravity,this.vector.x*=.99;var i=this.point+this.vector;(i.x<this.radius||i.x>t.width-this.radius)&&(this.vector.x*=-this.dampen),(i.y<this.radius||i.y>t.height-this.radius)&&(Math.abs(this.vector.x)<3&&(this.vector=Point.random()*[150,100]+[-75,20]),this.vector.y*=this.bounce);var a=Point.max(this.radius,this.point+this.vector);this.item.position=this.point=Point.min(a,t-this.radius),this.item.rotate(this.vector.x)};for(var balls=[],i=0;10>i;i++){var position=Point.random()*view.size,vector=(Point.random()-[.5,0])*[50,100],ball=new Ball(position,vector);balls.push(ball)}var textItem=new PointText({point:[20,30],fillColor:"black",content:"Click, drag and release to add balls."}),lastDelta;
'''
print(evaluate(s))
