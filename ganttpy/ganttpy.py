import matplotlib.pyplot as plt
import datetime

class Ganttpy():
    """

    """

    def __init__(self, date_format):
        """

            date_format is the same format used in the datetime.strptime function, and must be
            the same in all dates
            If date_format is not defined, the date is assumed to be an UTC timestamp or datetime instance.
        Args:
            date_format (str): Format code based on 1989 C standard to treat dates inputs in ganttpy.
        """

        pass

    def add_task(self, task_name, start_date, end_date):
        pass

    def input_from_df(self, key_mapping=None):
        pass

    def input_from_lists(self, task_name, start_date, end_date):

    def plot(self):
        pass

    def show(self):
        pass

    def export(self):
        pass
