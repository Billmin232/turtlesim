#To do: Hacer las montañas utilizando el pose de la tortuga3

import rclpy
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen, TeleportAbsolute, Spawn
from std_srvs.srv import Empty
from turtlesim.msg import Pose

class TurtleController:
    def __init__(self):
        self.node = rclpy.create_node('my_node')
        self.publisher = self.node.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.publisher2 = self.node.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.subscriber = self.node.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.subscriber2 = self.node.create_subscription(Pose, 'turtle2/pose', self.pose_callback, 10)
        self.pose = Pose()

    def pose_callback(self, msg):
        self.pose = msg

    def pose_callback2(self, msg2):
        self.pose = msg2

    # Mueve la tortuga1 seguna una velocidad normal i angular
    def move(self, linear_speed, angular_speed):
        msg = Twist()
        msg.linear.x = linear_speed
        msg.angular.z = angular_speed
        self.publisher.publish(msg)

    #Mueve la tortuga2 seguna una velocidad normal i angular
    def move2(self, linear_speed, angular_speed):
        msg2 = Twist()
        msg2.linear.x = linear_speed
        msg2.angular.z = angular_speed
        self.publisher2.publish(msg2)

    #Canva el color de la linia de la tortuga1 al especificado segun rgb
    def change_pen_color(self, r, g, b, width):
        set_pen = self.node.create_client(SetPen, 'turtle1/set_pen')
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width

        future = set_pen.call_async(request)
        rclpy.spin_until_future_complete(self.node, future)

    #Canva el color de la linia de la tortuga2 al especificado segun rgb
    def change_pen_color2(self, r, g, b, width):
        set_pen = self.node.create_client(SetPen, 'turtle2/set_pen')
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width

        future = set_pen.call_async(request)
        rclpy.spin_until_future_complete(self.node, future)

    #Teletransporta la tortuga1 a las cordenadas especificadas
    def teleport_turtle(self, x, y):
        teleport_absolute = self.node.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        request = TeleportAbsolute.Request()
        request.x = x
        request.y = y
        request.theta = 0.0  # Facing upwards

        future = teleport_absolute.call_async(request)
        rclpy.spin_until_future_complete(self.node, future)

    #Crea tortugas en la coredenadas especificadas
    def create_new_turtle(self, x, y, theta):
        spawn_turtle = self.node.create_client(Spawn, '/spawn')
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta

        future = spawn_turtle.call_async(request)
        rclpy.spin_until_future_complete(self.node, future)

    #Limpieza de la pantalla
    def clear_turtlesim(self):
        reset = self.node.create_client(Empty, '/reset')
        request = Empty.Request()

        future = reset.call_async(request)
        rclpy.spin_until_future_complete(self.node, future)

    #Movimiento de las tortugas basico
    def run(self):
        i = 0
        rate = self.node.create_rate(10)
        while i < 1000:
            linear_speed = 35.0
            angular_speed = 50.0
            self.move(linear_speed, angular_speed)
            self.move2(linear_speed, 0.0)
            rate.sleep()
            i = i + 1

def main(args=None):

    msg = Twist()
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    turtle_controller.clear_turtlesim()
    turtle_controller.create_new_turtle(0.0, 1.0, 0.0)      #Crear turtle2
    turtle_controller.create_new_turtle(0.0, 2.5, 0.0)      #Crear turtle3
    turtle_controller.change_pen_color(69, 86, 255, 0)   #Canviar el color de la linia de turtle1 a el del fondo
    turtle_controller.teleport_turtle(9.0, 8.5)                   #Teleop de turtle1 a la esquina superior derecha
    turtle_controller.change_pen_color(255, 255, 0, 65)  #Canviar el color de la linia de turtle1 a el del sol
    turtle_controller.change_pen_color2(0, 255, 0, 120)  #Canviar el color de la linia de turtle1 a el del prado
    turtle_controller.run()   #Ejecutar el movimiento de las tortugas
    rclpy.shutdown()

if __name__ == '__main__':
    main()
