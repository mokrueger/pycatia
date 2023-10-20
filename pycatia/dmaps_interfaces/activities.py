#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Activities(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Activities
                | 
                | The collection of activities related to the current activity.
                | 
                | It respectively manages the children hierarchy, the downstream control flow,
                | the uptream control flow, the downstream product flow or the upstream product
                | flow.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Activity)
        self.activities = com_object

    def add(self, i_activity: Activity) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Add(Activity iActivity)
                | 
                |     This method adds the specified activity as a precedence
                |     constraint
                | 
                |     Parameters:
                | 
                |         iActivity
                |             The activity Handle

        :param Activity i_activity:
        :return: None
        :rtype: None
        """
        return self.activities.Add(i_activity.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add'
        # # vba_code = """
        # # Public Function add(activities)
        # #     Dim iActivity (2)
        # #     activities.Add iActivity
        # #     add = iActivity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def item(self, i_index: cat_variant) -> Activity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Activity
                | 
                |     This method gets the specified activity on the current activities
                |     management.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The activity identifier 
                | 
                |     Returns:
                |         oActivity The activity

        :param cat_variant i_index:
        :return: Activity
        :rtype: Activity
        """
        return Activity(self.activities.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     This method removes the specified activity on the current activities
                |     management.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The activity identifier

        :param cat_variant i_index:
        :return: None
        :rtype: None
        """
        return self.activities.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(activities)
        # #     Dim iIndex (2)
        # #     activities.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Activities(name="{self.name}")'