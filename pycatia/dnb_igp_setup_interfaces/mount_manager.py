#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_igp_setup_interfaces.tag import Tag
from pycatia.knowledge_interfaces.list import List
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class MountManager(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MountManager
                | 
                | Represents the Mount Manger of a Robot.
                | 
                | Role: Mount Manager is the object used to access and manage the devices mounted
                | on the robot.
                | The following code snippet can be used to obtain the Mount Manager from the
                | robot product.
                | 
                |    Dim objMountManager As MountManager
                |    Dim objRobot as Product
                |    
                |    Set objMountManager = objRobot.GetTechnologicalObject("MountManager" )
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mount_manager = com_object

    def get_mounted_devices(self, o_device_list: tuple) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMountedDevices(CATSafeArrayVariant oDeviceList)
                | 
                |     Retrieves the list of mounted devices on the Robot
                | 
                |     Parameters:
                | 
                |         oDeviceList
                |             Retrieved list of Mounted devices 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The list of mounted devices could be successfully retrieved from
                |             the robot.
                |         E_FAIL
                |             TThe list of mounted devices could be not be obtained from the
                |             robot
                | 
                |         Example:
                |             The following example retrieves the list of mounted devices on the
                |             Robot.
                | 
                |                Dim objMountManager As MountManager
                |                Dim DeviceList(3) As Product
                |                ..
                |                objMountManager.GetMountedDevices DeviceList

        :param tuple o_device_list:
        :return: Product
        :rtype: Product
        """
        return Product(self.mount_manager.GetMountedDevices(o_device_list))
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_mounted_devices'
        # # vba_code = """
        # # Public Function get_mounted_devices(mount_manager)
        # #     Dim oDeviceList (2)
        # #     mount_manager.GetMountedDevices oDeviceList
        # #     get_mounted_devices = oDeviceList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_device_mounted(self, i_device: Product, i_is_mounted: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub IsDeviceMounted(Product iDevice,
                | boolean iIsMounted)
                | 
                |     Checks if the device is mounted or not on a robot.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             Device for which mount status needs to be checked 
                |         iIsMounted
                |             Retrieved result for the mount status- Mounted(1), Not Mounted(0)
                |
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The status could be successfully queried from the mount
                |             manager
                |         E_FAIL
                |             The query failed.
                | 
                |         Example:
                |             The following example retrieves the list of mounted devices on the
                |             Robot.
                | 
                |                Dim objMountManager As MountManager
                |                Dim Device As Product
                |                Dim IsMounted As Boolean
                |                ..
                |                objMountManager.IsDeviceMounted
                |                Device,IsMounted

        :param Product i_device:
        :param bool i_is_mounted:
        :return: None
        :rtype: None
        """
        return self.mount_manager.IsDeviceMounted(i_device.com_object, i_is_mounted)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'is_device_mounted'
        # # vba_code = """
        # # Public Function is_device_mounted(mount_manager)
        # #     Dim iDevice (2)
        # #     mount_manager.IsDeviceMounted iDevice
        # #     is_device_mounted = iDevice
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def mount_device(
            self,
            i_device: Product,
            i_tool_profile_name: str,
            i_mount_offset: tuple,
            i_tool_mobility: bool,
            i_tool_tag: Tag,
            i_base_tag: Tag
    ) -> List:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub MountDevice(Product iDevice,
                | CATBSTR iToolProfileName,
                | CATSafeArrayVariant iMountOffset,
                | boolean iToolMobility,
                | Tag iToolTag,
                | Tag iBaseTag)
                | 
                |     Mounts the device on to the Robot
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The Device to mount 
                |         iToolProfileName
                |             Name of the Tool Profile 
                |         iMountOffset
                |             Offset required from the mount plate of the robot to base part of
                |             the device including position and orientation. If a Base Tag is selected then
                |             its the offset of MountPlate of the Robot to the Base Tag
                |             
                |         iToolMobility
                |             The Tool Mobility. 
                |         iToolTag
                |             The Tool Tag 
                |         iBaseTag
                |             The Base Tag 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The device is successfully mounted on the Robot.
                |         E_FAIL
                |             The device could not be mounted to the robot.
                | 
                |         Example:
                |             The following example mounts a device to a robot.
                | 
                |                Dim objMountManager As MountManager
                |                Dim Device As Product
                |                ...
                |                Dim ToolMobility As Boolean
                |                ToolMobility = TRUE   
                |                Dim TCPMatrix(5) As List
                |                TCPMatrix(0)=0
                |                TCPMatrix(1)=0
                |                TCPMatrix(2)=0
                |                TCPMatrix(3)=0
                |                TCPMatrix(4)=0
                |                TCPMatrix(5)=0
                |                Dim ToolProfileName As String
                |                ToolProfileName = "Tool.1"
                |                Dim BaseTag as Tag
                |                Dim ToolTag as Tag
                |                ...
                |                objMountManager.MountDevice
                |                object,name2,TCPMatrix,ModifyRef,ToolTag,Nothing

        :param Product i_device:
        :param str i_tool_profile_name:
        :param tuple i_mount_offset:
        :param bool i_tool_mobility:
        :param Tag i_tool_tag:
        :param Tag i_base_tag:
        :return: List
        :rtype: List
        """
        return List(
            self.mount_manager.MountDevice(
                i_device.com_object,
                i_tool_profile_name,
                i_mount_offset,
                i_tool_mobility,
                i_tool_tag.com_object,
                i_base_tag.com_object
            )
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'mount_device'
        # # vba_code = """
        # # Public Function mount_device(mount_manager)
        # #     Dim iDevice (2)
        # #     mount_manager.MountDevice iDevice
        # #     mount_device = iDevice
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def re_mount_device(self, i_device: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ReMountDevice(Product iDevice)
                | 
                |     Remounts the device on the Robot
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to be remount. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The device is successfully remounted on the Robot.
                |         E_FAIL
                |             The device could not be remounted.
                | 
                |         Example:
                |             The following example remounts a device on a
                |             robot.
                | 
                |                Dim objMountManager As MountManager
                |                Dim Device As Product
                |                ..
                |                objMountManager.ReMountDevice Device

        :param Product i_device:
        :return: None
        :rtype: None
        """
        return self.mount_manager.ReMountDevice(i_device.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 're_mount_device'
        # # vba_code = """
        # # Public Function re_mount_device(mount_manager)
        # #     Dim iDevice (2)
        # #     mount_manager.ReMountDevice iDevice
        # #     re_mount_device = iDevice
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def un_mount_device(self, i_device: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnMountDevice(Product iDevice)
                | 
                |     Unmounts the device from the Robot
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to be unmount. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The device is successfully unmounted from the
                |             Robot.
                |         E_FAIL
                |             The device could not be unmounted.
                | 
                |         Example:
                |             The following example unmounts a device from a
                |             robot.
                | 
                |                Dim objMountManager As MountManager
                |                Dim Device As Product
                |                ..
                |                objMountManager.UnMountDevice Device

        :param Product i_device:
        :return: None
        :rtype: None
        """
        return self.mount_manager.UnMountDevice(i_device.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'un_mount_device'
        # # vba_code = """
        # # Public Function un_mount_device(mount_manager)
        # #     Dim iDevice (2)
        # #     mount_manager.UnMountDevice iDevice
        # #     un_mount_device = iDevice
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def un_set_device(self, i_device: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnSetDevice(Product iDevice)
                | 
                |     Unsets the device from the Robot
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to be unset. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The device is successfully unset from the Robot.
                |         E_FAIL
                |             The device could not be unset.
                | 
                |         Example:
                |             The following example unsets a device from a
                |             robot.
                | 
                |                Dim objMountManager As MountManager
                |                Dim Device As Product
                |                ..
                |                objMountManager.UnSetDevice Device

        :param Product i_device:
        :return: None
        :rtype: None
        """
        return self.mount_manager.UnSetDevice(i_device.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'un_set_device'
        # # vba_code = """
        # # Public Function un_set_device(mount_manager)
        # #     Dim iDevice (2)
        # #     mount_manager.UnSetDevice iDevice
        # #     un_set_device = iDevice
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MountManager(name="{self.name}")'