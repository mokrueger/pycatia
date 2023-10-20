#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connector import SchAppConnector
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchAppConnection(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppConnection
                | 
                | Manage a schematic connection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_connection = com_object

    def app_add_connector(self, i_cntr_to_add: SchAppConnector) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppAddConnector(SchAppConnector iCntrToAdd)
                | 
                |     Add a connector.
                | 
                |     Parameters:
                | 
                |         iCntrToAdd
                |             The Application Connector to be added to the connection
                |             
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnection
                |          Dim objArg1 As SchAppConnector
                |           ...
                |          objThisIntf.AppAddConnectorobjArg1

        :param SchAppConnector i_cntr_to_add:
        :return: None
        :rtype: None
        """
        return self.sch_app_connection.AppAddConnector(i_cntr_to_add.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_add_connector'
        # # vba_code = """
        # # Public Function app_add_connector(sch_app_connection)
        # #     Dim iCntrToAdd (2)
        # #     sch_app_connection.AppAddConnector iCntrToAdd
        # #     app_add_connector = iCntrToAdd
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_list_connectables(
            self,
            i_l_cntble_class_filter: SchListOfBSTRs,
            o_l_cntbles: SchListOfObjects,
            o_l_cntrs: SchListOfObjects
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppListConnectables(SchListOfBSTRs
                | iLCntbleClassFilter,
                | SchListOfObjects oLCntbles,
                | SchListOfObjects oLCntrs)
                | 
                |     Find all the application object connected to this connection through their
                |     connectors.
                | 
                |     Parameters:
                | 
                |         oLCntrClassFilter
                |             A list of all the class types for filtering the output application
                |             objects list. 
                |         oLCntbles
                |             A list of application objects connected to this connection.
                |             (members are CATISchAppConnectable interface pointers).
                |             
                |         oLCntrs
                |             A list of connectors through which this connection is made.
                |             (members are CATISchAppConnector interface pointers).
                |             
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnection
                |          Dim objArg1 As SchListOfBSTRs
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchListOfObjects
                |           ...
                |         
                |         objThisIntf.AppListConnectablesobjArg1,objArg2,objArg3

        :param SchListOfBSTRs i_l_cntble_class_filter:
        :param SchListOfObjects o_l_cntbles:
        :param SchListOfObjects o_l_cntrs:
        :return: None
        :rtype: None
        """
        return self.sch_app_connection.AppListConnectables(
            i_l_cntble_class_filter.com_object,
            o_l_cntbles.com_object,
            o_l_cntrs.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_list_connectables'
        # # vba_code = """
        # # Public Function app_list_connectables(sch_app_connection)
        # #     Dim iLCntbleClassFilter (2)
        # #     sch_app_connection.AppListConnectables iLCntbleClassFilter
        # #     app_list_connectables = iLCntbleClassFilter
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_list_connectors(self, i_l_cntr_class_filter: SchListOfBSTRs) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListConnectors(SchListOfBSTRs iLCntrClassFilter) As
                | SchListOfObjects
                | 
                |     Find all the connectors included in this connection.
                | 
                |     Parameters:
                | 
                |         oLCntrClassFilter
                |             A list of all the class types for filtering the output connector
                |             list. 
                |         oLCntrs
                |             A list of connectors included in this connection. (members are
                |             CATISchAppConnector interface pointers). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnection
                |          Dim objArg1 As SchListOfBSTRs
                |          Dim objArg2 As SchListOfObjects
                |           ...
                |          Set objArg2 = objThisIntf.AppListConnectors(objArg1)

        :param SchListOfBSTRs i_l_cntr_class_filter:
        :return: SchListOfObjects
        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_app_connection.AppListConnectors(i_l_cntr_class_filter.com_object))

    def app_remove_connector(self, i_cntr_to_remove: SchAppConnector) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppRemoveConnector(SchAppConnector iCntrToRemove)
                | 
                |     Remove a connector.
                | 
                |     Parameters:
                | 
                |         iCntrToRemove
                |             The Application Connector to be removed 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnection
                |          Dim objArg1 As SchAppConnector
                |           ...
                |          objThisIntf.AppRemoveConnectorobjArg1

        :param SchAppConnector i_cntr_to_remove:
        :return: None
        :rtype: None
        """
        return self.sch_app_connection.AppRemoveConnector(i_cntr_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_remove_connector'
        # # vba_code = """
        # # Public Function app_remove_connector(sch_app_connection)
        # #     Dim iCntrToRemove (2)
        # #     sch_app_connection.AppRemoveConnector iCntrToRemove
        # #     app_remove_connector = iCntrToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchAppConnection(name="{self.name}")'