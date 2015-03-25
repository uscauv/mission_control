#!/usr/bin/env python

__author__ = 'vmagro'

import rospy
import smach
import smach_ros

from direction_marker_align.msg import AlignAction


def main():
    rospy.init_node('smach_example_state_machine')

    sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
    with sm:
        smach.StateMachine.add()
        smach.StateMachine.add('DIRECTION_MARKER_ALIGN',
                               smach_ros.SimpleActionState('direction_marker_align',
                                                           AlignAction),
                               transitions={'succeeded': 'succeeded'})

        # so that we can monitor it in the ros sm visualization tools
        # Create and start the introspection server
        sis = smach_ros.IntrospectionServer('mission_control', sm, '/mission_control_sm')
        sis.start()

        # Execute SMACH plan
        outcome = sm.execute()

        rospy.spin()
        sis.stop()


if __name__ == '__main__':
    main()