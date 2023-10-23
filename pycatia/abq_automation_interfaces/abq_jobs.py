#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_job import ABQJob
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQJobs(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQJobs
                | 
                | The collection of Abaqus (ABQJob) objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQJob)
        self.abq_jobs = com_object

    def add(self) -> ABQJob:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As ABQJob
                | 
                |     Creates a new Abaqus job and adds it to the collection of Abaqus
                |     jobs.
                | 
                |     Returns:
                |         oJob The Abaqus job object that was created. 
                |     Example:
                |         The following example creates a job in the ABQJobs
                |         collection:
                | 
                |          Dim abaqusJobs As ABQJobs
                |          Dim abqJob As ABQJob
                |          Set abaqusJobs = abqCase.Jobs
                |          Set abqJob =  abaqusJobs.Add()

        :rtype: ABQJob
        """
        return ABQJob(self.abq_jobs.Add())

    def item(self, i_index: cat_variant) -> ABQJob:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQJob
                | 
                |     Returns an Abaqus job using its index or its name from the ABQJobs
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus job to retrieve from the
                |             collection of Abaqus jobs. If the index is a number, it specifies the rank of
                |             the Abaqus job in the collection. The index of the first Abaqus job in the
                |             collection is 1, and the index of the last job is Count. If the index is a
                |             string, it specifies the name you assigned to the job using the
                |             CATIACollection::Name property. 
                | 
                |     Returns:
                |         oJob The specified ABQJob.

        :param cat_variant i_index:
        :rtype: ABQJob
        """
        return ABQJob(self.abq_jobs.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus Job using its index or its name from the job
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the job to retrieve from the collection of
                |             jobs. As a numeric, this index is the rank of the job in the collection. The
                |             index of the first job in the collection is 1, and the index of the last job is
                |             Count. As a string, it is the name you assigned to the job using the
                |             CATIABase::Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_jobs.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_jobs)
        # #     Dim iIndex (2)
        # #     abq_jobs.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQJobs(name="{self.name}")'
