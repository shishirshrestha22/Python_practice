#A PROGRAM THAT ALLOWS A ROBOT TO MOVE IN 2D COORDINATE SYSTEM
#SHOULD START FROM (0,0) AND END IF THE NEXT POINT IS (999,999)
import math
print("------Robot Program------")
def get_next_point(step):
    x=int(input(f"Input x{step} coordinates: "))
    y=int(input(f"Input y{step} coordinates: "))
    return (x,y)
def cal_distance(p1,p2):
    x1 ,y1 =p1
    x2,y2 = p2
    distance = math.sqrt((x2 -x1)**2+(y2-y1)**2)
    return distance
    
def main():
    current_point = (0,0)
    total_distance = 0
    step = 1

    while True:
        next_point = get_next_point(step)
        if next_point == (999,999):
            break
        d = cal_distance(current_point,next_point)
        print(f"step {step}:{d:.2f} units")
        total_distance += d
        current_point = next_point
        step +=1
    print("----------------------")
    print(f"Total distance travelled by the robot: {total_distance:.2f} units ")
if __name__ == "__main__":
    main()