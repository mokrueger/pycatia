#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_route import SchRoute
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class SchAppRoute(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppRoute
                | 
                | Manage a schematic route.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_route = com_object

    def app_break(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppBreak() As AnyObject
                | 
                |     Break the application route into 2 routes.
                | 
                |     Parameters:
                | 
                |         oNewAppRoute
                |             New application route 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppRoute
                |          Dim objArg1 As AnyObject
                |           ...
                |          Set objArg1 = objThisIntf.AppBreak

        :rtype: AnyObject
        """
        return AnyObject(self.sch_app_route.AppBreak())

    def app_create_local_reference(self, i_document_to_put_copy_in: Document) -> 'SchAppRoute':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppCreateLocalReference(Document iDocumentToPutCopyIn) As
                | SchAppRoute
                | 
                |     Make a local route reference in another document by copying an existing one
                |     in the current document.
                | 
                |     Parameters:
                | 
                |         iDocumentToPutCopyIn
                |             Pointer to the document to make the copy in 
                |         oSchAppRoute
                |             Pointer to the copy. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppRoute
                |          Dim objArg1 As Document
                |          Dim objArg2 As SchAppRoute
                |           ...
                |          Set objArg2 = objThisIntf.AppCreateLocalReference(objArg1)

        :param Document i_document_to_put_copy_in:
        :rtype: SchAppRoute
        """
        return SchAppRoute(self.sch_app_route.AppCreateLocalReference(i_document_to_put_copy_in.com_object))

    def app_ok_to_branch(self, i_branch_class_type: str, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToBranch(CATBSTR iBranchClassType,
                | boolean oBYes)
                | 
                |     Query whether it is OK to create branch.
                | 
                |     Parameters:
                | 
                |         iBranchClassType
                |             Class type of the branch to create. 
                |         oBYes
                |             If TRUE, then it is OK to create a branch from an application route
                |
                |     Example:
                | 
                |          Dim objThisIntf As SchAppRoute
                |          Dim strVar1 As String
                |          Dim bVar2 As boolean
                |           ...
                |          objThisIntf.AppOKToBranchstrVar1,bVar2

        :param str i_branch_class_type:
        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_route.AppOKToBranch(i_branch_class_type, o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_branch'
        # # vba_code = """
        # # Public Function app_ok_to_branch(sch_app_route)
        # #     Dim iBranchClassType (2)
        # #     sch_app_route.AppOKToBranch iBranchClassType
        # #     app_ok_to_branch = iBranchClassType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_break(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToBreak(boolean oBYes)
                | 
                |     Query whether it is OK to break.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to break the application route
                |             
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppRoute
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToBreakbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_route.AppOKToBreak(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_break'
        # # vba_code = """
        # # Public Function app_ok_to_break(sch_app_route)
        # #     Dim oBYes (2)
        # #     sch_app_route.AppOKToBreak oBYes
        # #     app_ok_to_break = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_concatenate(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToConcatenate(boolean oBYes)
                | 
                |     Query whether it is OK to concatenate.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to concatenate the application route with
                |             another 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppRoute
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToConcatenatebVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_route.AppOKToConcatenate(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_concatenate'
        # # vba_code = """
        # # Public Function app_ok_to_concatenate(sch_app_route)
        # #     Dim oBYes (2)
        # #     sch_app_route.AppOKToConcatenate oBYes
        # #     app_ok_to_concatenate = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_modify_points(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToModifyPoints(boolean oBYes)
                | 
                |     Query whether it is OK to modify (add or remove) the
                |     points.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to add or remove the points from the
                |             application route 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppRoute
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToModifyPointsbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_route.AppOKToModifyPoints(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_modify_points'
        # # vba_code = """
        # # Public Function app_ok_to_modify_points(sch_app_route)
        # #     Dim oBYes (2)
        # #     sch_app_route.AppOKToModifyPoints oBYes
        # #     app_ok_to_modify_points = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_post_break_process(self, i_old_app_route: SchRoute, i_new_app_route: SchRoute) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostBreakProcess(SchRoute iOldAppRoute,
                | SchRoute iNewAppRoute)
                | 
                |     Post process after breaking an application route into 2
                |     pieces.
                | 
                |     Parameters:
                | 
                |         iOldAppRoute
                |             The old application route object 
                |         iNewAppRoute
                |             The new Application route object 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppRoute
                |          Dim objArg1 As SchRoute
                |          Dim objArg2 As SchRoute
                |           ...
                |          objThisIntf.AppPostBreakProcessobjArg1,objArg2

        :param SchRoute i_old_app_route:
        :param SchRoute i_new_app_route:
        :rtype: None
        """
        return self.sch_app_route.AppPostBreakProcess(i_old_app_route.com_object, i_new_app_route.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_post_break_process'
        # # vba_code = """
        # # Public Function app_post_break_process(sch_app_route)
        # #     Dim iOldAppRoute (2)
        # #     sch_app_route.AppPostBreakProcess iOldAppRoute
        # #     app_post_break_process = iOldAppRoute
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_post_concatenate_process(self, i_sch_route2: SchRoute) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostConcatenateProcess(SchRoute iSchRoute2)
                | 
                |     Post process after concatenate 2 application routes into
                |     one.
                | 
                |     Parameters:
                | 
                |         iSchRoute2
                |             Second route to be concatenate to this. This route will be deleted.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchAppRoute
                |          Dim objArg1 As SchRoute
                |           ...
                |          objThisIntf.AppPostConcatenateProcessobjArg1

        :param SchRoute i_sch_route2:
        :rtype: None
        """
        return self.sch_app_route.AppPostConcatenateProcess(i_sch_route2.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_post_concatenate_process'
        # # vba_code = """
        # # Public Function app_post_concatenate_process(sch_app_route)
        # #     Dim iSchRoute2 (2)
        # #     sch_app_route.AppPostConcatenateProcess iSchRoute2
        # #     app_post_concatenate_process = iSchRoute2
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchAppRoute(name="{self.name}")'
