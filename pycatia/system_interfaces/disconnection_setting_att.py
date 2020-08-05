#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class DisconnectionSettingAtt(SettingController):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         DisconnectionSettingAtt
                | 
                | Represents the base object to handle the parameters of automatic
                | disconnection.
                | If the automatic disconnection is enable, the V5 session will be kill after a
                | user-defined duration of inactivity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.disconnection_setting_att = com_object

    @property
    def activation_state(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ActivationState() As boolean
                | 
                |     Returns or sets the activation state of automatic
                |     disconnection.
                |     Role:Returns or sets the activation mode of automatic disconnection.

        :return: bool
        """

        return self.disconnection_setting_att.ActivationState

    @activation_state.setter
    def activation_state(self, value):
        """
        :param bool value:
        """

        self.disconnection_setting_att.ActivationState = value

    @property
    def inactivity_duration(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property InactivityDuration() As long
                | 
                |     Returns or sets the inactivity duration.
                |     Role: Returns or sets the timeout in seconds before the automatic
                |     disconnection when no activity has been detected, if the mechanism is enabled.

        :return: int
        """

        return self.disconnection_setting_att.InactivityDuration

    @inactivity_duration.setter
    def inactivity_duration(self, value):
        """
        :param int value:
        """

        self.disconnection_setting_att.InactivityDuration = value

    def get_activation_state_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetActivationStateInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the activation mode of automatic
                |     disconnection.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.disconnection_setting_att.GetActivationStateInfo(admin_level, o_locked)

    def get_inactivity_duration_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetInactivityDurationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for inactivity
                |     duration.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.disconnection_setting_att.GetInactivityDurationInfo(admin_level, o_locked)

    def set_activation_state_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetActivationStateLock(boolean iLocked)
                | 
                |     Locks or unlocks the activation mode of automatic
                |     disconnection.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.disconnection_setting_att.SetActivationStateLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_activation_state_lock'
        # # vba_code = """
        # # Public Function set_activation_state_lock(disconnection_setting_att)
        # #     Dim iLocked (2)
        # #     disconnection_setting_att.SetActivationStateLock iLocked
        # #     set_activation_state_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_inactivity_duration_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetInactivityDurationLock(boolean iLocked)
                | 
                |     Locks or unlocks the inactivity duration.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.disconnection_setting_att.SetInactivityDurationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_inactivity_duration_lock'
        # # vba_code = """
        # # Public Function set_inactivity_duration_lock(disconnection_setting_att)
        # #     Dim iLocked (2)
        # #     disconnection_setting_att.SetInactivityDurationLock iLocked
        # #     set_inactivity_duration_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DisconnectionSettingAtt(name="{ self.name }")'
