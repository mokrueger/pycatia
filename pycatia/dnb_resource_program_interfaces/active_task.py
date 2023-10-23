#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_resource_program_interfaces.task import Task
from pycatia.system_interfaces.any_object import AnyObject


class ActiveTask(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ActiveTask
                | 
                | Represents the Active task of the resource in conjunction with a particular
                | activity.
                | 
                | Role: Active Task is the object used to access and manage the active task set
                | for all the resources assigned for the activity.
                | The following code snippet can be used to obtain the Active Task from the
                | activity.
                | 
                |    Dim objChildActivity As Activity
                |    Dim objActiveActivity As ActiveTask
                |    
                |    Set objActiveActivity = objChildActivity.GetTechnologicalObject("ActiveTask")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.active_task = com_object

    def get_active_task(self, i_resource: AnyObject, o_task: Task) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetActiveTask(AnyObject iResource,
                | Task oTask)
                | 
                |     Retrieves the Active Task for an activity for a particular
                |     Resource.
                | 
                |     Parameters:
                | 
                |         iResource
                |             The resources. 
                |         oTask
                |             The Active Task. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The status could be successfully queried from the
                |             activity
                |         E_FAIL
                |             The query failed.
                | 
                |         Example:
                |             The following example get the active task of the particular
                |             resource in the activity.
                | 
                |                Dim oActiveAct As ActiveTask
                |                Dim iResPrgMngr As ResourceProgramManager
                |                Dim oTask As Task
                |                ..
                |                oActiveAct.GetActiveTask iResPrgMngr, oTask

        :param AnyObject i_resource:
        :param Task o_task:
        :rtype: None
        """
        return self.active_task.GetActiveTask(i_resource.com_object, o_task.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_active_task'
        # # vba_code = """
        # # Public Function get_active_task(active_task)
        # #     Dim iResource (2)
        # #     active_task.GetActiveTask iResource
        # #     get_active_task = iResource
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_active_task(self, i_resource: AnyObject, i_task: Task) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetActiveTask(AnyObject iResource,
                | Task iTask)
                | 
                |     Defines the Active Task for an activity for a particular
                |     Resource.
                | 
                |     Parameters:
                | 
                |         iResource
                |             The resources that owns the Task. 
                |         iTask
                |             The Tasks to be made active. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Active Task was corrrectly set
                |         E_FAIL
                |             The Active Task was not corrrectly set
                | 
                |         Example:
                |             The following example sets Active Task for an activity for a
                |             particular Resource.
                | 
                |                Dim iActiveAct As ActiveTask
                |                Dim iResPrgMngr As ResourceProgramManager
                |                Dim iTask As Task
                |                ..
                |                oActiveAct.SetActiveTask iResPrgMngr, iTask

        :param AnyObject i_resource:
        :param Task i_task:
        :rtype: None
        """
        return self.active_task.SetActiveTask(i_resource.com_object, i_task.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_active_task'
        # # vba_code = """
        # # Public Function set_active_task(active_task)
        # #     Dim iResource (2)
        # #     active_task.SetActiveTask iResource
        # #     set_active_task = iResource
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ActiveTask(name="{self.name}")'
