#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_work_interfaces.wi_text import WIText


class WIChangeNotification(WIText):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBWorkInterfaces.WIText
                |                         WIChangeNotification

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.wi_change_notification = com_object

    def get_parameters_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetParametersList() As CATSafeArrayVariant
                | 
                |     Gets a List of Parameters defined on this activity
                |     Role: Gets a List of Parameters defined on this activity
                | 
                |     Parameters:
                | 
                |         iPath
                |             a CATSafeArrayVariant of CATBSTR that has the list of Parameters.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: tuple
        """
        return self.wi_change_notification.GetParametersList()

    def set_parameters_list(self, i_list_of_parameters: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetParametersList(CATSafeArrayVariant
                | iListOfParameters)
                | 
                |     Sets a List of Parameters defined on this activity
                |     Role: Sets a List of Parameters defined on this activity
                | 
                |     Parameters:
                | 
                |         iPath
                |             a CATSafeArrayVariant of CATBSTR that has the list of Parameters.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param tuple i_list_of_parameters:
        :rtype: None
        """
        return self.wi_change_notification.SetParametersList(i_list_of_parameters)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameters_list'
        # # vba_code = """
        # # Public Function set_parameters_list(wi_change_notification)
        # #     Dim iListOfParameters (2)
        # #     wi_change_notification.SetParametersList iListOfParameters
        # #     set_parameters_list = iListOfParameters
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'WIChangeNotification(name="{self.name}")'
