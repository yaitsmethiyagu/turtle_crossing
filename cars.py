from turtle import Turtle,Screen
import random

#CAR_GAP = 0.1

direction_option = [0, 180]
car_colors = ["red", "green", "blue", "pink", "orange", "grey"]


class Cars():

    def __init__(self):
        self.car_speed = 1
        self.number_of_lane = 2
        self.road = []
        self.create_road()


    def add_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(car_colors))
        new_car.penup()
        new_car.shapesize(1, random.randint(1, 4))
        return new_car

    def create_lane(self):
        lane = []

        random_cars = random.randint(4, 10)
        for i in range(random_cars):
            new_car = self.add_car()
            new_car.setx(random.randint(-380, 380))
            lane.append(new_car)
        # number_of_cars = len(lane)
        # equal_space_between = int(800 / number_of_cars)
        # gap_lower = int(equal_space_between + (equal_space_between * CAR_GAP))
        # gap_higher = int(equal_space_between - (equal_space_between * CAR_GAP))

        # for cars in lane:
        #     i = lane.index(cars) + 1
        #     cars.setx(random.randint(-400 * i * gap_lower, -400 * i * gap_higher))

        return lane

    def create_road(self):

        for i in range(self.number_of_lane):
            self.road.append(self.create_lane())

        number_of_lanes = len(self.road)
        equal_gap = int(550 / number_of_lanes)

        for lanes in self.road:
            car_direction = random.choice(direction_option)
            lane_number = self.road.index(lanes)
            for cars in lanes:
                cars.sety(-240 + (lane_number * equal_gap))
                cars.setheading(car_direction)

    def cars_move(self):
        for lanes in self.road:
            for cars in lanes:
                cars.forward(20 * self.car_speed)
                if (cars.heading() == 0 and cars.xcor() > 440) or (cars.heading() == 180 and cars.xcor() < -440):
                    new_x = cars.xcor() * -1
                    cars.setx(new_x)


    def increase_car_speed(self):

        for lanes in self.road:
            for cars in lanes:
                cars.reset()
                cars.hideturtle()

        self.road.clear()
        self.car_speed *= 1.05
        if self.number_of_lane < 10:
            self.number_of_lane += 1

        self.road = []
        self.create_road()


    def check_collision(self, object):
        for lanes in self.road:
            for cars in lanes:
                car_size = cars.shapesize()[1]
                car_player_distance = cars.distance(object)
                car_y_differnce = cars.ycor() - object.ycor()
                safe_distance = 10 + (car_size * 10)

                # print(cars.shapesize())
                # print(cars.distance(object))

                #print(car_size)
                if cars.ycor() >= object.ycor():
                    if (car_player_distance <= safe_distance) and (car_y_differnce < 30):
                        # print(f"car size {car_size}")
                        # print(f"car distance {cars.distance(object)}")
                        # print(f"player y cor{object.ycor()}")
                        # print(f"car y cor {cars.ycor()}")
                        # print (f"player - car {(cars.ycor() - object.ycor())}")
                        print(f" SIZE {car_size}, distance {car_player_distance}, ydis {car_y_differnce}")
                        print(f" {safe_distance} >= {cars.distance(object)} ")

                        return True
