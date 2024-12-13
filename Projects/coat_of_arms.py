###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("summer")
q1=codesters.Square(100,100,200, 'Navy')
q2=codesters.Square(-100,100,200, 'DeepPink')
q3=codesters.Square(-100,-100,200, 'violet')
q4=codesters.Square(100,-100,200, 'RoyalBlue')
s1=codesters.Sprite("soccerball",100,100)
s1.set_size(1.7)
s2=codesters.Sprite("puppy (1)",-110,-100)
s2.set_size(0.2)
s3=codesters.Sprite("cardinal", 100, -100)
s3.set_size(0.8)
s4=codesters.Sprite("roblox2",-100,100)
s4.set_size(0.4)

message1=codesters.Text("Josie Salazar Hanson",0,220,"black")
message2=codesters.Text("My room. My clothes. My bed.",0,-220,"black")