import rospy
from std_msgs.msg import Float64
import sys, select, termios, tty

# define the teleop class
class Teleop(object):

    
    def __init__(self):
        
        rospy.init_node('teleop_node')
        topic1 = '/rrbot/joint1_position_controller/command'
        topic2 = '/rrbot/joint2_position_controller/command'
        self.pub1 = rospy.Publisher(topic1, Float64, queue_size=10)
        self.pub2 = rospy.Publisher(topic2, Float64, queue_size=10)
        self.rate = rospy.Rate(100)  # 10hz
        self.command1 = Float64()
        self.command2 = Float64()
        self.command1.data = 0
        self.command2.data = 0

    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def run(self):
        global settings
        settings = termios.tcgetattr(sys.stdin)

        rospy.loginfo("Use arrow keys to move the robot.")
        
        while not rospy.is_shutdown():
            key = self.getKey()
            if key == '\x03':
                break
            """
            if key == 'A':
                self.command1.data = self.command1.data + 0.087
                pass
            elif key == 'B':
                self.command1.data = self.command1.data - 0.087
                pass
            elif key == 'C':
                self.command2.data = self.command2.data + 0.087
                pass
            elif key == 'D':
                self.command2.data = self.command2.data - 0.087
                pass
            """
            if key == 'A' and key == 'C':
                self.command1.data = self.command1.data + 0.087
                self.command2.data = self.command1.data + 0.087
                pass
            elif key == 'A' and key == 'D':
                self.command1.data = self.command1.data + 0.087
                self.command2.data = self.command1.data - 0.087
                pass 
            elif key == 'B' and key == 'C':
                self.command1.data = self.command1.data - 0.087
                self.command2.data = self.command1.data + 0.087
                pass
            elif key == 'B' and key == 'D':
                self.command1.data = self.command1.data - 0.087
                self.command2.data = self.command1.data - 0.087
                pass  
            else:
                continue
        

            self.pub1.publish(self.command1)
            self.pub2.publish(self.command2)
            self.rate.sleep()

if __name__ == '__main__':
    teleop = Teleop()
    teleop.run()
