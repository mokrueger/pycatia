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


class SchAppConnectable(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppConnectable
                | 
                | Represents an application object that can be connected to
                | others.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_connectable = com_object

    def app_add_connector(self, i_class_type: str, o_new_app_cntr: SchAppConnector) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppAddConnector(CATBSTR iClassType,
                | SchAppConnector oNewAppCntr)
                | 
                |     Add a connector.
                | 
                |     Parameters:
                | 
                |         iClassType
                |             Class type of the connector to be added. 
                |         oNewAppCntr
                |             The new Application Connector object created. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnectable
                |          Dim strVar1 As String
                |          Dim objArg2 As SchAppConnector
                |           ...
                |          objThisIntf.AppAddConnectorstrVar1,objArg2

        :param str i_class_type:
        :param SchAppConnector o_new_app_cntr:
        :rtype: None
        """
        return self.sch_app_connectable.AppAddConnector(i_class_type, o_new_app_cntr.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_add_connector'
        # # vba_code = """
        # # Public Function app_add_connector(sch_app_connectable)
        # #     Dim iClassType (2)
        # #     sch_app_connectable.AppAddConnector iClassType
        # #     app_add_connector = iClassType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_get_reference_name(self, o_reference_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetReferenceName(CATBSTR oReferenceName)
                | 
                |     Get the reference name of a connectable. It will be displayed in
                |     catalogs.
                | 
                |     Parameters:
                | 
                |         oReferenceName
                |             The name of the reference 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnectable
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.AppGetReferenceNamestrVar1

        :param str o_reference_name:
        :rtype: None
        """
        return self.sch_app_connectable.AppGetReferenceName(o_reference_name)

    def app_list_connectables(
            self,
            i_l_cntble_class_filter: SchListOfBSTRs,
            o_l_cntbles: SchListOfObjects,
            o_l_cntrs_on_this_obj: SchListOfObjects,
            o_l_cntrs_on_connected: SchListOfObjects
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppListConnectables(SchListOfBSTRs
                | iLCntbleClassFilter,
                | SchListOfObjects oLCntbles,
                | SchListOfObjects oLCntrsOnThisObj,
                | SchListOfObjects oLCntrsOnConnected)
                | 
                |     Find all the application objects connected to this object through their
                |     connectors.
                | 
                |     Parameters:
                | 
                |         oLCntrClassFilter
                |             A list of all the class types for filtering the output application
                |             objects list. 
                |         oLCntbles
                |             A list of application objects connected to this object. (members
                |             are CATISchAppConnectable interface pointers). 
                |         oLCntrsOnThisObj
                |             A list of connectors on this object through which the connection is
                |             made. (members are CATISchAppConnector interface pointers).
                |             
                |         oLCntrsOnConnected
                |             A list of connectors on the connected objects through which the
                |             connection is made. (members are CATISchAppConnector interface pointers).
                |             Members in this list corresponds to those in oLCntrsOnThisObj in making the
                |             corresponding connections. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnectable
                |          Dim objArg1 As SchListOfBSTRs
                |          Dim objArg2 As SchListOfObjects
                |          Dim objArg3 As SchListOfObjects
                |          Dim objArg4 As SchListOfObjects
                |           ...
                |          objThisIntf.AppListConnectablesobjArg1,objArg2,objArg3,objArg4

        :param SchListOfBSTRs i_l_cntble_class_filter:
        :param SchListOfObjects o_l_cntbles:
        :param SchListOfObjects o_l_cntrs_on_this_obj:
        :param SchListOfObjects o_l_cntrs_on_connected:
        :rtype: None
        """
        return self.sch_app_connectable.AppListConnectables(
            i_l_cntble_class_filter.com_object,
            o_l_cntbles.com_object,
            o_l_cntrs_on_this_obj.com_object,
            o_l_cntrs_on_connected.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_list_connectables'
        # # vba_code = """
        # # Public Function app_list_connectables(sch_app_connectable)
        # #     Dim iLCntbleClassFilter (2)
        # #     sch_app_connectable.AppListConnectables iLCntbleClassFilter
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
                |     Find all the connectors of this application object.
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
                |          Dim objThisIntf As SchAppConnectable
                |          Dim objArg1 As SchListOfBSTRs
                |          Dim objArg2 As SchListOfObjects
                |           ...
                |          Set objArg2 = objThisIntf.AppListConnectors(objArg1)

        :param SchListOfBSTRs i_l_cntr_class_filter:
        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_app_connectable.AppListConnectors(i_l_cntr_class_filter.com_object))

    def app_list_valid_cntr_types(self) -> SchListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListValidCntrTypes() As SchListOfBSTRs
                | 
                |     List the valid application connector types allowed to be
                |     created.
                | 
                |     Parameters:
                | 
                |         oLValidCntrTypes
                |             A list of connector class types allowed. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnectable
                |          Dim objArg1 As SchListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.AppListValidCntrTypes

        :rtype: SchListOfBSTRs
        """
        return SchListOfBSTRs(self.sch_app_connectable.AppListValidCntrTypes())

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
                |             The application connector object to be removed 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnectable
                |          Dim objArg1 As SchAppConnector
                |           ...
                |          objThisIntf.AppRemoveConnectorobjArg1

        :param SchAppConnector i_cntr_to_remove:
        :rtype: None
        """
        return self.sch_app_connectable.AppRemoveConnector(i_cntr_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_remove_connector'
        # # vba_code = """
        # # Public Function app_remove_connector(sch_app_connectable)
        # #     Dim iCntrToRemove (2)
        # #     sch_app_connectable.AppRemoveConnector iCntrToRemove
        # #     app_remove_connector = iCntrToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_set_reference_name(self, i_reference_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppSetReferenceName(CATBSTR iReferenceName)
                | 
                |     Set the reference name of a connectable. It will be displayed in
                |     catalogs.
                | 
                |     Parameters:
                | 
                |         iReferenceName
                |             The name of the reference 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppConnectable
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.AppSetReferenceNamestrVar1

        :param str i_reference_name:
        :rtype: None
        """
        return self.sch_app_connectable.AppSetReferenceName(i_reference_name)

    def __repr__(self):
        return f'SchAppConnectable(name="{self.name}")'
