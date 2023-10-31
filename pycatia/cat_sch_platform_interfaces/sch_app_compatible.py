#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchAppCompatible(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppCompatible
                | 
                | Provide application rules of how to connect objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_compatible = com_object

    def app_is_target_ok_for_insert(
            self,
            i_l_comp_source_cntrs: SchListOfObjects,
            o_l_source_cntrs: SchListOfObjects,
            o_b_yes: bool
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppIsTargetOKForInsert(SchListOfObjects
                | iLCompSourceCntrs,
                | SchListOfObjects oLSourceCntrs,
                | boolean oBYes)
                | 
                |     Query whether a component (source) is compatible to be inserted into this
                |     route. This method is used when inserting a component into a route. This mehtod
                |     should only be implemented on a route object. For a component object, the
                |     method should simply returns oBYes=FALSE.
                | 
                |     Parameters:
                | 
                |         iLCompSourceCntrs
                |             A list of connectors on the source component. The target (to be
                |             connected) is "this" route. 
                |         oLSourceCntrs
                |             A list of compatible and available connectors on the source
                |             component (the input) that can be connected to the target ("this" route)
                |             (members are CATISchAppConnector interface pointers)
                |             
                |         oBYes
                |             If TRUE, the object is OK to be connected to a route.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchAppCompatible
                |          Dim objArg1 As SchListOfObjects
                |          Dim objArg2 As SchListOfObjects
                |          Dim bVar3 As boolean
                |           ...
                |         objThisIntf.AppIsTargetOKForInsertobjArg1,objArg2,bVar3

        :param SchListOfObjects i_l_comp_source_cntrs:
        :param SchListOfObjects o_l_source_cntrs:
        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_compatible.AppIsTargetOKForInsert(
            i_l_comp_source_cntrs.com_object,
            o_l_source_cntrs.com_object,
            o_b_yes
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_is_target_ok_for_insert'
        # # vba_code = """
        # # Public Function app_is_target_ok_for_insert(sch_app_compatible)
        # #     Dim iLCompSourceCntrs (2)
        # #     sch_app_compatible.AppIsTargetOKForInsert iLCompSourceCntrs
        # #     app_is_target_ok_for_insert = iLCompSourceCntrs
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_is_target_ok_for_place(
            self,
            i_l_comp_source_cntrs: SchListOfObjects,
            o_l_target_cntrs: SchListOfObjects,
            o_b_yes: bool
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppIsTargetOKForPlace(SchListOfObjects
                | iLCompSourceCntrs,
                | SchListOfObjects oLTargetCntrs,
                | boolean oBYes)
                | 
                |     Query whether a component (source) is compatible to be connected to "this"
                |     object (the target, which can be a route or a component). This method is used
                |     when placing a component to be connected to another
                |     object.
                | 
                |     Parameters:
                | 
                |         iLCompSourceCntrs
                |             A list of connectors on the source component. The target (to be
                |             connected) is "this" component. 
                |         oLOKCntrs
                |             A list of compatible and available connectors on "this" component
                |             (the target) to be connected to the source component (the input source).
                |             (members are CATISchAppConnector interface pointers)
                |             
                |         oBYes
                |             If TRUE, the object is OK to be connected to a route.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchAppCompatible
                |          Dim objArg1 As SchListOfObjects
                |          Dim objArg2 As SchListOfObjects
                |          Dim bVar3 As boolean
                |           ...
                |         
                |         objThisIntf.AppIsTargetOKForPlaceobjArg1,objArg2,bVar3

        :param SchListOfObjects i_l_comp_source_cntrs:
        :param SchListOfObjects o_l_target_cntrs:
        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_compatible.AppIsTargetOKForPlace(
            i_l_comp_source_cntrs.com_object,
            o_l_target_cntrs.com_object,
            o_b_yes
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_is_target_ok_for_place'
        # # vba_code = """
        # # Public Function app_is_target_ok_for_place(sch_app_compatible)
        # #     Dim iLCompSourceCntrs (2)
        # #     sch_app_compatible.AppIsTargetOKForPlace iLCompSourceCntrs
        # #     app_is_target_ok_for_place = iLCompSourceCntrs
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_is_target_ok_for_route(
            self,
            i_route_cntr_class_type: str,
            o_lok_cntrs: SchListOfObjects,
            o_b_yes: bool
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppIsTargetOKForRoute(CATBSTR iRouteCntrClassType,
                | SchListOfObjects oLOKCntrs,
                | boolean oBYes)
                | 
                |     Query whether a route of the input class type can be connected to "this"
                |     object (the target, which can be a route or a component). This method is used
                |     when routing a route.
                | 
                |     Parameters:
                | 
                |         iRouteCntrClassType
                |             Class type of a schematic route connector. 
                |         oLOKCntrs
                |             A list of compatible and available connectors on this object.
                |             (members are CATISchAppConnector interface pointers)
                |             
                |         oBYes
                |             If TRUE, the object is OK to be connected to a route.
                |             
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppCompatible
                |          Dim strVar1 As String
                |          Dim objArg2 As SchListOfObjects
                |          Dim bVar3 As boolean
                |           ...
                |         
                |         objThisIntf.AppIsTargetOKForRoutestrVar1,objArg2,bVar3

        :param str i_route_cntr_class_type:
        :param SchListOfObjects o_lok_cntrs:
        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_compatible.AppIsTargetOKForRoute(
            i_route_cntr_class_type,
            o_lok_cntrs.com_object,
            o_b_yes
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_is_target_ok_for_route'
        # # vba_code = """
        # # Public Function app_is_target_ok_for_route(sch_app_compatible)
        # #     Dim iRouteCntrClassType (2)
        # #     sch_app_compatible.AppIsTargetOKForRoute iRouteCntrClassType
        # #     app_is_target_ok_for_route = iRouteCntrClassType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchAppCompatible(name="{self.name}")'
