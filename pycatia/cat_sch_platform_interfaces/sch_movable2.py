#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchMovable2(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchMovable2
                | 
                | Manage rotation of a schematic object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_movable2 = com_object

    def rotate_at_point(self, i_db1_rotation_angle_in_radian: float, i_db2_center_point: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RotateAtPoint(double iDb1RotationAngleInRadian,
                | CATSafeArrayVariant iDb2CenterPoint)
                | 
                |     Rotate a schematic object with an angle in radian at a
                |     point.
                | 
                |     Parameters:
                | 
                |         iDb1RotationAngleInRadian
                |             Rotation angle (from x-axis) in radian. 
                |         iDb2CenterPoint
                |             X-Y components of a center point of rotation. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchMovable2
                | 
                |          Dim dbVar2(2) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.RotateAtPoint,dbVar2

        :param float i_db1_rotation_angle_in_radian:
        :param tuple i_db2_center_point:
        :rtype: tuple
        """
        return self.sch_movable2.RotateAtPoint(i_db1_rotation_angle_in_radian, i_db2_center_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'rotate_at_point'
        # # vba_code = """
        # # Public Function rotate_at_point(sch_movable2)
        # #     Dim iDb1RotationAngleInRadian (2)
        # #     sch_movable2.RotateAtPoint iDb1RotationAngleInRadian
        # #     rotate_at_point = iDb1RotationAngleInRadian
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchMovable2(name="{self.name}")'
